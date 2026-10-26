# Quy tắc thực nghiệm trên Kaggle

## Dataset cố định

- Dữ liệu dùng chung: `PCB_Baseline_v1` trên Kaggle; cập nhật link và số phiên bản trong README trước khi phân công train.
- Fingerprint: `b1aafdd0aa23fa30b74e77940c04046c47dad786d3b785a737c6547b988e2089`.
- Train 7.324 ảnh, validation 1.588 ảnh, test 1.700 ảnh; giữ manifest trong `data/splits/`.
- Không chia lại và không thêm augmentation vào validation/test.
- Bộ dữ liệu đã có biến thể augmented từ nguồn. Phiên bản crop cải tiến của nhóm chỉ tạo từ train.
- Test hiện có một ID board; ảnh crop/biến thể không phải các board độc lập.

## Cấu hình và đánh giá

- Huấn luyện trên Kaggle; dùng GPU T4 ×2 nếu có và ghi rõ số GPU thực sự được sử dụng.
- Seed mặc định `42`, kích thước đầu vào mặc định `640`.
- Trước khi chạy so sánh, thống nhất ngân sách huấn luyện, batch size và cách chọn checkpoint trong PR.
- Ghi phiên bản Python, PyTorch, Ultralytics và các thay đổi thư viện trong notebook/lần chạy.
- Chọn checkpoint, mô hình và siêu tham số bằng validation. Chỉ dùng test sau khi chốt cấu hình.
- Báo cáo precision, recall, mAP50, mAP50-95, AP từng lớp, thời gian huấn luyện và phần cứng.
- Khi đo tốc độ, dùng cùng điều kiện và ghi rõ phạm vi thời gian được đo.

## Lưu kết quả

- Kaggle Output: checkpoint, log đầy đủ và các file chạy lớn; Save Version để giữ lại.
- GitHub `notebooks/`: notebook tái lập thí nghiệm, không chứa khóa truy cập.
- GitHub `reports/`: bảng so sánh, hình cần thiết, cấu hình và link Kaggle Version tương ứng.
- Mọi thay đổi dataset/giao thức cần PR được duyệt; khi thay đổi dữ liệu, tạo Kaggle Dataset Version mới và ghi rõ ảnh hưởng tới split.
