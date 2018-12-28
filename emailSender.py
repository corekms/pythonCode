# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

SMTP_MAIL_SERVER = 'smtp.gmail.com'
SMTP_ID='E-mail to send'
SMTP_PASSWORD='*********'
SMTP_MAIL_SERVER_PORT=465

SEND_TO = ['user email1', ''user email2']

def sendMail(subject_,contents_):
	message_ = MIMEText(contents_,_charset='utf-8')
	message_['Subject'] = subject_
	message_['From'] = SMTP_ID
	message_['To'] = ', '.join(SEND_TO)
	
	sm_ = smtplib.SMTP_SSL(SMTP_MAIL_SERVER, SMTP_MAIL_SERVER_PORT)
	sm_.ehlo()
	sm_.login(SMTP_ID, SMTP_PASSWORD)
	sm_.sendmail(SMTP_ID, SEND_TO, message_.as_string())
	sm_.quit()
	
if __name__ == "__main__":
	sendMail('메일제목','메일내용')

