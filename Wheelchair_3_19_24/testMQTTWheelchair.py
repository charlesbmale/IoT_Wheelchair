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
MQTT_TOPIC = [("vmi\Direction",2),("vmi\Speed",1),("vmi\Brake",0)]

dirr=""
br=""
spd=""


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    data = message.payload
    receive=data.decode("utf-8")
    m_decode = json.loads(receive)
    #print(m_decode)
    #print (m_decode['Server_name'])
    print ("Message received: "  + str(m_decode))
    if( message.topic=="vmi\Direction"):
        dirr=str(m_decode)
    elif (message.topic=="vmi\Speed"):
        spd=str(m_decode)
    elif (message.topic=="vmi\Break"):
        br=str(m_decode)
    
    
Connected = False   #global variable for the state of the connection

client=paho.Client()
client.on_connect = on_connect

client.connect("mqtt.eclipseprojects.io", 1883, 60) 

client.subscribe(MQTT_TOPIC)


print("pres ctrl c to exit")

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
        
    
client.loop_forever()

