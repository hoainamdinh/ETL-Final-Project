# ETL-Final-Project
## Giới thiệu
Dự án này thực hiện quá trình ETL (Extract, Transform, Load) bằng Django và Pandas để nhập dữ liệu từ các tệp CSV, Excel, JSON vào cơ sở dữ liệu.
## Yêu cầu hệ thống
- Python 3.10+
- Django 5.0+
- SQLite (hoặc cơ sở dữ liệu khác như PostgreSQL, MySQL)
- Các thư viện Python:
  - `pandas`

## Cài đặt

### 1. Tạo môi trường ảo và cài đặt dependencies
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. Cấu hình database
```sh
python manage.py makemigrations
python manage.py migrate
```

### 3. Chạy server
```sh
python manage.py runserver
```
Truy cập: [http://127.0.0.1:8000/]

## Hướng dẫn sử dụng
1. Mở trang `/upload/` để tải lên tệp dữ liệu.
2. Hệ thống sẽ tự động phân tích, kiểm tra và lưu vào database.
3. Xem dữ liệu đã nhập tại `/display/`.

Just mandatory assignment from mr chucnv :))) chill
