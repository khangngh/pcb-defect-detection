"""Run once after moving/unpacking the dataset to rewrite data.yaml."""
from pathlib import Path
import json

def bind(root):
    root=Path(root).resolve()
    info=json.loads((root/'dataset_info.json').read_text(encoding='utf-8'))
    text='path: '+json.dumps(root.as_posix(),ensure_ascii=False)+'\n'
    text+='train: images/train\nval: images/val\ntest: images/test\nnames:\n'
    text+=''.join(f'  {i}: {name}\n' for i,name in enumerate(info['classes']))
    path=root/'data.yaml';path.write_text(text,encoding='utf-8');print(path)
    return path

if __name__=='__main__':bind(Path(__file__).resolve().parent)
