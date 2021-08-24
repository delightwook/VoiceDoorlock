
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(('192.168.111.100',8088))


def sendingMsg() :
		file=open("output.wav","rb")
		print 'Success File Open'
		for lines in file.readlines():
			print 'Data Sending....'
			soc.send(lines)
		print 'End'
		file.close();
		print 'file close Success'
