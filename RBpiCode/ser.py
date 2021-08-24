import paho.mqtt.client as mqtt
import RealDoor
import time
def on_connect(client,userdata,rc) :
    print'Success'
    print("Connected with result code" +str(rc))

    client.subscribe("Speech_recognition/result")
    print 'Connect Good'
    
def on_message(client,userdata,msg):
    global save1
    print 'on_message in Function'
    save1 = str(msg.payload)
    print save1
    if save1 == "TRUE" :
        print 'Door open'
	logic = "TRUE"
        RealDoor.DoorFunction(logic)
	time.sleep(2)
	logic = "anyway"
        RealDoor.DoorFunction(logic)
	time.sleep(5)
	logic = "TRUE"
	RealDoor.DoorFunction(logic)
	time.sleep(2)
	logic="anyway"
	RealDoor.DoorFunction(logic)
    else :
        print 'Not Door open'
	logic ="FALSE"
        RealDoor.DoorFunction(logic)
try :
        
	save1 = ""
	print ' wait Receive Data'

	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect("[IP address]",1883,60)
	print 'connect Success'
	client.loop_forever()

except KeyboardInterrupt : 
	logic = "in"
	RealDoor.DoorFunction(logic)
                     

                     
    
