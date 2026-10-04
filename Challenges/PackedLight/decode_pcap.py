#!/usr/bin/env python3

import base64

from scapy.all import rdpcap
from scapy.layers.http import HTTPRequest

# File PCAP cần phân tích
PCAP_FILE = "traffic.pcapng"

# Khóa XOR được malware sử dụng
KEY = b"H0t3lSt@ff0NlyK3epS3cr3t!"


def xor(data: bytes, key: bytes) -> bytes:
    """
    Giải mã dữ liệu bằng XOR.
    """
    return bytes(
        b ^ key[i % len(key)]
        for i, b in enumerate(data)
    )


def decode_cookie(cookie_value: str) -> str:
    """
    Base64 Decode -> XOR -> UTF-8
    """
    try:
        encrypted = base64.b64decode(cookie_value)
        decrypted = xor(encrypted, KEY)

        print(f"[DEBUG] XOR Bytes: {decrypted}")

        return decrypted.decode("utf-8", errors="replace")

    except Exception:
        return ""


def extract_cookie(cookie_header: str):
    """
    Trích xuất giá trị hotel_sess_state từ Cookie.
    """
    for item in cookie_header.split(";"):
        item = item.strip()

        if item.startswith("hotel_sess_state="):
            return item.split("=", 1)[1]

    return None


def main():
    # Đọc toàn bộ packet trong file PCAP
    packets = rdpcap(PCAP_FILE)

    # Danh sách Cookie và ký tự đã giải mã
    recovered = []

    for pkt in packets:

        # Chỉ xử lý HTTP Request
        if not pkt.haslayer(HTTPRequest):
            continue

        http = pkt[HTTPRequest]

        # Chỉ xử lý các request có Cookie
        if "Cookie" not in http.fields:
            continue

        # Lấy header Cookie
        cookie_header = http.fields["Cookie"].decode(errors="ignore")

        # Trích xuất giá trị hotel_sess_state
        value = extract_cookie(cookie_header)

        print(f"[DEBUG] Encoded Cookie: {value}")

        if value is None:
            continue

        # Giải mã Cookie
        ch = decode_cookie(value)

        recovered.append(ch)

        print(f"[+] Cookie : {value}")
        print(f"    Decoded: {repr(ch)}")

    print("\n========== RECOVERED TEXT ==========\n")
    print("\nRecovered Keystrokes:")
    print("".join(recovered))


if __name__ == "__main__":
    main()
