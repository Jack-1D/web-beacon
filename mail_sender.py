import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from web_bug_html import web_bug
from web_beacon_html import web_beacon

load_dotenv()
source = os.getenv('SOURCE_GMAIL')
password = os.getenv('PASSWORD')
target = os.getenv('TARGET_GMAIL')

mail = MIMEText(web_bug(), 'html', 'utf-8')
mail['Subject'] = "test mail"
mail['From'] = 'Jack'
mail['To'] = target

if __name__ == "__main__":
    smtp = smtplib.SMTP('smtp.gmail.com', 587)    # SMTP secure default port: 587
    smtp.ehlo()                         # 向伺服器表明身分，詢問對方是否支援 ESMTP
    smtp.starttls()                     # 開始TLS交握
    smtp.login(source, password)
    status = smtp.send_message(mail)
    print(status)
    smtp.quit