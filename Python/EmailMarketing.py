import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time

print("Welcome to Email Marketing")
# This can be read from a csv
emailList = ['rahulsh3105@gmail.com', 'arnav1672@gmail.com', 'care@codeswear.in']

def sendMail(fromEmail, toEmail, subject, message):
  msg = MIMEMultipart()
  msg.set_unixfrom("Rahul")
  msg['From'] = fromEmail
  msg['To'] = toEmail
  msg['Subject'] = subject
  msg.attach(MIMEText(message))
  mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
  mailserver.ehlo()
  mailserver.login(os.environ['email'], os.environ['password']) 
  
  mailserver.sendmail(fromEmail, toEmail, msg.as_string())
  mailserver.quit()
  
for email in emailList: 
  fromEmail = "care@codeswear.in"
  subject = "Unknown"
  message = "Yes"
  # sendMail(fromEmail, email, subject, message)
  print(f"Mail sent to - {email}")
  time.sleep(2)

print("All emails sent successfully")
