import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('shaunakbdn@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Shaunak Badani'
msg['To'] = 'shaunakb163@hotmail.com'
msg['Subject'] = 'Just A Test'

with open('msg.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'cheems.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('shaunakbdn@gmail.com', 'shaunakb163@hotmail.com', text)