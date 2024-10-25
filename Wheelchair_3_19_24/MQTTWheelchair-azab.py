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
mymotor1 = Motor(enable1 =20, enable2 = 21, pwm1=19, pwm2=26)
# mymotor1= Motor(forward=20,backward=21)
mymotor2 = Motor(enable1=11, enable2 = 9, pwm1=18, pwm2=17)
MQTT_TOPIC = [("vmi/Direction",2),("vmi/Speed",1),("vmi/Brake",0)]

 


    
def on_connect(client, userdata, flags, rc):
    if rc == 0: # rc is only a non zero number when an error is thrown
        print("Connected to broker")
        client.subscribe(MQTT_TOPIC)    # Subscribes the wheelchair to the 3 topics
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    dirr=""
    br=""
    spd=""
    data = message.payload
    
    
    receive=data.decode("utf-8")
    m_decode = receive 
    
    
    print ("Message received: "  + str(m_decode))
    if( message.topic=="vmi/Direction"):
        dirr=str(m_decode)
        print(dirr)
    elif (message.topic=="vmi/Speed"):
        spd=str(m_decode)
    elif (message.topic=="vmi/Break"):
        br=str(m_decode)
    chair(dirr,spd,br)
    

client=paho.Client()
client.on_connect = on_connect
client.on_message =on_message


#client.loop_start()        #start the loop


client.connect('192.0.0.238',1883,60)
client.subscribe(MQTT_TOPIC)

def chair(dirr,spd,br):
       # time.sleep(1)

        #Speed = spd
        #you are not changing the speed in the publishedr code!!
        speed = .5
        direction = dirr
        


        breakWheel = br
        if (breakWheel == "On"):
                mymotor1.set_output(0)
                mymotor2.set_output(0)
                
        elif (breakWheel == "Off"):
                speed = .5
                time.sleep(1)
                mymotor1.set_output(speed)
                mymotor2.set_output(speed)
         
        if (direction == "Forward"):
                mymotor1.set_output(speed)
                mymotor2.set_output(speed)
        elif (direction == "Back"):
                mymotor1.set_output(-speed)
                mymotor2.set_output(-speed)
               
        elif (direction == "Right"):
            mymotor1.set_output(.5)
            mymotor2.set_output(-.5)
        elif (direction == "Left"):
            mymotor1.set_output(-.5)
            mymotor2.set_output(.5)

        if (spd == 'Faster'):
            speed =speed + .3
        elif(spd == 'Slower'):
            speed = speed - .3
            
        

try:  

        print("pres ctrl c to exit")
        client.loop_forever() # loops the code untill broken by ctrl c
except KeyboardInterrupt:
        print("disconecting from broker")
        client.disconnect()
        client.loop_stop()

 

   
