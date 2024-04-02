import paho.mqtt.client as paho
import time
from gpiozero_extended import Motor
import keyboard
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

# Creating motor object using GPIO pins 16, 17, and 18
# (using SN754410 quadruple half-H driver chip)
mymotor1 = Motor(enable1=16, pwm1=17, pwm2=18)
mymotor2 = Motor(enable1=6, pwm1=14, pwm2=15)

def on_connect(client, userdata,flags,rc):
	print("conneced") 
dirr=""
spd=""
br=""

def on_message(client,userdata,msg):
	print(str(msg.payload))
    

 
clientd=paho.Client()
clientd.on_connect = on_connect
clientd.on_message =on_message
clientd.subscribe("Direction")
clients=paho.Client()
clients.subscribe("Speed")
clientb=paho.Client()
clientb.subscribe("Brake")

if clientd.connect("mqtt.eclipseprojects.io", 1883, 60) != 0:
    print("could not connect to mqtt broker!")
    sys.exit(-1)
if clients.connect("mqtt.eclipseprojects.io", 1883, 60) != 0:
    print("could not connect to mqtt broker!")
    sys.exit(-1)
if clientb.connect("mqtt.eclipseprojects.io", 1883, 60) != 0:
    print("could not connect to mqtt broker!")
    sys.exit(-1)
    
running =True
while (running == True):
    Speed = spd
    direction = dirr
    if (direction == "Forward"):
        mymotor1.set_output(speed)
        mymotor2.set_output(speed)
    elif (direction == "Backward"):
        mymotor1.set_output(speed)
        mymotor2.set_output(speed)
    breakWheel = br
    if (breakWheel == "0"):

        mymotor1.set_output(0)
        mymotor2.set_output(0)
    elif (breakWheel == "1"):
        speed = .5
        time.sleep(1)
        mymotor1.set_output(speed)
        mymotor2.set_output(speed)

try:
    print("pres ctrl c to exit")
    client.loop_forver()
except:
    print("disconecting from broker")

client.disconnect
