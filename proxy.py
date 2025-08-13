# -*- coding: utf-8 -*-
# Elite Proxy Scraper MAX - Tool Get Proxy VIP 👑
# Admin: Duong Vi | SDT: 0785308626 | TOOL GỘP DGVIKAKA

import requests
import threading
from queue import Queue
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.progress import Progress, BarColumn, SpinnerColumn, TextColumn, TimeElapsedColumn
import os
import time

console = Console()
live_proxies = []
all_proxies = []

sources = [
    "https://www.sslproxies.org/",
    "https://free-proxy-list.net/",
    "https://www.us-proxy.org/",
    "https://www.proxy-list.download/HTTP",
    "https://www.hide-my-ip.com/proxylist.shtml",
    "https://proxyscrape.com/free-proxy-list",
    "https://openproxy.space/list/http",
    "https://www.freeproxylists.net/",
    "https://www.proxynova.com/proxy-server-list/",
    "https://www.proxy-daily.com/",
    "https://spys.one/en/free-proxy-list/",
    "https://www.my-proxy.com/free-proxy-list.html",
    "https://proxy11.com/free-proxy/",
    "https://www.freeproxy.world/",
    "https://www.live-proxy.net/",
    "https://www.proxy-listen.de/Proxy/Proxyliste.html",
    "https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc",
    "https://www.cool-proxy.net/proxies.json",
    "https://www.proxyscan.io/api/proxy?format=json&limit=100",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
    "https://www.proxydocker.com/en/proxylist/api?format=txt",
    "https://proxylist.me/api/proxies?type=http&limit=50",
    "https://www.freeproxychecker.com/api/proxy/list?page=1&limit=100",
    "https://proxyhub.me/en/all-active-free-proxy-list.html",
    "https://www.proxypedia.org/",
    "https://www.proxyrack.com/free-proxies/",
    "https://www.idcloak.com/proxylist/free-proxy-list.html",
    "https://www.proxylists.net/http.txt",
    "https://www.proxy4free.com/en/proxy-list/",
    "https://www.freshproxylist.org/",
    "https://www.proxyserverlist24.top/",
    "https://proxylist.live/free-proxy-list/",
    "https://www.blackhatworld.com/seo/proxy-list.1128439/",
    "https://www.freeproxylist.cc/",
    "https://www.hidemy.name/en/proxy-list/",
    "https://www.proxy-list.org/english/index.php",
    "https://www.proxylistpro.com/free-proxies/",
    "https://www.luxproxy.com/free-proxy-list/",
    "https://www.multiproxy.org/txt_all/proxy.txt",
    "https://www.samair.ru/proxy/proxy-01.htm",
    "https://www.proxz.com/proxy_list_high_anonymous_0.html",
    "https://www.proxyelite.info/en/free-proxy-list/",
    "https://www.httptunnel.ge/ProxyListForFree.aspx",
    "https://www.getproxy.io/free-proxies/",
    "https://www.proxyranker.com/free-proxy-list/",
    "https://www.proxyway.com/free-proxy-list/"
]

