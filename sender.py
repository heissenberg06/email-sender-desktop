from email.message import EmailMessage
from passs import password
import ssl
import smtplib
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui = loadUiType('senderU.ui')

email_sender = 'berk579.32@gmail.com'
email_password = password

email_receiver = ''


subject = 'staj'
body = """

merhaba ben ibrahim yilmaz

"""

em = EmailMessage() #this is an instance of EmailMessage
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())