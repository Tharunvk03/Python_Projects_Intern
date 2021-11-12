#Mail Automation

import smtplib #secure mail transfer protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = "mailid@gmail.com"
email_send = "mailid@gmail.com"

subject = "Hello"

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = "Hello!Hope your work is going well."
msg.attach(MIMEText(body,'plain'))


text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

#Next, log in to the server
server.login("emailid@gmail.com", "password")
#Send the mail

server.sendmail(email_user, email_send, text) 
server.quit()
