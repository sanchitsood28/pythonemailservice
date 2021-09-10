from flask import Flask,render_template,request
import tkinter
from tkinter import messagebox
import smtplib
import mimetypes
import email.mime.application
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

@app.route('/',methods =['POST','GET'])



def sendMailTo():
    

  
    id=''
    message=''
    check=None
    #Comment/Uncomment filename based on local or server storage
    #filename = '..//application//static//fu.png'
    filename = '/home/essurprise/mysite/static/fu.png'
    print(filename)
    fo=open(filename,'rb')
    attach = email.mime.application.MIMEApplication(fo.read(),_subtype="png")
    attach.add_header('Content-Disposition','attachment',filename="Surprise.png")
    fo.close()

    if request.method=="POST" and 'mail' in request.form and 'message' in request.form:
      id = request.form.get('mail')
      message = request.form.get('message')
      sender_address ="" #Type in email
      sender_pass ="" #Type in password
      receiver_address =request.form.get('mail')
      mail_content= "Hey Fucker!"+"\n"+"\n"+request.form.get('message')+"\n"+"\n"+"Regards"+"\n"+"Another Fucker!"
      print('Checker1',receiver_address)
      if receiver_address and mail_content:
            print('Checker2',receiver_address)
            check="1"  
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Find your gift as attachment.'
            message.attach(MIMEText(mail_content, 'plain'))
            message.attach(attach)
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(sender_address, sender_pass)
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent')
            receiver_address=None
      else:
            check="0"
            print("No Receiver")    
    elif id is None:
      print("Error")  
    return render_template('index.html',id=id,check=check)
