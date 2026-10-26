# Phân công và nhánh

Người phụ trách dữ liệu upload `PCB_Baseline_v1` lên Kaggle, cấp quyền truy cập nếu để Private,
rồi bổ sung link và số phiên bản vào README. Mọi người Add Input cùng phiên bản này.

| Nhiệm vụ | Nhánh gợi ý | Sản phẩm đưa vào GitHub |
|---|---|---|
| Chuẩn bị dữ liệu | feature/data-preparation | Notebook, manifest và báo cáo kiểm tra |
| Baseline YOLOv8n | feature/baseline-yolov8n | Notebook và kết quả validation |
| Baseline YOLOv11n | feature/baseline-yolov11n | Notebook và kết quả validation |
| Baseline YOLOv12n | feature/baseline-yolov12n | Notebook và kết quả validation |
| Crop ưu tiên lỗi nhỏ | feature/small-defect-crops | Notebook và báo cáo so sánh dữ liệu |

Chỉ tạo notebook mô hình mới khi bắt đầu nhiệm vụ. Khung `baseline_yolov8n.ipynb` chưa phải mô hình đã huấn luyện.
Tổ chức theo chức năng, không tạo thư mục theo tên thành viên.

## Quy trình

1. Sửa notebook trên nhánh nhiệm vụ trong VS Code hoặc Kaggle.
2. Chạy phần huấn luyện/đánh giá trên Kaggle và Save Version giữ output.
3. Đưa notebook cập nhật và kết quả tổng hợp về nhánh, commit trong VS Code.
4. Mở PR vào `main`, ghi link lần chạy, cấu hình, phiên bản dữ liệu và phần đã kiểm tra.
5. Quản trị viên review trước khi merge theo quy tắc bảo vệ nhánh đã bật.

Không commit ảnh, ZIP, checkpoint hoặc khóa truy cập. Checkpoint nằm trong Kaggle Output.
