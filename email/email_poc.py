import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "neel.parmar@trringo.com"
receiver = ["parmarneel1718@gmail.com" , "neel.parmar@mountblue.io" , "bohrneel@gmail.com"]

msg = MIMEMultipart("alternative")
msg["Subject"] = "test email from python"
msg["From"] = sender
msg["To"] = ", ".join(receiver)

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org with multiple receipants"
html = """\
    <html>
    <head>
    </head>
    <body>
    <p>Hello good morning!</p>
    </body>
    </html>
"""
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)
  
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.start()
server.login("neel.parmar@trringo.com", "tatwchpxogusxvtc")
server.sendmail(sender, receiver,msg.as_string())
# s.sendmail(sender, receiver, msg.as_string())
# s.quit()