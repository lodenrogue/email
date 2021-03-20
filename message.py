import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import configparser
import sys
import os

class Email():

    def __init__(self):
        self._config = None
        another line


    def send(self, recipient, subject, body):
        smtp_message = self._create_smtp_message(recipient, subject, body)
        self._send_email(recipient, smtp_message)


    def _create_smtp_message(self, recipient, subject, message):
        smtp_message = MIMEMultipart('alternative')
        smtp_message['Subject'] = subject
        smtp_message['From'] = self._get_sender() 

        part1 = MIMEText('You need an email that can render html', 'plain')
        part2 = MIMEText(message, 'html')

        smtp_message.attach(part1)
        smtp_message.attach(part2)
        return smtp_message


    def _send_email(self, recipient, smtp_message):
        sender = self._get_sender()
        password = self._get_password()
        smtp_url = self._get_smtp_url()
        smtp_port = self._get_smtp_port()

        try:
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(smtp_url, smtp_port, context=context) as server:
                server.login(sender, password)
                server.sendmail(sender, recipient, smtp_message.as_string())
        
        except Exception as e:
            print(e)


    def _get_sender(self):
        return self._get_config()['email']
    

    def _get_password(self):
        return self._get_config()['password']
    
    
    def _get_smtp_url(self):
        return self._get_config()['smtpSSL'].split(':')[0]


    def _get_smtp_port(self):
        return int(self._get_config()['smtpSSL'].split(':')[1])


    def _get_config(self):
        if self._config is None:
            self._config = self._read_config()

        return self._config


    def _read_config(self):
        path = os.path.expanduser('~')
        config = {}

        with open('{}/.email/email.conf'.format(path)) as f:
            for line in f.readlines():
                key = line.split('=')[0]
                value = line.split('=')[1]  
                config[key] = value

        return config


def get_message(path):
    with open(path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    recipient = sys.argv[1]
    subject = sys.argv[2]
    message = get_message(sys.argv[3])
    Email().send(recipient, subject, message)
