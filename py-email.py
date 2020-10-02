#For this, you should have a Gmail account and Python installed on your machine. You will also need to install the `smtplib` package.
#You can install smtplib using pip install
#Also, for this script to work, you should enable "less secure apps" to access your gmail account, you can do this in your google accounts settings.

import smtplib

def send_email(email_address, password, subject, msg, to_email):
    try: 
        server = smtplib.SMTP('smtp.gmail.com:587')

        #general protocol for starting a connection
        server.ehlo()
        server.starttls()

        # Login to your gmail account. 
        server.login(email_address, password)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(email_address, to_email, message)   #first email is of senders, second is of receivers
        server.quit()
        print("Email sent successfully")
    except:
        print("Email sending unsuccessfull")  


email_id = ""              # your emailid
password = ""              # password
subject  = ""
message  = ""
to_email = ""              # receivers email address.

send_email(email_id, password, subject, message, to_email)