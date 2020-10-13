#For this you need to have a file emails.csv which has all the emails you want to send to.

import smtplib
import csv

def sendmail(toemail):
    fromemail = ''
    password = ''

    print(toemail)
    subject = "testSubject"
    message = "testMessage"
    message = 'Subject: {}\n\n{}'.format(subject, message)
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        print('1')
        server.ehlo()
        server.starttls()
        print("2")

        server.login(fromemail, password)
        print("3")

        server.sendmail(fromemail, toemail, message)
        print("email sent successfully")
        server.quit()
    except:
        print("email sending failed successfully")

def getrecipientsfromcsv():
    lst =[]
    with open('emails.csv') as email:
        csvfile = csv.reader(email)
        for row in csvfile:
            if len(row):
                lst.append(row[1])
    return lst

lst = getrecipientsfromcsv()
print(lst)
sendmail(lst)