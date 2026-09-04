import random
import socketserver 
import socket, os
import string

'''
                    Client kết nối
                          │
                          ▼
                 Sinh khóa ngẫu nhiên 5 ký tự
                          │
                          ▼
          Flag giả: THM{thisisafakeflag}
                          │
                          ▼
               XOR với khóa ngẫu nhiên
                          │
                          ▼
                  Chuyển sang chuỗi hex
                          │
                          ▼
      Gửi ciphertext cho client qua TCP
                          │
                          ▼
            Hỏi: "What is the encryption key?"
                          │
                Client nhập khóa
                          │
                          ▼
               Có đúng với khóa đã sinh?
                  │                  │
                Đúng               Sai
                  │                  │
                  ▼                  ▼
   Gửi flag thật từ flag.txt   "Close but no cigar"
                  │
                  ▼
              Đóng kết nối
'''

#Mở file flag.txt để đọc flag thật
flag = open('flag.txt','r').read().strip()

#Gửi dữ liệu qua socket
def send_message(server, message):
    enc = message.encode()
    server.send(enc)

#Thiết lập
def setup(server, key):
    flag = 'THM{thisisafakeflag}' #flag giả
    xored = ""

    for i in range(0,len(flag)):
    	#Lấy mã ASCII của cờ và xor với key
        xored += chr(ord(flag[i]) ^ ord(key[i%len(key)]))

    #Đổi sang mã hex
    hex_encoded = xored.encode().hex()
    return hex_encoded

def start(server):
    #Tạo khóa random
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    key = stchủr(res)
    #encrypted khóa(giả) và gửi 
    hex_encoded = setup(server, key)
    send_message(server, "This XOR encoded text has flag 1: " + hex_encoded + "\n")
    #Nhận khóa
    send_message(server,"What is the encryption key? ")
    key_answer = server.recv(4096).decode().strip()

    try:
    	#Kiểm tra khóa
        if key_answer == key:
            send_message(server, "Congrats! That is the correct key! Here is flag 2: " + flag + "\n")
            server.close()
        else:
            send_message(server, 'Close but no cigar' + "\n")
            server.close()
    except:
        send_message(server, "Something went wrong. Please try again. :)\n")
        server.close()

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        start(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 1337), RequestHandler)#Lắng nghe mọi kết nối cổng 1337
    server.serve_forever()
