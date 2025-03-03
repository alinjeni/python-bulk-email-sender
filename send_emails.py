import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import chardet

with open('Mail.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")


# SMTP settings
SMTP_SERVER = "smtp.gmail.com"  # Change for Outlook/Yahoo
SMTP_PORT = 587
EMAIL_SENDER = "abc@gmail.com" 
EMAIL_PASSWORD = "xxxx xxxx xxxx xxxx"  # Use App Password if needed 

# Email details
EMAIL_SUBJECT = "Inquiry About Job Opportunities – Software Engineer"
EMAIL_BODY = """Dear HR,

I hope you’re doing well. My name is xxxx, and I am a Software Engineer with..... 

Looking forward to your response.

Best regards,
xxxxx,
yyy789987,
abc@gmail.com"""

# Attachment file path (Change this to your actual file)
ATTACHMENT_PATH = "Resume.pdf"

# Read emails from CSV
csv_file = "Mail.csv"  # Change to your CSV file name
df = pd.read_csv(csv_file, encoding=encoding)
email_list = df["Email"].dropna().tolist()  # Ensure "Email" column exists

def send_email(recipient_email):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = recipient_email
        msg["Subject"] = EMAIL_SUBJECT
        msg.attach(MIMEText(EMAIL_BODY, "plain"))

        # Attach file
        if ATTACHMENT_PATH:
            with open(ATTACHMENT_PATH, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={ATTACHMENT_PATH.split('/')[-1]}")
                msg.attach(part)

        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, recipient_email, msg.as_string())
        server.quit()

        print(f"Email sent successfully to {recipient_email}")

    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")

# Send emails to all recipients
for email in email_list:
    send_email(email)
