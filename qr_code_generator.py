#Hands-on Assignment2
#AI QR Code Generator with Python
#Nischal Tiwari


import qrcode

#fixed destination url to generate qr code
biox_url = "https://www.bioxsystems.com"

#user prompt
input("Please enter a URL: ")

#QR code configuration
qr_conf = qrcode.QRCode(
    #Q for a clearer, readable qr code
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    
    #approximately according to the assignment
    box_size=16,
    border=4,
)

#adding configuration to the url to generate qr
qr_conf.add_data(biox_url)
qr_conf.make()

#Generating and saving the QR code image
generated_img = qr_conf.make_image(fill_color="black", back_color="white")
generated_img.save("nischal's_qr_code.png")
generated_img.show()#to open the generated image

#Confirmation message
print("* * *  QR Code generated  * * *")
