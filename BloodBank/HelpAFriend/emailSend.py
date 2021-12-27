import smtplib

content = "Hello "
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('bloodbank2002@gmail.com','bloodbank.project')
mail.sendmail('bloodbank2002@gmail.com','Vishalbidari2002@gmail.com',content)
