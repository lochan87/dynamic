import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from certificate import create_certificate

def send_email(recipient_email, certificate_io, participant_name):
    sender_email = "lochantn5277@gmail.com"
    sender_password = "atrr zdkp zdsl gozl"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Certificate of Appreciation" 

    body = "Hi "+participant_name+",\n\nPlease find the Certificate of Appreciation awarded for your incredible work attached.\n\nRegards,\nNYB,\nXYZ Team"
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
    print('Email sent successfully to', recipient_email)

# Example usage:
participant_name = "Disha N G"
certificate_io = create_certificate(participant_name)
send_email("ngdisha72@gmail.com", certificate_io, participant_name)
