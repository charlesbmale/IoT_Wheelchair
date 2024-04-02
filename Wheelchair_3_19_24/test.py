import paho.mqtt.client as mqtt

def on_connect(client, userdata,flags,rc):
	print("conneced")
	client.subscribe("test")

def on_message(client,userdata,msg):
	print(str(msg.payload))

client=mqtt.Client()
client.on_connect = on_Connect
client.on_message =on_message

client.connect("localhost",1883,60)

client.loop_forever()
