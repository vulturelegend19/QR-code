import qrcode

features = qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data('https://www.youtube.com/c/GeeksforGeeksVideos')
features.make(fit=True)
generate_image = qrcode.make("GeeksforGeeks")
generate_image.save('image1.png'
)
