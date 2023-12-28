# Black and White

# import qrcode
# data = "https://youtu.be/FOGRHBp6lvM"
# img = qr.add_data(data)
# img.save("QR_generating_Video.png")

# Color QR

import qrcode
from PIL import Image

qr = qrcode.QRcode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)
qr.add_data("https://youtu.be/FOGRHBp6lvM")
qr.make(fit=True)
img=qr.make_image(fil_color="yellow", back_color="blue")
img.save("QR_generating.png")

