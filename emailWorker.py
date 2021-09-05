# Import smtplib for the actual sending function
import smtplib

import ssl

# Here are the email package modules we"ll need

# from email.mime.image import MIMEImage # not needed for now
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os

from dotenv import load_dotenv

def createEmail(emailAddress, recipientEmailAddress):
	# Create the container (outer) email message.

	# By default the type is set to mixed
	message = MIMEMultipart()
	print("\n\n", message)
	message["Subject"] = "Hi"
	# me == the sender"s email address
	# family = the list of all recipients" email addresses
	message["From"] = "User Alerter <" + emailAddress + ">" # message["From"] contains the sender's email address
	recipient_list = [recipientEmailAddress]
	message["To"] = ", ".join(recipient_list) # message["To"] contains the recipient (one or many)'s email addresses, in a comma separated list
	# If a Reply-To is explicitly provided then the email client will
	# use this address when the user hit the reply button
	message["Reply-To"] = "User Alerter <" + emailAddress + ">"
	message.preamble = "Hi"

	textual_message = MIMEMultipart('alternative')

	# plaintext part of the message
	plaintext_part = MIMEText("Hello this is a test message\n testing the app", "plain")
	textual_message.attach(plaintext_part)

	# HTML part of the message
	html_part = MIMEText("<h1>Hello this is a test message</h1><br><p style='color:red'>This is the first test message for this app! Congrats for seeing it\
	!</p>", "html")
	textual_message.attach(html_part)

	message.attach(textual_message)
	return message

def sendEmail(emailAddress, recipientEmailAddress, message, server):
	# Send the email via our own SMTP server.
	# server = smtplib.SMTP('localhost') # localhost smtpm
	server.set_debuglevel(1)
	# 2nd parameter in sendmail below is a list of all email addresses the email is to be sent to
	server.sendmail(emailAddress, [recipientEmailAddress], message.as_string())
	server.quit()

def createSSLContext(port):
	# Create a secure SSL context
	context = ssl.create_default_context()

	# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	# server.login("my@gmail.com", password)

	server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
	# server.set_debuglevel(1)
	return server

def main():
	# load .env variables from local .env file (using .env and dotenv to not expose credentials and other key information)
	load_dotenv()

	# get .env variables from local .env file
	port = os.getenv("PORT") # SSL port
	emailAddress = str(os.getenv("EMAIL")) # str may not be needed
	password = str(os.getenv("PASSWORD")) # str may not be needed
	recipientEmailAddress = str(os.getenv("TEST_RECIPIENT_EMAIL")) # str may not be needed 

	server = createSSLContext(port)
	server.login(emailAddress, password) # FIXME use emailAddress in other functions, modularize emailWorker with ease

	# try catch for failed email addresses and other catch scenarios
	
	message = createEmail(emailAddress, recipientEmailAddress)
	#print(message)

	sendEmail(emailAddress, recipientEmailAddress, message, server)


if __name__ == "__main__":
	main()