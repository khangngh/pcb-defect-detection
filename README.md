# PCB Defect Detection

Dự án phát hiện sáu loại lỗi PCB, so sánh các mô hình baseline và nghiên cứu cải thiện phát hiện lỗi nhỏ.
Nhóm dùng Kaggle để lưu dữ liệu, huấn luyện và giữ checkpoint; GitHub lưu notebook, metadata và kết quả tổng hợp.
VS Code dùng để sửa mã nguồn, review thay đổi và commit.

## Cấu trúc

```text
pcb-defect-detection/
├── README.md
├── .gitignore
├── .github/
│   ├── CODEOWNERS
│   └── pull_request_template.md
├── notebooks/
│   ├── data_preparation.ipynb
│   └── baseline_yolov8n.ipynb
├── data/
│   ├── README.md
│   └── splits/
├── reports/
│   ├── data/
│   └── figures/
└── docs/
    ├── experiment_protocol.md
    └── task_assignment.md
```


## Chạy notebook

1. Tải notebook cần chạy từ `notebooks/`.
2. Import vào Kaggle Notebook, Add Input bộ dữ liệu phù hợp.
3. Notebook chuẩn bị dữ liệu dùng nguồn `VOC_PCB`; notebook baseline dùng `PCB_Baseline_v1` đã xử lý.
4. Phần huấn luyện chọn GPU T4 ×2 nếu có; cấu hình đường dẫn và thư viện trong notebook.
5. Save Version trên Kaggle để lưu output và checkpoint. Đưa notebook cùng báo cáo tổng hợp về GitHub qua PR.

`notebooks/data_preparation.ipynb` đã có quy trình chuẩn bị dữ liệu.
`notebooks/baseline_yolov8n.ipynb` hiện là khung giao việc, **chưa có code huấn luyện hoặc kết quả**.
Không cần thiết lập môi trường huấn luyện trên laptop cho quy trình này.

## Nguồn dữ liệu và giới hạn

Nguồn ban đầu: [HRIPCB / PKU PCB](https://robotics.pkusz.edu.cn/resources/dataset/).

## Dữ liệu

- [Dữ liệu nguồn HRIPCB / PKU PCB](https://www.kaggle.com/datasets/khangisme/hripcb-pku-pcb/)
- [Dữ liệu huấn luyện PCB_Baseline_v1](https://www.kaggle.com/datasets/khangisme/pcb-baseline-v1-zip)
- [Chi tiết và quy tắc sử dụng dữ liệu](data/README.md)

