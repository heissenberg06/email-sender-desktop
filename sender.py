from email.message import EmailMessage
import ssl
import smtplib
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys

ui, _ = loadUiType('senderDesktop.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Send_Email)

    def Login_Account(self):
        email_sender = self.lineEdit.text()
        email_password = self.lineEdit_2.text()
        subject = self.lineEdit_5.text()
        body = self.lineEdit_3.text()
        email_receiver = self.lineEdit_4.text()
        em = EmailMessage()  # this is an instance of EmailMessage
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    def Send_Email(self):
        self.Login_Account()

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