def banner():
    os.system("clear")
    print("""\033[1;31m██████╗░██╗░░░██╗██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;34m██╔══██╗██║░░░██║██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;33m██║░░██║╚██╗░██╔╝██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;32m██║░░██║░╚████╔╝░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;35m██████╔╝░░╚██╔╝░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;36m╚═════╝░░░░╚═╝░░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝

\033[1;33m[👑] TOOL TÌM GET PROXY VIP
[•] TOOL GỘP DGVIKAKA
[•] SDT: 0785308626
[•] ADMIN: Duong Vi
\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

def fetch_source(url):
    proxies = []
    try:
        r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if "raw.githubusercontent" in url or ".txt" in url or "api" in url:
            for line in r.text.splitlines():
                if ":" in line and "." in line:
                    proxies.append(line.strip())
        else:
            soup = BeautifulSoup(r.text, "html.parser")
            table = soup.find("table")
            if table:
                for row in table.find_all("tr")[1:]:
                    cols = row.find_all("td")
                    if len(cols) >= 2:
                        ip = cols[0].text.strip()
                        port = cols[1].text.strip()
                        proxies.append(f"{ip}:{port}")
    except:
        pass
    return proxies

def check(proxy, queue):
    try:
        start = time.time()
        requests.get("https://www.google.com", proxies={
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }, timeout=5)
        elapsed = time.time() - start
        queue.put((proxy, True, elapsed))
    except:
        queue.put((proxy, False, None))

def collect_and_check(target=100):
    banner()
    console.print(f"[cyan]🌀 Đang thu thập {target} proxy từ {len(sources)} nguồn...[/cyan]")
    global all_proxies, live_proxies
    all_proxies.clear()
    live_proxies.clear()
    for src in sources:
        all_proxies += fetch_source(src)
        if len(all_proxies) >= target:
            break
    all_proxies = list(set(all_proxies))[:target]

    console.print(f"[green]✓ Đã thu thập {len(all_proxies)} proxy. Đang kiểm tra...[/green]")

    q = Queue()
    threads = []
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), TimeElapsedColumn()) as progress:
        task = progress.add_task("[yellow]Kiểm tra proxy sống...", total=len(all_proxies))
        for proxy in all_proxies:
            t = threading.Thread(target=check, args=(proxy, q))
            threads.append(t)
            t.start()

        for _ in range(len(all_proxies)):
            proxy, status, elapsed = q.get()
            if status:
                live_proxies.append((proxy, elapsed))
            progress.advance(task)

    console.print(f"[bold green]✓ Hoàn tất! {len(live_proxies)} proxy sống.[/bold green]")

def show_live():
    banner()
    if not live_proxies:
        console.print("[red]Chưa có proxy sống![/red]")
        return
    table = Table(title="Danh sách Proxy Sống (sắp xếp theo tốc độ)", header_style="bold cyan", box=None)
    table.add_column("STT", style="green", justify="center", width=5)
    table.add_column("Proxy", style="white")
    table.add_column("Ping", style="magenta", justify="center", width=10)
    
    sorted_live = sorted(live_proxies, key=lambda x: x[1])
    for i, (proxy, ping) in enumerate(sorted_live, 1):
        table.add_row(str(i), proxy, f"{ping:.2f}s")
    console.print(table)

def save_proxies():
    banner()
    if not live_proxies:
        console.print("[yellow]⚠ Không có proxy sống để lưu![/yellow]")
        return
    try:
        path = "/storage/emulated/0/Download/"
        os.makedirs(path, exist_ok=True)
        name = Prompt.ask("Nhập tên file", default="proxy_vip.txt")
        if not name.endswith(".txt"):
            name += ".txt"
        full_path = os.path.join(path, name)
        with open(full_path, "w") as f:
            for p, _ in live_proxies:
                f.write(p + "\n")
        console.print(f"[green]✓ Đã lưu {len(live_proxies)} proxy vào: {full_path}[/green]")
    except Exception as e:
        console.print(f"[red]✗ Lỗi khi lưu file: {e}[/red]")

def menu():
    while True:
        banner()
        console.print("[cyan bold]1.[/cyan bold] Thu thập & kiểm tra proxy")
        console.print("[cyan bold]2.[/cyan bold] Xem proxy sống")
        console.print("[cyan bold]3.[/cyan bold] Lưu vào file")
        console.print("[cyan bold]4.[/cyan bold] Thoát")
        choice = Prompt.ask("[bold yellow]➤ Chọn chức năng[/bold yellow]", choices=["1", "2", "3", "4"])
        if choice == "1":
            qty = IntPrompt.ask("Nhập số lượng proxy cần", default=100)
            collect_and_check(qty)
            input("Nhấn Enter để quay lại menu...")
        elif choice == "2":
            show_live()
            input("Nhấn Enter để quay lại menu...")
        elif choice == "3":
            save_proxies()
            input("Nhấn Enter để quay lại menu...")
        else:
            break

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        console.print("\n[red]✗ Đã dừng bởi người dùng[/red]")