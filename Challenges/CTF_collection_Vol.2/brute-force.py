import requests 
import string
from bs4 import BeautifulSoup

url = 'http://10.48.144.51/game1/'
hash_final = '51 89 77 93 126 14 93 10'
chars = list(string.printable)
list_hash = {}

def getHash(response):
    soup = BeautifulSoup(response.text, "html.parser")
    p = soup.find("p", string= lambda x : x and "Your hash:" in x)
    your_hash = p.get_text().split(":", 1)[1].strip()
    return your_hash

def create_list_hash():
    for i in range(len(chars)):
        data = { 'answer': {chars[i]} }
        res = requests.post(url, data= data)
        hs = getHash(res)
        list_hash[hs] = chars[i]

print("[+] Chuong trinh tim plain text tuong ung hash!")
print(f"[+] Du lieu co the hien thi: {chars}")
print("[+] Xay dung bang cau vong!")
create_list_hash()
print(f"[+] Bang cau vong: {list_hash}")
print("[+] Tao plain text")

plain = ""
list_str = hash_final.split(" ")
for i in list_str:
    c = list_hash[i]
    plain = plain + c

print(f"[+] Plain text: {plain}")