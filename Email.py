import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'yinkz4real@gmail.com'
email['to'] = 'idumuolayinka@gmail.com'  # receiver's email id
email['subject'] = 'How are you?'     # subject of the email

# Content to be sent
email.set_content('We are here to make you happy and good')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # Identify yourself to an ESMTP server using EHLO
    smtp.starttls()  # Put the SMTP connection in TLS (Transport Layer Security) mode
    # Sender's email ID and password
    smtp.login('olayinkaidumu@gmail.com', 'ffwrerlwckobckxc')
    smtp.send_message(email)
    print('Check your email ;)')
