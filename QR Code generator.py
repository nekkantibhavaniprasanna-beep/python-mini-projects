import os
import qrcode
url=input("Enter the URL to generate QR code: ")
qr=qrcode.make(url)
filename="qrcode.png"
qr.save(filename)
print("saved at:", os.path.abspath(filename))