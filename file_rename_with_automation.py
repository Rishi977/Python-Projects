import os
import smtplib, ssl
from email.message import EmailMessage


folder_path = "/Users/rishikeshsingh/Desktop/test_folder"

for filename in os.listdir(folder_path):
    if filename.endswith(".rtf"):
        new_name = "rename_" + filename


        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)


        os.rename(old_file, new_file)

        print(f"File rename successfully from {filename} ---> {new_name}")


bulk_email = ["singhrishikesh977@gmail.com",
              "rishikesh101singh@gmail.com",
              "anksingh612@gmail.com"]

send_email = "singhrishikesh999@gmail.com"
receiver_email = bulk_email
password = "mddthlpovmaeazwf"
subject = "This is a Test Email Automation"
body = "This body is the part of the Test Email Automation"

message = EmailMessage()

message["From"] = send_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

html_content= """
<html>
 <body>
    <h2 style="color:blue">Hello Rishikesh!</h2>
    <p> this the body part of the test HTML EMAIL TEST AUTOMATION</p>
    <p>Click below to visit my Github page</p>
    <a href="https://github.com/Rishi977/">Go to My Github Page</a>
    <hr>
    <p style="color:red; font-size:12px">If it is not relevent to you. Please ignore</p>
 </body>
</html>
"""

message.add_alternative(html_content, subtype="html")



#file_path = os.path.join(os.path.expanduser('~'), "Desktop", "test_folder")
file_path = folder_path
for at_filename in os.listdir(file_path):
    if at_filename == ".DS_Store":
        continue
    file_name = at_filename
    full_path = os.path.join(file_path, file_name)

    with open(full_path, "rb") as f:
        file_data = f.read()
        file_type= "application/rtf"
        print(file_name)
        message.add_attachment(file_data, maintype="application", subtype="rtf", filename=full_path)


context = ssl.create_default_context()


try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(send_email, password)
        server.send_message(message)
        #server.sendmail(send_email,receiver_email,message)
        print("HTML Email sent successfully with attachment!")
except Exception as e:
    print(f"Error: {e}")



