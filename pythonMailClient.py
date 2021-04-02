import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('mail.testing.is.fun@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'mail.testing.is.fun'
msg['To'] = 'jonathanjgodinez@gmail.com'
msg['Subject'] = 'Just a Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'goldrushmaidsgirl.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('mail.testing.is.fun@gmail.com', 'jonathanjgodinez@gmail.com', text)