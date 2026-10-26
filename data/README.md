# Dữ liệu dùng chung

Ảnh và nhãn YOLO được lưu trên Kaggle Dataset `PCB_Baseline_v1`; repo chỉ lưu metadata chia tập.
**Link và số phiên bản Kaggle Dataset: người phụ trách bổ sung sau khi upload.**

## Cách sử dụng

1. Mở notebook baseline trên Kaggle, chọn Add Input và thêm đúng phiên bản dataset của nhóm.
2. Xác định thư mục chứa `dataset_info.json`, `images/`, `labels/` trong input.
3. Tạo YAML làm việc trong `/kaggle/working` theo đường dẫn input đó; không ghi vào input chỉ đọc.
4. Giữ nguyên các split đã chuẩn bị, không tạo lại train/val/test.

Dataset có 10.612 ảnh và 21.592 bbox. Train 7.324 ảnh, validation 1.588 ảnh, test 1.700 ảnh.
56 ảnh thuộc nhóm trùng có nhãn xung đột được cách ly.

ID lớp cố định:

| ID | Lớp |
|---|---|
| 0 | missing_hole |
| 1 | mouse_bite |
| 2 | open_circuit |
| 3 | short |
| 4 | spur |
| 5 | spurious_copper |

`splits/` giữ manifest và cấu hình chia tập; các đường dẫn nguồn trong manifest là dấu vết của phiên Kaggle lúc chuẩn bị,
không phải đường dẫn bắt buộc trên mọi máy. Gói dataset có manifest dùng đường dẫn tương đối.
`../reports/data/dataset_info.json` lưu thông tin của bộ baseline đã xuất.

Notebook chuẩn bị dữ liệu vẫn chứa công cụ kiểm tra và đóng gói; nhóm không cần chạy lại bước này để train baseline.
Với cải tiến dữ liệu, tạo phiên bản train riêng và giữ nguyên validation/test của baseline.
