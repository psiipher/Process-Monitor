import sys
import urllib.request
import urllib.error
import smtplib
import getpass

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def check_connection():
    try:
        urllib.request.urlopen("https://www.google.com/", timeout=1)
        return True
    except urllib.error.URLError as error:
        return False


def get_credentials():
    try:
        from_id = input("\nEnter sender's email-id:\t")
        to_id = input("\nEnter receiver's email-id:\t")
        print("\n")
        password = getpass.getpass()
        return from_id, to_id, password
    except Exception as E:
        print("\nUnsuccessful\n", E)
        sys.exit()


def send_mail(filename, _time,from_id, to_id, password):
    try:
        msg = MIMEMultipart()

        msg['From'] = from_id
        msg['To'] = to_id

        body = f"Hello {from_id}, Here is a log of running process. It was created at {_time}"
        subject = f"Process log generated at: {_time}"

        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, 'rb')

        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment;filename= %s" % filename)
        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(from_id, password)

        text = msg.as_string()
        s.sendmail(from_id, to_id, text)
        s.quit()

        print("\nLog file sent successfully\n")

    except Exception as E:
        print("\nUnsuccessful\n", E)
        sys.exit()
