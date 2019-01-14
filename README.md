# LAB ERP (Enterprise Resource Planning)
[![GitHub license](https://img.shields.io/github/license/ERPGroup/lab_erp.svg)](https://github.com/ERPGroup/lab_erp/blob/master/LICENSE)
[![Travis (.org) branch](https://img.shields.io/travis/ERPGroup/lab_erp/master.svg)](https://github.com/ERPGroup/lab_erp)
[![GitHub stars](https://img.shields.io/github/stars/ERPGroup/lab_erp.svg?style=flat-square&label=Stars)](https://github.com/ERPGroup/lab_erp/stargazers)

## Tên đề tài: Xây dựng hệ thống mua bán điện thoại.

### Tiến độ thực thiện công việc

| Tuần          | Công việc                         | Người thực hiện           |
| ------------- |:--------------------------------- |:------------------------- |
| Tuần 1        | Lấy yêu cầu dự án                 | Product Owner             |
| Tuần 2        | Phân tích yêu cầu dự án           | Product Owner + Leader    |
| Tuần 3        | Thiết lập mô hình cho dự án       | Product Owner + Leader    |
| Tuần 4        | Phân tích và xây dựng CSDL        | Database Manager + Leader |
| Tuần 5 - 6    | Front end                         | Fornt-End                 |
| Tuần 7 - 10   | Back end                          | Back-End                  |
| Tuần 11 -12   | Kiểm thử phần mềm                 | Back-End + Leader         |
| Tuần 13       | Kiểm định chất lượng phần mềm     | Product Ower + Back-End   |
| Tuần 14       | Nghiệm thu dự án                  | Leader                    |


## Giới thiệu chung:
***
#### 1. Giới thiệu chung về doanh nghiệp
* Hiện tại doanh nghiệp có một chuỗi cửa hàng gồm một trụ sở và bốn chi nhánh mua bán sản phẩm công nghệ bao gồm điện thoại, laptop, tablet trực tiếp tại chỗ và một website https://tabletplaza.vn/ theo mô hình B2C. 
* Chuỗi cửa hàng cho phép: khách hàng mua bán tại chỗ, đăng ký trả góp.
* Hệ thống website cho phép:
...Nhân viên: đăng các sản phẩm, xác nhận đơn hàng từ khách hàng, xử lý đăng ký trả góp
...Khách hàng: Đặt mua sản phẩm trực tuyến, đăng ký trả góp.
* Hệ thống website do bộ phận kinh doanh, bộ phận quản lý sử dụng trực tiếp tại công ty.

#### 2. Sơ đồ tổ chức doanh nghiệp
> Sơ đồ tổ chức dựa trên mô phỏng sau:
![sodotochuc](https://github.com/ERPGroup/lab_erp/blob/master/document/image/sodotochuc.png "sodotochuc")

#### 3. Mục đích
* Xây dựng HTTT để làm gì? Phục vụ cho bộ phận nào của doanh nghiệp? HTTT mang lại lợi ích gì cho doanh nghiệp
* Doanh nghiệp hiện tại đang có một vấn đề như sau: Công ty chỉ thu mua sản phẩm cũ là sản phẩm của công ty và không nhận mua sản phẩm cũ từ bất cứ nguồn nào khác. Một số khách hàng cần bán điện thoại cũ (không phải sản phẩm của công ty) để mua điện thoại mới, nhưng khi bán sản phẩm ở những nơi khác thì giá rất thấp so với giá trị của nó.
* Vì vậy, cửa hàng mong muốn xây dựng một hệ thống quản lý mua bán điện thoại ( C2C ) cho phép khách hàng mua bán lại sản phẩm cũ với giá cả phù hợp với nhau hoặc cá nhân, doanh nghiệp có nhu cầu bán sản phẩm
* Hệ thống phục vụ cho bộ phận kinh doanh của công ty.
* HTTT tăng thêm doanh thu từ việc bán gói tin để đăng bán sản phẩm, dịch vụ cho thuê quảng cáo. Ngoài ra, người bán sản phẩm vẫn có thể quay lại công ty để mua sản phẩm mới. 

#### 4. Phạm vi hệ thống
> Áp dụng cho bộ phận kinh doanh tại chi nhánh Tp Hồ Chí Minh

## Mô tả chung về hệ thống
***
#### 1. Tổng quan về yêu cầu hệ thống
Hệ thống được xây dựng nhằm mục đích, cung cấp môi trường cho phép khách hàng mua bán sản phẩm với nhau, đồng thời cung cấp thêm dịch vụ quảng cáo cho khách hàng có nhu cầu. Hệ thống có cung cấp thêm chức năng thống kê báo cáo và quản lý người dùng cho người quản trị.

#### 2. Chức năng yêu cầu của hệ thống
> **2.1 Quản lý Mua hàng:** 
* Chức năng tìm kiếm:
    * Tìm kiếm cơ bản: tìm theo từ khóa có thể là tên sản phẩm, mã sản phẩm, loại, ...
    * Tìm kiếm nâng cao: tìm sản phẩm và lọc theo những điều kiện cụ thể như khoảng giá, màu sắc, loại, tên, …
* Liệt kê danh sách sản phẩm.
* Hiển thị chi tiết sản phẩm.
* Quản lý giỏ hàng: 
    * Xem lại thông tin sản phẩm đã chọn. 
    * Cập nhập số lượng.
* Đăng ký, đăng nhập:
    * Đăng ký và xác thực thông qua gmail.
    * Đăng nhập: kiểm tra thông tin tài khoản.
* Thanh toán:
    * Yêu cầu phải đăng nhập mới được thanh toán.
    * Thanh toán: COD hoặc Trực tuyến thông qua Paypal. 
* Nhận xét, đánh giá: khi hóa đơn hoàn tất, cho phép người mua đánh giá người bán. 
* Quản lý đơn hàng: 
    * Xem tình trạng đơn hàng.
    * Xem lịch sử thanh toán.
> **2.2 Quản lý Bán hàng:**
* Đăng ký bán hàng, đăng nhập
    * Đăng ký và xác thực bằng Gmail.
    * Đăng nhập: kiểm tra thông tin tài khoản.
* Quản lý gói tin
    * Xem thông tin gói tin đang có.
    * Mua thêm gói tin.
    * Thanh toán: trực tuyến thông qua Paypal. 
* Đăng tin
    * Kiểm tra số lượng tin tồn.
    * Tự động cập nhập số lượng tin khi đăng tin.
* Quản lý đơn hàng
    * Xác nhận và cập nhập đơn hàng.
    * Đánh giá và nhận xét khi đơn hàng hoàn tất.
    * Xem lịch sử giao dịch.
* Thông kê, báo cáo.
> **2.3 Quản lý Quảng cáo:**
* Đăng ký, đăng nhập
    * Đăng ký: sẽ được cấp tài khoản dành riêng cho thuê quảng cáo.
    * Đăng nhập: Kiểm tra thông tin tài khoản.
* Đăng ký quảng cáo
    * Lựa chọn quảng cáo ( Vị trí, thời gian, giá tiền ).
    * Thực hiện thanh toán trực tuyến thông qua Paypal.
* Quản lý hợp đồng: ( Quản trị viên )
    * Kiểm tra và xác nhận hợp đồng.
    * Xem lịch sử giao dịch hợp đồng.
    * Thanh khoản hợp đồng.
* Thông kê: thực hiện thống kê quảng cáo đang chạy. 
> **2.4 Quản lý Thống kê báo cáo:**
* Thống kê doanh thu
* Thống kê người bán
* Thống kê người mua
* Thống lượt truy cập
> **2.5 Quản lý Tài khoản người dùng:**
* Cấp tài khoản mới
* Phân quyền tài khoản
* Khóa tài khoản

#### 3. Đối tượng người dùng
* Người bán: khoảng 200 - 500 người
* Người mua: khoảng 500 - 1000 người
* Khách hàng thuê quảng cáo: khoảng 50 - 100 người
* Quản trị viên: 2-5 người.

#### 4. Rằng buộc tổng thể
* a. Phần cứng: 1 - 5 server để sử dụng quản lý hệ thống
    * Cấu hình máy: Phần cứng RAM 8GB, CPU Intel Core i5 5200U, HDD 1TB
    * Thiết bị: Máy in, Scan
* b. Phần mềm: Hệ điều hành: Win 7 64bit, Win 10 64bit
* c. Dữ liệu: Dữ liệu được lưu trữ trong hệ QTCSDL Postgresql 9.6
* d. Mạng: Viettel – 100Mbp - Băng thông quốc tế 2.0 Mbp
* e. Con người: Độ tuổi 18-35 tuổi. Có bộ phận chuyên về IT

#### 5. Yêu cầu về giao diện (cho các đối tượng người dùng)
> **Giao diện website**
![Giao dien 1](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien1.png "Giao dien 1")

![Giao dien 2](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien2.png "Giao dien 2")

![Giao dien 3](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien3.png "Giao dien 3")

![Giao dien 4](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien4.png "Giao dien 4")

![Giao dien 5](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien5.png "Giao dien 5")

![Giao dien 6](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien6.png "Giao dien 6")

![Giao dien 7](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien7.png "Giao dien 7")

![Giao dien 8](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien8.png "Giao dien 8")


> **Giao diện người mua (Customer)**
![Giao dien 9](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien9.png "Giao dien 9")

![Giao dien 10](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien10.png "Giao dien 10")

> **Giao diện người bán (Merchant)**
![Giao dien 14](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien14.png "Giao dien 14")

![Giao dien 12](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien12.png "Giao dien 12")

![Giao dien 17](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien17.png "Giao dien 17")

![Giao dien 15](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien15.png "Giao dien 15")

![Giao dien 16](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien16.png "Giao dien 16")

![Giao dien 13](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien13.png "Giao dien 13")


> **Giao diện người quảng cáo (Advertiser)**
![Giao dien 18](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien18.png "Giao dien 18")

![Giao dien 19](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien19.png "Giao dien 19")

![Giao dien 20](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien17.png "Giao dien 20")

![Giao dien 13](https://github.com/ERPGroup/lab_erp/blob/master/document/image/giaodien13.png "Giao dien 13")

> **Giao diện người quản lý (Admin): Kết thừa 2 giao diện Merchant và Advertiver**

#### 6. Sơ đồ UseCase
![UseCase](https://github.com/ERPGroup/lab_erp/blob/master/document/image/usecase.png "UseCase")

#### 7. Thiết kế cơ sở dữ liệu
> Bản thiết kế cuối cùng
![Database](https://github.com/ERPGroup/lab_erp/blob/master/document/image/Database.png "Database")

## Hướng dẫn cài đặt
***
#### 1. Cài đặt Python3.x và Postgresql 9.6
```shell
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```
#### 2. Tạo database và cấp quyển truy cập
```shell
sudo -u postgres psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed'; 
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
```
#### 3. Cài đặt virtualenv
```shell
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
cd ~/
virtualenv lab_erp_env
source lab_erp_env/bin/activate
pip install django gunicorn psycopg2
```
#### 4. Cài đặt mã nguồn
```shell
git clone https://github.com/ERPGroup/lab_erp.git
git checkout master
git pull
cd lab_erp
pip install -r req.txt
```
Tại file /lab_erp/setting.py sửa lại tên database và user được cấp quyền
#### 5. Thiết lập database
Nếu muốn sử dụng dữ liệu có sẵn ta sẽ import file **backup.sql**
```shell
psql dbname < backup.sql
```
Nếu muốn tạo mới database ta chạy câu lệnh sau
```shell
python manage.py migrate
python manage.py shell
from website.models import *
```
Copy các dòng dữ liệu trong file **cmd** và khởi chạy

> Xem demo:
```shell
python manage.py runserver 0.0.0.0:8000
```
Lúc này bạn có thể xem website bằng cách gõ:
```shell
http://domain_or_ip_public:8000
```
Cần cho phép truy cập cổng **8000**, nếu chưa thì cần chạy câu lệnh sau:
```shell
sudo ufw allow 8000 // Bat tuong lua va cho phep truy cap cong 8000
```
#### 6. Cài đặt webserver
```shell
sudo apt-get update
sudo apt-get install nginx
sudo nano /etc/systemd/system/gunicorn.service
```
Bên dưới là các thuộc tính cần có của 1 service chạy trên Ubuntu
```shell
[Unit]
Description=gunicorn daemon
After=network.target
[Service]
User=user-ubuntu
Group=www-data
WorkingDirectory=/home/user-ubuntu/lab_erp
ExecStart=/home/user-ubuntu/lab_erp_env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/user-ubuntu/lab_erp/lab_erp.sock lab_erp.wsgi:application
[Install]
WantedBy=multi-user.target
```

Chạy service:
```shell
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

Lúc này chúng ta sẽ cài đặt service chạy trên nginx
```shell
sudo nano /etc/nginx/sites-available/myproject
```

Bên dưới là đoạn mã cơ bản để chạy service trên Nginx
```shell
server {
    listen 80;
    server_name server_domain_or_IP;
}
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/user-ubuntu/lab_erp;
    }
    location / {
        include proxy_params;
        proxy_pass  http://unix:/home/user-ubuntu/lab_erp/lab_erp.sock;
    }
}
```
#### 7. Cài đặt network
**Nếu khi chạy website xuất hiện thông báo lỗi**
> domain_ip_public’s server IP address could not be found

Có nghĩa server đã không cho phép truy cập qua cổng :80
Yêu cầu tắt tường lửa và cho phép sử dụng cổng :80
```shell
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
```

#### 8. Cài đặt SSL
Hệ thống sử dụng Let’s Encrypt để tạo miễn phí SSL
```shell
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx
```
Cài đặt tên miền cần SSL
```shell
sudo certbot --nginx -d example.com -d www.example.com
```

Certbot sẽ tự động tạo mới private key trên hệ thống và các thiết lập giao thức trên nginx


## Tổng kết

#### 1. Ưu điểm của hệ thống
* Hệ thống chạy tương đối ổn định, đáp ứng được hầu hết các chức năng.
* Có xây dựng back up database cho hệ thống.
* Giao diện thiết kế đúng yêu cầu.
* Có các tính năng bảo mật mã hoá thông tin, xác nhận mail, lập lịch quảng cáo theo yêu cầu, tự động hoá quảng cáo.
* Có xây dựng thêm chatbot hỗ trợ trong hệ thống cho customer.
#### 2. Những vấn đề chưa làm được
> Important: Dự án đã hoàn thiện, tuy nhiên do thời gian không đủ để kiểm thử tất cả các chức nên có thể sẽ có một vài lỗi phát sinh trong quá trình sử dụng.
#### 3. Đề xuất cho hệ thống trong tương lai
* Nâng cấp thêm chức năng thanh toán Online bằng thẻ ngân hàng.
* Nâng cấp thêm chatbot AI – hỗ trợ như một hệ thống CRM. 
* Nâng cấp hệ thống quản lý quảng cáo – cho thuê vị trí quảng cáo theo hình thức mới – một vị trí cho nhiều người thuê cùng một lúc – tăng lợi nhuận.
* Xây dựng thêm hệ thống shipper ( nếu có thể ) tăng thêm lợi nhuận
