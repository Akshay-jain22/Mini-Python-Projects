import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)

data = "Hello, Myself Akshay Jain."

qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill='black', back_color='white')
image.save('images/qr.png')