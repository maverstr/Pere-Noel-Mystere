# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:30:18 2018

@author: Maxime
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random as rd
import sys


participants = ["Gaëlle", "Maxime", "Chloé", "Nathan", "Déborah", "Lucas", "Sapho", "Thomas", "Pierre", "Romain", "Troc", "Alizée"]

emailAdresses = {
        "Gaëlle":"xxxxx@blabla.com",
        "Maxime":"xxxxx@blabla.com",
        "Chloé": "xxxxx@blabla.com",
        "Nathan": "xxxxx@blabla.com",
        "Déborah": "xxxxx@blabla.com",
        "Lucas": "xxxxx@blabla.com",
        "Sapho": "xxxxx@blabla.com",
        "Thomas": "xxxxx@blabla.com",
        "Pierre": "xxxxx@blabla.com",
        "Romain": "xxxxx@blabla.com",
        "Troc": "xxxxx@blabla.com",
        "Alizée": "xxxxx@blabla.com",
        }




def randomPick(participants):
    sendingToList = participants.copy()
    out = []
    for sender in participants:
        counter = 0
        while True:
            counter +=1
            mustSendTo=rd.choice(sendingToList)
            if mustSendTo != sender:
                sendingToList.remove(mustSendTo)
                break
            if counter > 5:
                print('erreur de tri')
                sys.exit()
        out.append([sender,mustSendTo])
    return out

def sendMail(fromAdd, toAdd, mailSubject, mailBody):
    fromaddr = fromAdd
    toaddr = toAdd
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = mailSubject
     
    body = mailBody
    msg.attach(MIMEText(body, 'plain'))
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "xxxxxxxxxxx") #mail password
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return


def sendMailTest(fromAdd, toAdd, mailSubject, mailBody):
    fromaddr = fromAdd
    toaddr = toAdd
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = mailSubject
     
    body = mailBody
    msg.attach(MIMEText(body, 'plain'))
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "xxxxxxxxxx") #mail password
    text = msg.as_string()
    print(text)
    server.quit()
    return


associations = randomPick(participants)
for elem in associations:
    sendingToEmail = emailAdresses[elem[0]]
    body = "Salut %s, second tirage la base ! C'EST CE TIRAGE CI QUI COMPTE DU COUP !! \n \n Pour le Père Noël Mystère de cette année, tu dois trouver un cadeau (budget max 15€) pour %s. \n Je laisse le messie Doodle décider de la date de remise des cadeaux ! \n \n Bonne chance ! \n \n Pense à confirmer sur la conversation facebook que tu as bien reçu ce mail! \n Ziboux zboui zboui" %(elem[0], elem[1])
    sendMail("v.maxime@gmail.com", sendingToEmail, "Père Noël Mystère 2019 !!!!!! SECOND TIRAGE", body)
    
for elem in associations:
    if elem[0] != "Maxime" and elem[1] != "Maxime":
        print(elem[0],elem[1])

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    