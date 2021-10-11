import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('kingking7173@gmail.com', 'King71--')
server.sendmail('kingking7173@gmail.com', 'dj835048@gmail.com', 'Hi! Iam king' )