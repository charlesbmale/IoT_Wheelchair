import paho.mqtt.client as mqtt

def on_connect(client, userdata,flags,rc):
	print("conneced")
	client.subscribe("vmi\Direction")

def on_message(client,userdata,msg):
	print(str(msg.payload))

client=mqtt.Client()
client.on_connect = on_connect
on_message(client.on_message

client.connect("mqtt.eclipseprojects.io",1883,60)

client.loop_forever()
