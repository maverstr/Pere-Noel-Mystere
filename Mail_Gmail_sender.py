# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:20:52 2018

@author: Maxime
"""

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
fromaddr = "v.maxime@gmail.com"
toaddr = "v.maxime@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Email Subject"
 
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "xxxx") #mail password
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()