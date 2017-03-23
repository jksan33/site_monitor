import requests
from bs4 import BeautifulSoup
import time
import smtplib

while True:
	uri = raw_input("Enter the URI of the website you wish to monitor: ")
	email = raw_input("Enter the email address where you wish to be notified when there is a change: ")
	headers = {'User-Agent': 'Chrome/56.0.2924.87'}
	response = requests.get(url, headers=headers)
	response.cookies['example_cookie_name']
	soup = BeautifulSoup(response.text, "lxml")
	
	url = raw_input("Enter the URI of the website you wish to monitor; ")
	cookies = dict(cookies_are='working')
	response = request.get(url, cookies=cookies)
	response.text

	if str(soup).find("Reddit") == -1:
		time.sleep(60)
		continue
	else:
		msg = 'WEBSITE UPDATED!'
		fromaddr = 'justthings4schcool@gmail.com'
		toaddr  = ['thanhtrinh12122010@gmail.com','davidtrieu6@gmail.com', 'gameguy47@gmail.com', 'francis.c.phan@gmail.com']

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
