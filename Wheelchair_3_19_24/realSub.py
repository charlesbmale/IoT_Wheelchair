#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.wattnotions.com/pretty-small-robot-adding-mqtt-for-remote-control/
import time
import sys
import os
from gpiozero_extended import Motor
import keyboard
import RPi.GPIO as GPIO
import paho.mqtt.client as paho

GPIO.setmode(GPIO.BCM)

#Breaks input
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

#Motor input
mymotor1 = Motor(enable1=20, enable2 = 21, pwm1=19, pwm2=26)
mymotor2 = Motor(enable1=11, enable2 = 9, pwm1=18, pwm2=17)

#Starting forward speed
fspeed=0.5

#Starting backwards speed
bspeed=-0.5

# Direction
def on_message_dir(mosq, obj, msg):

    print(str(msg.payload.decode("utf-8")))
    if (str(msg.payload)=="up"):
        print("Moving forwards")
        mymotor1.set_output(fspeed)
        mymotor2.set_output(fspeed)

    elif (str(msg.payload)=="down"):
        print("Reversing")
        mymotor1.set_output(bspeed)  #make speed negative
        mymotor2.set_output(bspeed)

    elif (str(msg.payload)=="left"):
        print("Turning left")
        mymotor1.set_output(bspeed)
        mymotor2.set_output(fspeed)

    elif (str(msg.payload)=="right"):
        print("Turning right")
        mymotor1.set_output(fspeed)
        mymotor2.set_output(bspeed)

# Speed
def on_message_spd(mosq, obj, msg):
    global fspeed
    global bspeed
    print(str(msg.payload.decode("utf-8")))
    if (str(msg.payload)=="up"):
        fspeed += .1
        print("increasing forward speed")
    #        lcd.message("RL1= 0 RL2= 0")
    elif (str(msg.payload.decode("utf-8"))=="down"):
       fspeed -= .1
       print("decreasing forward speed")

    elif (str(msg.payload.decode("utf-8"))=="Bup"):
        bspeed -= .1
        print("increasing backwards speed")

    elif (str(msg.payload.decode("utf-8"))=="Bdown"):
        bspeed -= .1
        print("decreasing backwards speed")
#

# Break
def on_message_br(mosq, obj, msg):
    print(str(msg.payload.decode("utf-8")))
    if (str(msg.payload)) == 'off':
        print("breaks unlocked")
        GPIO.output(37, 1)
        GPIO.output(38, 1)

### topic message
def on_message(mosq, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload.decode("utf-8")))

mqttc = paho.Client()

mqttc.message_callback_add('vmi/Break', on_message_br)
mqttc.message_callback_add('vmi/Speed', on_message_spd)
mqttc.message_callback_add('vmi/Direction', on_message_dir)
mqttc.on_message = on_message
mqttc.connect("mqtt.eclipseprojects.io", 1883, 30)
mqttc.subscribe("vmi/#")

mqttc.loop_forever()
