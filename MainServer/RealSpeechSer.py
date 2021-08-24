import socket,threading
import encoder
import extended_results
import MqttPub

sem = threading.Semaphore() # Lock Object Get
cv = threading.Condition()
count = 0
th = [] # Input Thread List
conns = [] #  Client connection List

# Create Socket
#soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


HOST=''
PORT=8088
ADDR=(HOST,PORT)

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(ADDR)
soc.listen(1)


def get_client(conn,addr,count):
	cnt = count
	print '\n'
	print '\n'
	print '########################################'
	print 'from %s, user %d is Access'%(addr[0],cnt)

	file = open("117.17.73.106.wav","wb")
	while True:
		data = conn.recv(1024)
		if not data :
			break
		else :
			file.write(data)
	print 'user %d is Complete Data Transfer' %(cnt)
	print '########################################'
	file.close()
	encoder.startEncoder()
	print 'call startSpeech '
	extended_results.startSpeech()
	MqttPub.MqttPub(extended_results.result)
	conn.close()
	print ' User %d is Exit' %(cnt)
	print '########################################'
	

while 1:
	print '########################################'
	print 'Waiting User'
	conn,addr = soc.accept()
	print 'login User'
	conns.append(conn)

	sem.acquire()
	count +=1
	sem.release()
	client = threading.Thread(target=get_client,args=(conn,addr,count))
	client.start()
	th.append(client)
for t in th:
	t.join()
