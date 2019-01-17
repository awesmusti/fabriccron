import smtplib
import subprocess
p1 = subprocess.Popen(['hostname'], stdout=subprocess.PIPE)
a = (p1.communicate()[0]).decode('ascii')
p2 = subprocess.Popen(['uptime','-p'], stdout=subprocess.PIPE)
b = (p2.communicate()[0]).decode('ascii')
d=" Hostname: "
e="\n Uptime: "
c=d+a[0:10]+e+b[3:29]

#print(c)

gmail_user = 'maniapersie@gmail.com'  
gmail_password = '8lWbmwGf'

sent_from = gmail_user  
to = ['awais.mustafa@nxb.com.pk']  
subject = 'Python Final Task'  
body1 = c

message = """From: Persie
To:<awais.mustafa@nxb.com.pk>
Subject: Cron Stats Update

{0}
"""

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, message.format(c))
    server.close()
#   print('Email sent!')
except:  
    print('Something went wrong...')
