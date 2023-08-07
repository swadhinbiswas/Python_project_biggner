import qrcode as qc
from PIL import Image
qr=qc.QRCode(version=1,
             error_correction=qc.constants.ERROR_CORRECT_H,
             box_size=10,border=4,)
x=input()
your_name=input()
qr.add_data(x)
qr.make(fit=True)
img=qr.make_image(fill_color="pink",back_color='white')
img.save(f"{your_name}.png")