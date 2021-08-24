#!/usr/bin/env python3

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path


AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "output.flac")
r = sr.Recognizer()
def startSpeech() :
	print 'In StartSpeech function'
	# use the audio file as the audio source
	global result
	with sr.AudioFile(AUDIO_FILE) as source:
   		print("start record") 
		audio = r.record(source) # read the entire audio file
		print("end record")

	try:
    		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
		# instead of `r.recognize_google(audio, show_all=True)`
    		from pprint import pprint
	    	print("Google Speech Recognition results:")
    		print(r.recognize_google(audio))
    		result = r.recognize_google(audio)
  #  pprint(r.recognize_google(audio, show_all=True)) # pretty-print the recognition result
	except sr.UnknownValueError:
    		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
    		print("Could not request results from Google Speech Recognition service; {0}".format(e))

