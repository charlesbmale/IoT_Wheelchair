import paho.mqtt.client as paho
from paho import mqtt
import sys
import keyboard


def on_connect(client, userdata, flags, rc, properties=None):
	print("CONNACK received with code %s." % rc)


client = paho.Client()
client.on_connect = on_connect

if client.connect('192.0.0.238', 1883)!=0:
	print("could not connect to mqtt broker")
	sys.exit(-1)
else:
	client.on_connect
	print("connection established")


client.publish("vmi/Break","Break ----hello world from paho")
client.publish("vmi/Speed","Speed ----hello world from paho")
client.publish("vmi/Direction","Direction ----hello world from paho")

while keyboard.is_pressed('esc')!=True:
	#Unlock Breaks and Keep breaks unlocked until space is unlocked. If statement is false then other actions are not allowed
	while keyboard.is_pressed('space') != True:
		client.publish("vmi/Break", "On")
		print("Breaks locked")

	while keyboard.is_pressed('space'):
		print("Breaks unlocked")
		client.publish("vmi/Break", "Off")
	#Forwards
		while keyboard.is_pressed('up arrow'):
			print("Moving Forward")
			client.publish("vmi/Direction","Forward")
	#Reverse
		while keyboard.is_pressed('down arrow'):
			print("Moving Backwards")
			client.publish("vmi/Direction","Back")

	#Increase forward speed
			if keyboard.is_pressed('w'):
				print("Speed increased")
				client.publish("vmi/Speed","Faster")

	#Decrease forward speed
			elif keyboard.is_pressed("s"):
				print("Speed decrease")
				client.publish("vmi/Speed", "Slower")

	#Turn Right
		while keyboard.is_pressed('right arrow'):
			print("turning right")
			client.publish("vmi/Direction","Right")
			
	#Turn Left
		while keyboard.is_pressed('left arrow'):
			print("turning left")
			client.publish("vmi/Direction","Left")


client.disconnect
