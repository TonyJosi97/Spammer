import smtplib
def mySpammer(fromAddr, message, myMailID, myPassword):
  
  spamServer = smtplib.SMTP('smtp.gmail.com: 587')
  spamServer.starttls()
  spamServer.login(myMailID, myPassword)

  with open('list.csv') as f:
   for line in f:
       fields = line.split(",")
       companyName = fields[0]
       mailID = fields[1]
       header  = 'From: %s\n' % fromAddr
       header += 'Subject: %s\n\n' % companyName
       message = header + message
       print ('Spamming %s, Mail ID: %s' % (companyName, mailID))
       problems = spamServer.sendmail(fromAddr, mailID, message)
       
  return problems
  spamServer.quit()


mySpammer('YOUR MAIL ID', 'MAIL CONTENT', 'YOUR USER NAME', 'YOUR PASSWORD')