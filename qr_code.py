import qrcode
from PIL import Image
# Get input from the user
data = input("Enter the value for the QR code: ")

image_name = input("Enter the image name (without extension): ")

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr.add_data(data)
qr.make(fit=True)
# Save the image
qr_image = qr.make_image(fill_color="midnightblue", back_color="white")
image_path = f"{image_name}.png"
qr_image.save(image_path)
print(f"QR code saved as {image_path}")