from email.mime.text import MIMEText
import smtplib

def send_email(email,name):
    from_email="bdywisher@gmail.com"
    from_password="patidar123"
    to_email=email
    body = '''Hey there....<br>
    Congratulations! You are given 365 more pages to write your story.<br> 
    We already know it’s going to be amazing again.<br>
    On your special day, I wish you the finest things that life can offer you, starting with all the love you deserve!<br>
    Happy birthday!!.<br>
    With lots of Love your friend '''

    subject="Happy Birthday"
    message=(body+"%s" %name)

    msg=MIMEText(message, 'html')
    
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    try:
            gmail=smtplib.SMTP('smtp.gmail.com',587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login(from_email, from_password)
            gmail.send_message(msg)
            gmail.close()
            print('email successfully')
    except:
        print("unsccesful email")

               
    
       