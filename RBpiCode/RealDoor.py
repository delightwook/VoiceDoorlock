import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

def DoorFunction(logic) :
	if logic == "TRUE" :
		print "Door Open"
		GPIO.output(18,False)
	elif logic == "FALSE" :
		print "False Door Open"
	elif logic == "anyway" :
		print "Door Close"
		GPIO.output(18,True)
	elif logic == "in" :
		print "Clean"
		GPIO.cleanup()

