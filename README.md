# Bulk Email Sender

This Python script enables users to send personalized emails with attachments to multiple recipients listed in a CSV file. It's particularly useful for tasks like job applications, newsletters, or any scenario requiring bulk email distribution.

## Features

- **Bulk Email Sending**: Automatically send emails to a list of recipients specified in a CSV file.
- **Attachment Support**: Attach files (e.g., resumes, brochures) to each email.
- **Personalized Content**: Customize the email body for each recipient.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `smtplib`
  - `pandas`
  - `email`
  - `chardet`

You can install the necessary libraries using:

```bash
pip install pandas chardet
```


## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/alinjeni/python-bulk-email-sender.git
   cd python-bulk-email-sender
   ```


2. **Prepare the CSV File**:

   - Create a `Mail.csv` file containing a column labeled `Email` with the list of recipient email addresses.
   - Ensure there are no blank lines or extra spaces in the email addresses.

3. **Configure the Script**:

   - Open the script and update the following variables:
     - `SMTP_SERVER`: Set to your email provider's SMTP server (e.g., `'smtp.gmail.com'` for Gmail).
     - `SMTP_PORT`: Set to the appropriate port (e.g., `587` for TLS).
     - `EMAIL_SENDER`: Your email address.
     - `EMAIL_PASSWORD`: Your email password or app-specific password.
     - `EMAIL_SUBJECT`: Subject of the email.
     - `EMAIL_BODY`: Body of the email.
     - `ATTACHMENT_PATH`: Path to the file you wish to attach.

## Usage

Run the script using:

```bash
python send_emails.py
```


The script will read the `Mail.csv` file, detect its encoding using `chardet`, and send emails to each address listed.

## Important Notes

- **Email Provider Settings**: The script is configured to use Gmail's SMTP server. If you're using a different email provider, adjust the `SMTP_SERVER` and `SMTP_PORT` settings accordingly.

- **App Passwords**: For Gmail users with 2-Step Verification enabled, generate an App Password and use it as the `EMAIL_PASSWORD`.

- **Avoiding Spam Filters**: To minimize the chances of your emails being marked as spam, consider the following:
  - Send emails in smaller batches.
  - Personalize the email content.
  - Ensure that your email content complies with anti-spam policies.

## References

- [Sending Emails With Python - Real Python](https://realpython.com/python-send-email/)
- [How to Send Email in Python: SMTP & Email API Methods Explained](https://mailtrap.io/blog/python-send-email/)
- [Sending Bulk Emails with Python: A Step-by-Step Guide](https://medium.com/@himanshu.developer01/sending-bulk-emails-with-python-a-step-by-step-guide-f27802512d18)

For more detailed explanations and advanced configurations, refer to the articles linked above.
