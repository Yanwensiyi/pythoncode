import smtplib
from email.message import EmailMessage as em
class mail:
  def __init__(self,domain,user,passwd):
    self.smserv=smtplib.SMTP(domain)
    self.smserv.login(user,passwd)
    self.user=user
    return
  
  def __del__(self):
    self.smserv.quit()
    return
  
  def send(self,to_user,text,title):
    msg=em()
    msg.set_content(text)
    msg["Subject"]=title
    msg["From"]=self.user
    msg["To"]=to_user
    self.smserv.send_message(msg)
    return
  
  pass
