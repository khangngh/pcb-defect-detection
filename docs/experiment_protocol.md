# Quy tắc thực nghiệm

- Dữ liệu: `PCB_Baseline_v1`, fingerprint
  `b1aafdd0aa23fa30b74e77940c04046c47dad786d3b785a737c6547b988e2089`.
- Chia tập: train 7.324 ảnh, validation 1.588 ảnh, test 1.700 ảnh; dùng các
  tệp trong `data/splits/`.
- Seed mặc định: `42`.
- Kích thước đầu vào mặc định: `640`.
- Chọn checkpoint và siêu tham số bằng validation; không dùng test để điều
  chỉnh mô hình.
- Báo cáo tối thiểu: precision, recall, mAP50, mAP50-95, thời gian huấn luyện
  và phần cứng.

Mọi thay đổi đối với dữ liệu hoặc giao thức phải được thảo luận trong pull
request và tạo phiên bản Release mới.
