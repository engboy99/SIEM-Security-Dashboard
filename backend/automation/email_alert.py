import smtplib
from email.mime.text import MIMEText
import os

def send_email_alert(subject, body, to_email):
    from_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Alert email sent!")
    except Exception as e:
        print(f"Error sending email: {e}")
