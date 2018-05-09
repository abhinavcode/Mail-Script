from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from smtplib import SMTP
import sys
import os
import re


#Update EMAIL ID and PASWORD with yours
USERNAME = "EMAIL ID"
PASSWORD = "PASSWORD"

#update subject and content of email
subject="SUBJECT OF EMAIL"


content="""\
Dear <b>%s</b>,<br><br>
This is the body of email. Above a placeholder is used which will be filled after reading the file.
You have to write HTML to get things done. For example to write in new line use br tag like <br>
To get things bold. Use b tag like <br>
<b>This is bold</b><br>

<br><br>
Regards, <br>
Your name<br>
Post <br>
Organization<br>
"""


#GMAIL connect settings
conn = SMTP("smtp.gmail.com", 587)
conn.ehlo()
conn.starttls()
conn.login(USERNAME, PASSWORD)


#CODE TO READ DETAILS FROM CSV FILE NAMED abc.csv
f=open("abc.csv","r")

#File format 
#Name, Email

#Update USERNAME TO APPEAR IN MAIL and file to be attached(if any) else comment the code for file
for l in f:
	print l
	x=l.split(",")
	emailid=x[1]
	name=x[0]
	msg = MIMEMultipart()   	
	msg['Subject']= subject
	msg['From']   = "USERNAME TO APPEAR IN MAIL <%s>" %USERNAME
	msg['To']= emailid
	a=content %(name)
	msg.attach(MIMEText(a, 'HTML'))
	#To attach file (Note: upadte FILENAME and make sure to have it at same location as script or specify complete location)

	#if no file delete from next line	
	filename = "FILENAME.zip"
	attachment = open("FILENAME.zip", "rb")
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename) 	
	msg.attach(part)
	#if you dont have any file remove till here 	

   	conn.sendmail(USERNAME, (emailid), msg.as_string())
	print "mail sent to %s" %emailid 
