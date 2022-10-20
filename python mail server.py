import smtplib
sender_mail = input("enter your sender mail : ")
password = input("enter your sender mail password : ")
message = input("enter your message")
receiver_mail = input("enter reciver's mail : ")

mail = smtplib.SMTP('smtp.gmail.com', '587')
mail.starttls()
mail.login( sender_mail , password)#you must enter the password

mail.sendmail( sender_mail, receiver_mail, message )

mail.quit()
print("mail sent successfully")