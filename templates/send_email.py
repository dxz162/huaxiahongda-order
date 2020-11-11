  
from email.mime.text import MIMEText
import smtplib

def send_email(email, product, quant):
    from_email="davidzhengdy@gmail.com"
    from_password="maomi2019"
    to_email=email

    subject="Product data"
    message="您好,我是华夏矿产科技的桃小姐，您订购的产品规格为 <strong>%s</strong>. <br> 采购数量为 <strong>%s</strong>. <br> 感谢您的购买!" % (product, quant)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)