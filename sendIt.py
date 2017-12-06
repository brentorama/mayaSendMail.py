import maya.mel as mel
import maya.cmds as cmds
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendPyMail():
    USER = mel.eval('getAttr mailNode.userName')
    TOFIELD = mel.eval('getAttr mailNode.toField')
    TEXTFIELD = mel.eval('getAttr mailNode.textField')
    SUBFIELD = mel.eval('getAttr mailNode.subField')
    HTMLSTRING = mel.eval('getAttr mailNode.htmlString')
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USERNAME = mel.eval('getAttr mailNode.emailAddress')
    with open ('//192.168.11.200/_AC_work/forrest/epw.txt', "r") as myfile:
        SMTP_PASSWORD = data=myfile.read()
    
    EMAIL_TO = cmds.textField(TOFIELD,query=True,text=True)
    EMAIL_FROM = mel.eval('getAttr mailNode.emailAddress')
    EMAIL_SUBJECT = cmds.textField(SUBFIELD,query=True,text=True)
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = EMAIL_SUBJECT 
    msg['To'] = EMAIL_TO
    msg['From'] = EMAIL_FROM
    text = cmds.scrollField(TEXTFIELD,query=True,text=True)
    html = HTMLSTRING
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    
    msg.attach(part1)
    msg.attach(part2)
    
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO.split(","), msg.as_string())
    mail.quit()
    print "Email Sent"
    mel.eval ('deleteUI "dailyMailer"')
    mel.eval ('print "Email Sent"')

sendPyMail()
