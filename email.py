# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Test'
msg['From'] = "me"
msg['To'] = "bn.chn2@gmail.com"

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
