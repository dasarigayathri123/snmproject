import smtplib #simple mail transfer protocol library module used for sending emails across the internet 
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465) # creating object gor gmail
    server.login('dasarigayathri3234@gmail.com','agqe pnyk aray osrq')
    msg=EmailMessage() #creating object for emailmeassage to form email form
    msg['FROM']='dasarigayathri3234@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()