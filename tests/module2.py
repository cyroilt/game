
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()


message = "Thank you"

# setup the parameters of the message
password = '76EevtR4Mcmbxm10bmja'
msg['From'] = 'alittlequbit@mail.ru'
msg['To'] = 'cyroil31@gmail.com'
msg['Subject'] = "Subscription"

# add in the message body
msg.attach(MIMEText(message, 'plain'))
print('runs')
#create server
server = smtplib.SMTP('smtp.mail.ru:465')
server.starttls()
print('started')
# Login Credentials for sending the mail
server.login(msg['From'], password)
print('loged in')

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
print('sent')
server.quit()
