import smtplib
import time


def gmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('kingking7173@gmail.com', 'King7173')
    subject = 'SMTP'
    body = 'I love you !!'
    message = 'Subject:{}\n\\n{}'.format(subject, body)

    server.sendmail('kingking7173@gmail.com', 'p200096@pwr.nu.edu.pk', message)

for i in range(50):
    gmail()
    time.sleep(50)