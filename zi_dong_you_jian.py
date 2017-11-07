import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'c1135805493@sina.com'
msg['to'] = '1135805493@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.sina.com', '25')
smtp.login('c1135805493@sina.com', '199842.')
smtp.sendmail('c1135805493@sina.com', '1135805493@qq.com', str(msg))
smtp.quit()