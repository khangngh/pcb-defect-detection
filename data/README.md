# Dữ liệu

Dữ liệu ảnh và nhãn không được commit vào repository. Gói baseline dùng chung
được phát hành dưới dạng Release `data-v1.0` với tên `PCB_Baseline_v1.zip`.

Sau khi tải và giải nén, đặt thư mục `PCB_Baseline_v1` tại
`data/processed/PCB_Baseline_v1/` (hoặc dùng `configs/data.local.yaml` để trỏ
đến vị trí khác), rồi chạy:

```powershell
python scripts\verify_dataset.py --root data\processed\PCB_Baseline_v1
```

Các tệp trong `data/splits/` là metadata đã chốt. Không tự chia lại dữ liệu
giữa các thành viên; chỉ dùng test cho đánh giá cuối cùng.
