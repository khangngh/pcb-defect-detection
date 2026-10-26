# Phân công và nhánh

Tổ chức theo chức năng, không tạo thư mục theo tên thành viên. Mỗi nhiệm vụ
dùng một nhánh riêng, ví dụ:

- `feature/baseline-yolov8n`
- `feature/baseline-yolov11n`
- `feature/baseline-yolov12n`
- `feature/small-defect-crops`

Mở pull request vào `main`, mô tả dữ liệu, cấu hình, kết quả validation và
thay đổi reproducibility. Không commit ảnh, checkpoint, khóa truy cập hoặc
`configs/data.local.yaml`.
