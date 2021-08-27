# Import smtplib for the actual sending function
import smtplib

import ssl

# Here are the email package modules we"ll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def createEmail():
	# Create the container (outer) email message.
	message = MIMEMultipart("hello\nthis is a test email\n")
	print("\n\n", message)
	message["Subject"] = "Hi Urmi"
	# me == the sender"s email address
	# family = the list of all recipients" email addresses
	message["From"] = "testinguseralerterapp@gmail.com" # message["From"] contains the sender's email address
	recipient_list = ["intentionallycommittingfakeemails@gmail.com", "tohidetestingemails@gmail.com"]
	message["To"] = ", ".join(recipient_list) # message["To"] contains the recipient (one or many)'s email addresses, in a comma separated list
	message.preamble = "Test 2"

	return message

def sendEmail(message, server):
	# Send the email via our own SMTP server.
	# server = smtplib.SMTP('localhost') # localhost smtpm
	server.set_debuglevel(1)
	server.sendmail("testinguseralerterapp@gmail.com", ["the.shardul.shah@gmail.com", "shardul@ualberta.ca", "urmishah04@yahoo.com"], message.as_string())
	server.quit()

def createSSLContext(port, password):
	# Create a secure SSL context
	context = ssl.create_default_context()

	# TODO change to using with instead of doing it like this

	#with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	#	server.login("my@gmail.com", password)

	server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
	server.set_debuglevel(1)
	return server

def main():
	port = 465 # SSL port
	password = input("Type your password and press enter: ") # change after to using getenv variable, input, a .txt file, database or a .config file
	server = createSSLContext(port, password)
	server.login("testinguseralerterapp@gmail.com", password)
	message = createEmail()
	print(message)
	sendEmail(message, server)
	
	#useralerterapp1!
	print("test")


if __name__ == "__main__":
	main()