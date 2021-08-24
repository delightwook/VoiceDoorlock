
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(('[IP address]',8088))


def sendingMsg() :
		file=open("output.wav","rb")
		print 'Success File Open'
		for lines in file.readlines():
			print 'Data Sending....'
			soc.send(lines)
		print 'End'
		file.close();
		print 'file close Success'
