import smtplib
import base64
import sys
sys.path.append('/root')

from pas import password

sys.dont_write_bytecode = True


def send_mail(to_addr = 'rvdaescu@gmail.com', subj = None, msg = None):
    """
    msg must contain subject \n\n + body
    """

    server = smtplib.SMTP_SSL('mail.vhsmail.vodafone.com', 465)

    server.login('office@daescu.ro', password)
    sub_msg =  'Subject: ' + subj + ' \n\n\n ' + msg + '\r\n'

    sent = False
    while not sent:
        try:
            server.sendmail('office@daescu.ro', to_addr , sub_msg)
            sent = True
        except Exception,e:
            print e
            continue

    server.quit()
