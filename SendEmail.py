import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('SendEmail.html').read_text())
email = EmailMessage()
email['from'] = 'Idumu Olayinka'
email['to'] = 'idumuolayinka@gmail.com'
email['subject'] = 'You won 1,000,000 dollars'


email.set_content(html.substitute({'name': 'TinTin'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('olayinka.idumu@gmail.com', 'ffwrerlwckobckxc')
    smtp.send_message(email)
    print('sent to the client')
