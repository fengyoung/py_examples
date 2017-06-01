#! /usr/bin/python

import sys
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib

reload(sys)
sys.setdefaultencoding('utf8')


def send_content(content, from_addr, passwd, to_addr, subject = None):
	"""Send content by email

	Args:
		conttent: A string. The content would be sent.
		from_addr: A string. The source email address.
		passwd: A string. The password of the source address.
		to_addr: A string. The destination email addrees.
		subject: A string. The title content of the email

	Returns:
		If send successfully return True, otherwise return False
	"""
	try:
		msg = MIMEText(content)
		msg['from'] = from_addr 
		msg['to'] = to_addr
		if subject:
			msg['subject'] = "[%s] %s" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), subject)
		else:
			msg['subject'] = "[%s]" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

		server = smtplib.SMTP()
		server.connect('smtp.sina.com')
		server.starttls()
		server.login(user = from_addr, password = passwd)
		server.sendmail(msg['from'], msg['to'], msg.as_string())
		server.quit()
	
		print 'email sent successfully!'
		return True
	
	except Exception as e:
		print str(e)
		return False



if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("usage: %s <from_addr> <password> <to_addr>" % sys.argv[0])
		exit(-1)

	subject = "Testing Mail"
	content = "This is a mail for testing SMTP & MIME in python, please don't reply."
	send_content(content, sys.argv[1], sys.argv[2], sys.argv[3], subject)
	exit(0)


