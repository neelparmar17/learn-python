import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email import encoders

emailfrom = "neel.parmar@trringo.com"
emailto = "parmarneel1718@gmail.com"
fileToSend = "automateDailyReport/New PF -9th Mar.xlsx"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "help I cannot send an attachment to save my life"
msg.preamble = "help I cannot send an attachment to save my life"

# fp = open(fileToSend, "rb")
# attachment = MIMEBase(maintype, subtype)
# attachment.set_payload(fp.read())
# fp.close()
# encoders.encode_base64(attachment)
# attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
# msg.attach(attachment)
part = MIMEBase('application', "octet-stream")
part.set_payload(open(fileToSend, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= %s' % (fileToSend))
msg.attach(part)


server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login("neel.parmar@trringo.com", "tatwchpxogusxvtc")
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()