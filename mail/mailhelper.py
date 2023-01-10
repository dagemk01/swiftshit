import sendgrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
from environs import Env

env = Env()
env.read_env()


def mail_helper(reciever, sub, infosent):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("dagemk1@umbc.edu")
    to_email = To(reciever)
    subject = sub
    content = Content("text/plain", infosent)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


def mailer (reciever, sub, infosent):
    message = Mail(
    from_email='dagemk1@umbc.edu',
    to_emails= reciever,
    subject=sub,
    html_content=infosent)
    try:
        sg = SendGridAPIClient(env.str("SENDGRID_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
        print("ERROR: PC LOAD LETTER")