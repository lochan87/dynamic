import smtplib
import csv
from io import BytesIO
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from certificate import create_certificate

def send_mail(recipient_email, certificate_io, participant_name):
    sender_email = " " # Your email address
    sender_password = " " # Your app password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Certificate of Appreciation" 

    body = "Hi "+participant_name+",\n\nPlease find the Certificate of Appreciation awarded for your incredible work attached.\n\nRegards,\nXYZ Team"
    msg.attach(MIMEText(body, 'plain'))

    # Attach the in-memory certificate
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(certificate_io.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="'+participant_name+'.png"')
    msg.attach(part)

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print('Email sent successfully to', participant_name)

def send_mails_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            participant_name = row['Name']
            recipient_email = row['Email']
            certificate_io = create_certificate(participant_name)
            send_mail(recipient_email, certificate_io, participant_name)

# Example usage:
csv_file_path = 'list.csv' # Your CSV file listing participant names and email addresses
send_mails_from_csv(csv_file_path)