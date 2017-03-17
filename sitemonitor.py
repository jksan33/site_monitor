import requests
from bs4 import BeautifulSoup
import time
import smtplib

while True:
	uri = raw_input('Please enter the URI of the site you wish to monitor: ")
	email = raw_input("Please enter your email address to be notified when the site changes: ")
	headers = {'User-Agent': 'Chrome/56.0.2924.87'}
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.text, "lxml")
#      Change the "Reddit" value, I'll leave that for someone else ;)
	if str(soup).find("Reddit") == -1:
		time.sleep(60)
		continue
	else:
		msg = 'REDDIT UPDATED!'
		fromaddr = 'justthings4schcool@gmail.com'
		toaddr  = [email]

		server = smtplib.SMTP("smtp.gmail.com:587")
		server.starttls()
		server.login("justthings4schcool@gmail", "M1lk3yway")

		# Print the email's contents
		print('From: ' + fromaddr)
		print('To: ' + str(toaddrs))
		print('Message: ' + msg)
		server.sendmail(fromaddr, toaddrs, msg)
		server.quit()

		break
