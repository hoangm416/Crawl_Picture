import requests
import os

# Tạo thư mục để lưu ảnh nếu chưa tồn tại
download_folder = "down_images"
os.makedirs(download_folder, exist_ok=True)

# URL của trang web
url = "https://thispersondoesnotexist.com"

# Gửi yêu cầu GET để lấy nội dung trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công hay không
if response.status_code == 200:
    # Tải ảnh về và lưu vào thư mục
    img_data = requests.get(url).content  
    
    #vì là phản hồi là một chuỗi byte nên sẽ dùng ghi mã nhị phân để sao chép lại
    img_path = os.path.join(download_folder, "download.jpg")
    with open(img_path, 'wb') as img_file:
        img_file.write(img_data)

    print(f"Ảnh đã được tải về và lưu vào {img_path}")
else:
    print(f"Không thể truy cập trang web. Mã trạng thái: {response.status_code}")