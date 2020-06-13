import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


fromaddr = input("enter your email address")
toaddr = []
password=input("enter password")

n = int(input("Enter the number of emails you want to message : "))

print("\n")

for i in range(0, n):
    print("Enter email number",i, ":")
    item = input()
    toaddr.append(item)
print("Emails are", toaddr)

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['Subject'] = input("enter the subject")


body = input("enter you message")
for i in toaddr:
    msg['To'] = i

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr,password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
