#importing essential libnraries to perform tasks
import os
from email.message import EmailMessage
import smtplib, ssl      #smtplib module is useful to send mail by using (SMTP Protocol)
    # ssl module is use to create encrypted secure connection

sender_email = "singhrishikesh999@gmail.com"
receiver_email = "singhrishikesh977@gmail.com"
password = "lqzhfxjhyqyltqps"

# to send mail to multiple people
receiver_bulk_email = [
    "singhrishikesh977@gmail.com",
    "rishikesh159singh@gmail.com",
    "anksingh612@gmail.com",
    "rishikesh101singh@gmail.com",
]

# to send mail to multiple people in bcc
receiver_bulk_bcc_email = [
    "singhrishikesh977@gmail.com",
    "rishikesh159singh@gmail.com",
    "anksingh612@gmail.com",
    "rishikesh101singh@gmail.com",
]

subject = "Automated Email Test"
subject1 = "Automated Bulk Email Test"
body = "This is an automated email sent via Python" 
body1 = "This is an automated email sent via Python with attachment"
body2 = "This is an automated bulk email sent via Python"


message = EmailMessage()

message['From'] = sender_email
#message['To'] = receiver_bulk_email
message['Bcc'] = ",".join(receiver_bulk_bcc_email)
message['Subject'] = subject1
message.set_content(body2)

#this part only for those receiver who supports HTML

# Set HTML content
html_content = """
<html>
  <body>
    <h2 style="color: blue;">Hello Rishikesh! 👋</h2>
    <p>This email is sent <b>automatically</b> using <span style="color: green;">Python</span>.</p>
    <p>Click below to visit:</p>
    <a href="https://www.python.org">Go to Python.org</a>
    <hr>
    <p style="font-size: 12px; color: gray;">This is a test mail. Please ignore if not relevant.</p>
  </body>
</html>
"""

message.add_alternative(html_content, subtype='html')

#================ This part of code is to send an email with attachment=================#

# file_path = os.path.join(os.path.expanduser("~"), "Desktop", "test_folder")
# file_name = "new_renamed_data.rtf"  
# full_path = os.path.join(file_path, file_name)

# with open(full_path, "rb") as f:
#     file_data=f.read()
#     file_type="application/rtf"
#     message.add_attachment(file_data, maintype="application", subtype="rtf", filename=full_path)

#========================================================================================#

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(message)
        #server.sendmail(sender_email,receiver_email, message)
        print("✅ HTML Email sent successfully!")
except Exception as e:
    print(f"❌ Error: {e}")

