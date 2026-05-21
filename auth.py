import firebase_admin
from firebase_admin import credentials, auth
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def send_verification_email(email, verification_link):
    msg = MIMEMultipart()
    msg['From'] = 'ita27rmp100@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'Email Verification'
    body = f'Click this link to verify your email: {verification_link}'
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], 'password')
    text = msg.as_string()
    server.sendmail(msg['From'], msg['To'], text)
    server.quit()

def verify_email(email):
    user = auth.get_user_by_email(email)
    if user.email_verified:
        return True
    else:
        return False

def create_user(email, password):
    user = auth.create_user(email=email, password=password)
    verification_link = auth.generate_email_verification_link(email)
    send_verification_email(email, verification_link)
    return user

def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        if user.email_verified:
            return True
        else:
            return False
    except:
        return False

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'create':
            email = input('Enter email: ')
            password = input('Enter password: ')
            create_user(email, password)
            print('User created successfully')
        elif sys.argv[1] == 'login':
            email = input('Enter email: ')
            password = input('Enter password: ')
            if login_user(email, password):
                print('Login successful')
            else:
                print('Invalid credentials')
        elif sys.argv[1] == 'verify':
            email = input('Enter email: ')
            if verify_email(email):
                print('Email verified')
            else:
                print('Email not verified')
        else:
            print('Invalid command')
    else:
        print('Usage: python script.py <create/login/verify>')

if __name__ == '__main__':
    main()
