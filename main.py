import qrcode

upi_id = input("Enter your name ")

paytm_url =f"upi://pay?pa={upi_id}&pn=Recipient%20name&am=amount&tn=thank youthank you  "
google_url = f"upi://pay?pa={upi_id}&pn=Recipient%20name&am=amount&tn=thank you"
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20name&am=amount&tn=thank you"

# create a QR code 

paytm_qr = qrcode.make(paytm_url)
google_qr = qrcode.make(google_url)
phonepe_qr = qrcode.make(phonepe_url)

# save the pic 

phonepe_qr.save('phonepe_qr.png')
google_qr.save('google_qr.png')
paytm_qr.save('paytm.png')

# Display the qr code 

phonepe_qr.show()
google_qr.show()
paytm_qr.show()