import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "neel.parmar@trringo.com"
receiver = "PADAKI.RAVI@mahindra.com"

msg = MIMEMultipart("alternative")
msg["Subject"] = "test email from python"
msg["From"] = sender
msg["To"] = receiver

# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Test email from python <a href="https://docs.python.org/2/library/smtplib.html">smtplib</a>
    </p>
  </body>
</html>
"""
# part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# msg.attach(part1)
msg.attach(part2)
  
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("neel.parmar@trringo.com", "vfmfuunnmtdxxydm")
server.sendmail(sender, receiver,msg.as_string())
# s.sendmail(sender, receiver, msg.as_string())
# s.quit()