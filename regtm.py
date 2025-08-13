# -*- coding: utf-8 -*-
# Tool Reg Mail.TM Auto - DGVIKAKA Version VIP 👑

import requests, json, random, time, threading, sys, os
from colorama import init, Fore, Style

init(autoreset=True)

RAINBOW = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.WHITE]

def banner():
    os.system("clear")
    banner_text = [
        "██████╗░██╗░░░██╗██╗  ████████╗░█████╗░░█████╗░██╗░░░░░",
        "██╔══██╗██║░░░██║██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░",
        "██║░░██║╚██╗░██╔╝██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░",
        "██║░░██║░╚████╔╝░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░",
        "██████╔╝░░╚██╔╝░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗",
        "╚═════╝░░░░╚═╝░░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝"
    ]
    for i, line in enumerate(banner_text):
        print(RAINBOW[i % len(RAINBOW)] + line)
    print(Fore.YELLOW + "\n[👑] TOOL REG MAIL.TM | DGVIKAKA")
    print("[📞] SDT: 0785308626 | Admin: Duong Vi")
    print(Fore.WHITE + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def typing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading(msg="Đang xử lý"):
    anim = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(10):
        for a in anim:
            sys.stdout.write(f"\r{Fore.YELLOW}{a} {msg}...{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 30 + "\r")

def get_best_domain():
    try:
        r = requests.get("https://api.mail.tm/domains", timeout=10)
        data = r.json()["hydra:member"]
        good = [d["domain"] for d in data if "@" not in d["domain"] and "." in d["domain"]]
        return good[0] if good else "mail.tm"
    except:
        return "mail.tm"

def create_account(domain, index, delay):
    email = f"DGVIKAKA{random.randint(1000,9999)}@{domain}"
    password = f"DGVIKAKA{random.randint(1000,9999)}"
    payload = {"address": email, "password": password}
    try:
        r = requests.post("https://api.mail.tm/accounts", json=payload, timeout=10)
        if r.status_code == 201:
            print(Fore.GREEN + f"✔ [{index}] {email} | {password}")
            return f"{email}|{password}"
        else:
            print(Fore.RED + f"✗ [{index}] Tạo thất bại. Đang thử lại...")
            return None
    except:
        print(Fore.RED + f"✗ [{index}] Lỗi kết nối.")
        return None
    finally:
        time.sleep(delay)

def save_to_file(data, filename):
    try:
        path = "/storage/emulated/0/Download/" + filename
        with open(path, "a") as f:
            for line in data:
                f.write(line + "\n")
        print(Fore.CYAN + f"\n[✓] Đã lưu vào: {path}")
    except Exception as e:
        print(Fore.RED + f"[✗] Lỗi lưu file: {e}")

def main():
    banner()
    try:
        total = int(input(Fore.YELLOW + "🔥 Bạn muốn tạo bao nhiêu mail? (ví dụ: 5): "))
        delay = float(input(Fore.CYAN + "⏱️ Nhập delay giữa mỗi lần tạo (giây, nên >2): "))
        filename = input(Fore.GREEN + "💾 Nhập tên file lưu (mặc định: regmail.txt): ") or "regmail.txt"
    except:
        print(Fore.RED + "✗ Lỗi nhập. Thoát.")
        return

    print(Fore.MAGENTA + "\n🌐 Đang lấy domain tốt nhất từ mail.tm...")
    domain = get_best_domain()
    print(Fore.GREEN + f"→ Sử dụng domain: {domain}\n")

    result = []
    for i in range(1, total + 1):
        acc = create_account(domain, i, delay)
        if acc: result.append(acc)

    if result:
        save_to_file(result, filename)
    else:
        print(Fore.RED + "✗ Không tạo được mail nào.")

if __name__ == "__main__":
    main()