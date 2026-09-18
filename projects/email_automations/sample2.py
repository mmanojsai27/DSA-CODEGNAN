'''
In this case we need to add the subject and to address for mail

we will use email packages
knsknsk10@gmail.com

'''
#
'''
import email
import smtplib
#MIME ---> Multipurpose Interner Mail Extensions
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Now we will provide the details
From = "mmsai3127@gmail.com"
To = "dineshdinu3026@gmail.com"
Subject = "Python full Stack traning"
#Now we will check the all the details and throw it to Multipart
msg = MIMEMultipart()
#print(msg)
#print(type(msg))
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject
msg['body'] = "Hey Guys,What's the learning plan for this week"
msg.attach(MIMEText(msg['body'],'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("mmsai3127@gmail.com","wikn cjoe hkbn hkqp")
server.sendmail(From,To,text)
#Closing the connections
server.quit()
print("Mail Sent")
'''

#Now we are adding an attachment along with subject to send email

import smtplib
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase #Loading the attachment as header file
from email import encoders #encode the file into binary
#Now We can directly insert earlier subject mail code and add the attachment
From = "mmsai3127@gmail.com"
To = "dineshdinu3026@gmail.com"
Subject = "Python full Stack traning - Vizag"
body = "We have understood how to send automated emails using Python"
attach = "samplemail.py" #Make sure the file is in same loction
#Now we will add our subject related code
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject
msg.attach(MIMEText(body))
#Now we need to add attachment to our mail
part = MIMEBase('application','octetstream')
print(part)
part.set_payload(open(attach).read())
encoders.encode_base64(part)
#Lets add the headers to our filename
part.add_header('Content-Dispostition',
                f'attachment;filename={os.path.basename(attach)}')
msg.attach(part)
#Finally Converting this to string
text = msg.as_string()
#Include Your smtplib code
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("mmsai3127@gmail.com","wikn cjoe hkbn hkqp")
server.sendmail(From,To,text)
#Closing the connections
server.quit()
print("Mail Sent")
















