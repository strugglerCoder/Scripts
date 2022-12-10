# import package
import pyqrcode

#methods
from pyqrcode import QRCode

link = "https://www.linkedin.com/in/ajinkya-hole/"

qrCode = pyqrcode.create(link)

qrCode.svg("linkedInQRCode.svg", scale=10, module_color="red")



