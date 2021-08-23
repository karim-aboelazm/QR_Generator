import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "My Name is : Karim Mohammed Aboelazm\nMy Whatsapp is : 01210903962"

# function for create QR
def qr_creator(s):
    # Generate QR code
    url = pyqrcode.create(s)
    
    # Create and save the png file naming "myqr.png"
    url.svg("info.svg", scale=8)

if __name__ == '__main__':
    qr_creator(s)
 
