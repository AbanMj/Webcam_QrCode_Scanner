import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size= 20,
    border=5
)
data= 'Traze Me'
data = 'Full Name: Kaleng Gardoce' '\nBirthday: June 30, 2002' '\nAddress: Pinagsabangan, Naujan' '\nContact Number: 09678956789'
qr.add_data(data)
qr.make(fit=True)
img= qr.make_image(fill='black', back_color='white')
img.save('Traze6.png')