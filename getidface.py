import requests, time, os, sys

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    art = [
        "\033[1;35m╔══════════════════════════════════════╗",
        "║        🐯 MENU DGVI TOOL 🐯          ║",
        "╚══════════════════════════════════════╝",
        "\033[1;33m      Tool Lấy ID Facebook Tự Động",
        "        Thương hiệu: DGVIKAKA",
        "──────────────────────────────────────\033[0m"
    ]
    for line in art:
        print(line)
        time.sleep(0.1)

def loading(text="⏳ Đang xử lý", delay=0.2):
    for i in range(3):
        sys.stdout.write(f"\r{text}{'.' * (i+1)}{' ' * (3-i)}")
        sys.stdout.flush()
        time.sleep(delay)
    print("\r" + " " * (len(text)+3), end="\r")  # clear line

banner()

print("🔍 Bạn đang sử dụng tool lấy ID cho: \033[1;36mFacebook\033[0m")
umbala = input("🔗 Nhập Link Facebook cần lấy ID: ").strip()

# ✅ Kiểm tra định dạng link cơ bản
if "facebook.com/" not in umbala or all(x not in umbala for x in ["profile.php?id=", ".com/", "/pages/", "/people/", "/"]):
    print("\033[1;31m❗ Link không hợp lệ! Vui lòng dán link trang cá nhân hoặc page.\033[0m")
    exit()

loading("🚀 Đang gửi yêu cầu")

headers = {
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://id.traodoisub.com/',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {'link': umbala}

try:
    response = requests.post('https://id.traodoisub.com/api.php', headers=headers, data=data, timeout=10)
    loading("📡 Đang nhận dữ liệu")
    if response.status_code == 200:
        json = response.json()
        if 'id' in json:
            print(f"\033[1;32m✅ ID Facebook của bạn là: \033[1;37m{json['id']}\033[0m")
        else:
            print("\033[1;31m❌ Không tìm thấy ID từ link đã nhập.\033[0m")
    else:
        print(f"\033[1;31m⚠️ Lỗi kết nối! Mã lỗi: {response.status_code}\033[0m")
except requests.exceptions.RequestException:
    print("\033[1;31m⚠️ Không thể kết nối tới máy chủ. Kiểm tra mạng hoặc thử lại sau.\033[0m")