import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_password_reset_email(account_email: str, reset_token: str):
    try: 
      message = Mail(
        from_email='mail@em6767.kalygo.io',
        to_emails='ceemmmdee@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>'
      )
      sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
    except Exception as e:
      print(e.message)