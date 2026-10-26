"""Verify an exported PCB dataset; Python standard library plus Pillow."""
from pathlib import Path
import argparse
import csv, json, hashlib, math
from collections import defaultdict, Counter
from PIL import Image

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()

def verify(root):
    root=Path(root).resolve()
    with (root/'metadata/manifest.csv').open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))
    spec=json.loads((root/'dataset_info.json').read_text(encoding='utf-8'))
    checksum_lines=(root/'checksums.sha256').read_text().splitlines()
    for line in checksum_lines:
        expected,rel=line.split('  ',1)
        assert digest(root/rel)==expected,f'Checksum mismatch: {rel}'
    seen_paths=set(); hash_splits=defaultdict(set);board_splits=defaultdict(set)
    groups=defaultdict(set); classes=Counter(); counts=Counter();total=0
    for r in rows:
        assert r['split'] in ('train','val','test')
        assert r['image'] not in seen_paths;seen_paths.add(r['image'])
        image=root/r['image'];label=root/r['label']
        with Image.open(image) as im:
            im.load();w,h=im.size
        assert (w,h)==(int(r['width']),int(r['height']))
        assert digest(image)==r['sha256']
        hash_splits[r['sha256']].add(r['split'])
        board_splits[r['board_id']].add(r['split']);groups[r['group_id']].add(r['split'])
        lines=label.read_text().splitlines()
        assert len(lines)==int(r['boxes'])
        for line in lines:
            parts=line.split();assert len(parts)==5,f'Invalid YOLO row: {label}'
            cid=int(parts[0]);x,y,bw,bh=map(float,parts[1:])
            assert 0<=cid<len(spec['classes'])
            assert all(math.isfinite(v) for v in [x,y,bw,bh])
            assert 0<bw<=1 and 0<bh<=1
            assert x-bw/2>=-1e-8 and y-bh/2>=-1e-8
            assert x+bw/2<=1+1e-8 and y+bh/2<=1+1e-8
            classes[(r['split'],cid)]+=1;total+=1
        counts[r['split']]+=1
    assert all(len(s)==1 for m in (hash_splits,board_splits,groups) for s in m.values())
    actual_images={p.relative_to(root).as_posix() for p in (root/'images').rglob('*') if p.is_file()}
    actual_labels={p.relative_to(root).as_posix() for p in (root/'labels').rglob('*.txt')}
    assert actual_images==set(r['image'] for r in rows),'Unexpected/missing image files'
    assert actual_labels==set(r['label'] for r in rows),'Unexpected/missing label files'
    assert len(rows)==spec['images'] and total==spec['boxes']
    for split in ('train','val','test'):
        assert counts[split]>0
        assert all(classes[(split,i)]>0 for i in range(len(spec['classes'])))
        listed=(root/'splits'/f'{split}.txt').read_text().splitlines()
        assert set(listed)=={'../'+r['image'] for r in rows if r['split']==split}
        assert len(listed)==counts[split]
    result={'status':'passed','images':len(rows),'boxes':total,'split_images':dict(counts),
            'split_fingerprint':spec['split_fingerprint'],'checksummed_files':len(checksum_lines)}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Verify an exported PCB dataset.')
    parser.add_argument(
        '--root',
        type=Path,
        default=Path(__file__).resolve().parent.parent / 'data' / 'processed' / 'PCB_Baseline_v1',
        help='Path to the unpacked PCB_Baseline_v1 directory.',
    )
    args = parser.parse_args()
    verify(args.root)
