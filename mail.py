import smtplib
from email.message import EmailMessage
import imghdr

Sender_Email = "driverdrowsiness0@gmail.com"
Reciever_Email = "vikrantsakpal87@gmail.com"
Password ='oldyndhhvxublydz'
newMessage = EmailMessage()    #creating an object of EmailMessage class
newMessage['Subject'] = "Test Email from Diver Drowsiness" #Defining email subject
newMessage['From'] = Sender_Email  #Defining sender email
newMessage['To'] = Reciever_Email  #Defining reciever email


import requests 


newMessage.set_content('Hi,Yawn detected.Please help me urgently...') #Defining email body

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)
