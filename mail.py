def mail(list,otp):
    from smtplib import SMTP,SMTPAuthenticationError,SMTPException
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    host = "smtp.gmail.com"
    port = 587
    username = "soubhagyakumar666@gmail.com"
    password = "SOubh@gy@519"
    from_email= username
    to_list=list

    try:
        email_conn = SMTP(host, port)
        email_conn.ehlo()
        email_conn.starttls()
        email_conn.login(username,password)

        the_msg = MIMEMultipart("alternative")
        the_msg['subject'] ="jobcental: verify otp !"
        the_msg["from"]=from_email
        # the_msg["to"]=to_list

        plain_txt = "testing the message"

        html_text = """\
        <!DOCTYPE html>
        <html>
        <body>

        <div class="card" style="background-image:url('/static/bg/3.jpg');background:#cf4a3d;border-radius:15px;">
        <h2 style="padding:20px;color:white;text-align:center;">Verify your email ..</h2>
        <h3 style="padding:20px;color:white;text-align:center;">Dear user your otp is : {}</h3>
        <h1 style="padding:20px;color:white;text-align:center;">OR</h1>
        <h4 style="padding:20px;color:white;text-align:center;"><a href="https://google.com/" style="color:white;">
        Click here to reset your password.
        </a></h4>
        <h5 style="padding:20px;color:white;">
        Regards JobCentral Team..
        </h5>
        </div>
        <br>
        <br>

        </body>
        </html>
        """.format(otp)

        part_1 = MIMEText(plain_txt,'plain')
        part_2 = MIMEText(html_text,"html")
        the_msg.attach(part_1)
        the_msg.attach(part_2)
        print(the_msg.as_string())
        email_conn.sendmail(from_email,to_list,the_msg.as_string())
        email_conn.quit()
    except SMTPException:
        print("some thing went wrong")

# list=["soubhagyakumar666@gmail.com"]
# email(list)




def otp_html_contents():
    contents = """\


            <!DOCTYPE html>
            <html lang="en">
            <!-- Mirrored from byrushan.com/projects/super-admin/app/2.1.2/blog-detail.html by HTTrack Website Copier/3.x [XR&CO'2014], Mon, 05 Feb 2018 04:17:45 GMT -->
            <head>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
            <style media="screen">
            *{
              color:white;
              text-align:center;
            }
            a{
            text-decoration:none;
            color:white;
            }
            </style>
            </head>



            <div class="card" style="background-image:url('/static/bg/3.jpg');background:#cf4a3d;border-radius:15px;">
            <h2 style="padding:20px;">Verify your email ..</h2>
            <h3 style="padding:20px;">Dear user your otp is : {}</h3>
            <h1 style="padding:20px;">OR</h1>
            <h4 style="padding:20px;"><a href="https://google.com/" style="color:white;">
            Click here to reset your password.
            </a></h4>

            <h5 style="padding:20px;float:right;">
            Regards JobCentral Team..
            </h5>

            <br><br>
            </div>

            </html>


    """
    return contents
