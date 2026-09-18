#
#simple MAil Automation
#SMTP ---> SIMPLE MAIL TRANSFER PROTOCOL 

'''
import smtplib
#First lets makes server connecctions #prot address and host
server = smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#Start the connections
server.starttls()
#login
server.login("mmsai3127@gmail.com","wikn cjoe hkbn hkqp")
msg = "Hello guys,hope you are doing well and improving daily"
server.sendmail("mmsai3127@gmail.com","sanjay43650@gmail.com",msg)

#Closing the connections
server.quit()
print("Mail Sent")
'''

#Now let's send the OTP to mail and validate the script
'''

import math
import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("mmsai3127@gmail.com","wikn cjoe hkbn hkqp")
otp = random.randint(100000,999999)
msg = f"Hello Man, This is your OTP: {otp}"
server.sendmail("mmsai3127@gmail.com","dineshdinu3026@gmail.com",msg)

#Closing the connections
server.quit()
print("Mail Sent")
'''
import math
import random
import smtplib

digits = '123456789'
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random()*10)]
    #print(OTP)
msg = f'YOUR OTP IS {OTP}'
server = smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#Start the connections
server.starttls()
#login
server.login("mmsai3127@gmail.com","wikn cjoe hkbn hkqp")
msg = "Hello guys,hope you are doing well and improving daily"
server.sendmail("mmsai3127@gmail.com","dineshdinu3026@gmail.com",msg)

a = input("Enter the OTP Received")
if a == OTP:
    print("Access Granted")
else:
    print("Timed Out")
#close the connections
server.quit()
print("Mail Sent")

