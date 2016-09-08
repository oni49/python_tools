import smtplib, sys

def simpleCheck(emailList):
	domain = 'smtp.gmail.com'
	port = 25
	server = smtplib.SMTP(host=domain,port=port)
	for email in emailList:
		resCode = server.verify(email)[0]
		if resCode in range(200,300):
			print email, '\tGOOD\t', resCode
		else:
			print email, '\tBAD\t', resCode
	server.quit()
	
if __name__ == "__main__":
	simpleCheck(sys.argv[1:])