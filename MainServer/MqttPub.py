import paho.mqtt.client as mqtt
import random
import time

mqttc = mqtt.Client("python_pub")
mqttc.connect("192.168.111.100",1883)

def MqttPub(result):

	if result == 'hi' : 
   		tf = 'TRUE'
		print(result)
		mqttc.publish("Speech_recognition/result",tf)
		print("Success Send")
	else :
		tf = 'FALSE'
		print("No answer")
		mqttc.publish("Speech_recognition/result",tf)
#	time.sleep(2)
#	mqttc.loop(2)
