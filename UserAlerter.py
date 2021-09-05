from flask import Flask
from flask_ngrok import run_with_ngrok # enables Flask application to be hosted on non localhost URLs, so webhooks can be enabled #CHECKME (for development only)
from flask import request

def config():
	app = Flask(__name__)
	run_with_ngrok(app)  # Start ngrok when app is run #CHECKME (for development only)
	return app

def main():
	print("test")
	app.run()
	
app = config()

@app.route("/", methods=["GET", "POST"])
def hello_world():
	print("\nTESTING\n\n", request.get_json())
	response="Success"
	return (response, 200)

@app.route("/feed", methods=['GET', 'POST'])
def feed():
    challenge = request.args.get('hub.challenge')

    if challenge:
        return challenge

    print(request.data) # binary literal with xml payload

    return ('', 204)


if __name__ =="__main__":
	main()



# TODO:
# Set up email veification (verify your email through the link)
# Save emails in database for verification token, timer, and subscribe=on/off
# You need a email - video table (many to many)
# Video table db
# Send notifications to users
# Messenger, Whatsapp, Phone # are next steps
# Flask app.config/env variables can be used (or a config.json file) for local variables
# allow users to subscribe/unsubscribe to email notifications directly if they are logged in, or 
# through a secure email confirmation link which expires, if they are not
# allow users to make an account

