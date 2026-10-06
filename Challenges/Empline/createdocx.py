#!/usr/bin/env python 
from docx import Document

print("[+] Chuong trinh tao file docx don gian!")
document = Document()
p = document.add_paragraph("10h37")
document.save("payload.docx")
print("[+] Tao file payload.docx thanh cong!")