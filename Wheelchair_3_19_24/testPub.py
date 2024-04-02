import paho.mqtt.client as paho
import sys

client= paho.Client()
if client.connect("localhost",1883,60)!=0:
	print("could not connect")
	sys.exit
	
def on_connect(client, userdata,flags,rc):
	print("conneced")
	
client.on_connect
client.publish("test","working")

client.disconnect
