# UserAlerter 

<h2> Database Credentials </h2>

A file called .env.example exists in the main directory. Type the command `cat .env.example`. Copy paste the content of this file manually. Type the command `touch .env`. Then open <strong> ".env" </strong> in the text editor of your choice. Paste the <strong> .env.example </strong> content into this file. Replace the PORT, EMAIL, PASSWORD AND TEST_RECIPIENT_EMAIL as needed. This will be used to fill in needed informaton for the application.
<!--This will be used to configure a database when running the server (either locally or remotely) fill in needed information for our application. --> The following is the content of <strong> ".env.example" </strong>, for reference: 

<strong> ".env.example" </strong> file should have information of the SMTP port, email address for the sender email account, password of the sender email account and a recipient email address for testing purposes:

```
PORT=port

EMAIL=email_address

PASSWORD=email_password

TEST_RECIPIENT_EMAIL=recipient_email_address
```

That is, subsitute the values of each field accordingly. Note that "PORT" is most commonly set to 465 for SMTP.

The <strong> ".env" </strong> file cannot be stored on GitHub, because the credentials will be exposed on GitHub. 

<!--Note that the username and password you input must be the same as the root username and password of your LOCAL MySQL environment! This should be made uniform when hosted remotely. -->

### Full stack application to alert users of Youtube video uploads

### More to come

### Important note: ngrok dependency must be modified, and a custom pip install link must be used. Self-reminder to add more later.

