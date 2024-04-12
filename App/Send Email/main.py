import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email = "tobi21203@gmail.com"
password = "02122003TcH"

msg = MIMEMultipart()
msg['From'] = my_email
msg['To'] = "thau1298@gmail.com"
msg['Subject'] = "Subject of the Mail"
body = "Hello"
msg.attach(MIMEText(body, 'plain'))

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

text = msg.as_string()
connection.sendmail(from_addr=my_email, to_addrs="thau1298@gmail.com", msg=text)
connection.quit()