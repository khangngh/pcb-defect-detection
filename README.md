# PCB Defect Detection

Dự án phát hiện sáu loại lỗi trên bo mạch PCB bằng các mô hình YOLO. Nhánh
`main` chứa notebook chuẩn bị dữ liệu, metadata chia tập đã chốt, cấu hình
chung và các công cụ kiểm tra. Ảnh, nhãn và checkpoint lớn được phát hành
riêng, không commit vào Git.

## Cài đặt

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Dữ liệu dùng chung

Tải `PCB_Baseline_v1.zip` từ Release `data-v1.0`, giải nén vào
`data/processed/PCB_Baseline_v1/`, sau đó kiểm tra:

```powershell
python scripts\verify_dataset.py --root data\processed\PCB_Baseline_v1
```

Nếu dữ liệu ở vị trí khác, tạo `configs/data.local.yaml` từ
`configs/data.example.yaml`. Không sửa các tệp trong `data/splits/`; chúng
định nghĩa cùng một train/validation/test cho cả nhóm.

## Notebook

- [data_preparation.ipynb](notebooks/data_preparation.ipynb): EDA và chuẩn bị
  dữ liệu trên Kaggle.

Các notebook baseline YOLO sẽ được thêm khi thí nghiệm tương ứng hoàn tất.

## Quy ước thí nghiệm

Giữ nguyên seed, kích thước đầu vào, ngân sách huấn luyện và cách tính chỉ số
theo [docs/experiment_protocol.md](docs/experiment_protocol.md). Chọn mô hình
bằng validation và chỉ báo cáo kết quả test một lần ở đánh giá cuối.

## Quy trình đóng góp

Tạo nhánh theo nhiệm vụ, ví dụ `feature/baseline-yolov11n`, rồi mở pull
request vào `main`. Xem [docs/task_assignment.md](docs/task_assignment.md).

## Upload lên GitHub

Repository đích là
[`khangngh/pcb-defect-detection`](https://github.com/khangngh/pcb-defect-detection).
Trong PowerShell, chạy từ thư mục gốc dự án:

```powershell
git init
git branch -M main
git add .
git status
git commit -m "Add PCB defect detection project structure"
git remote add origin https://github.com/khangngh/pcb-defect-detection.git
git push -u origin main
```

Nếu `origin` đã tồn tại, không chạy lại lệnh `git remote add`; dùng:

```powershell
git remote set-url origin https://github.com/khangngh/pcb-defect-detection.git
```

GitHub sẽ yêu cầu đăng nhập hoặc Personal Access Token khi push qua HTTPS.
Không đưa token vào URL, mã nguồn hoặc file cấu hình.

### Upload dataset dưới dạng Release

`PCB_Baseline_v1.zip` và `VOC_PCB.zip` không được đưa vào commit vì `.gitignore`
đã loại `*.zip`. Sau khi push mã nguồn:

1. Mở tab **Releases** của repository và chọn **Draft a new release**.
2. Tạo tag `data-v1.0` trên nhánh `main`.
3. Đặt tiêu đề `PCB baseline dataset v1.0`.
4. Đính kèm `PCB_Baseline_v1.zip`, không đính kèm `VOC_PCB.zip`.
5. Ghi SHA-256 của file trong phần mô tả Release:

   ```text
   78a8aaa095c32d5c6276e05ac792439d49732e4794703dcac9ad05c7d8d70881
   ```

Sau khi Release được tạo, sửa `README.md` nếu cần để bổ sung URL asset chính
thức. Người dùng tải asset về, giải nén vào
`data/processed/PCB_Baseline_v1/`, rồi chạy `verify_dataset.py` như hướng dẫn
ở trên.

### Kiểm tra trước khi push

```powershell
git status --short
git check-ignore -v .\PCB_Baseline_v1.zip .\VOC_PCB.zip
git diff --cached --stat
```

Hai file ZIP phải xuất hiện trong kết quả `git check-ignore`, và không được
xuất hiện trong danh sách file staged.
