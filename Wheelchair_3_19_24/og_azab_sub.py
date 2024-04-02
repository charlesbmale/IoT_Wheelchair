
#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import os
import paho.mqtt.client as paho

### RELAY
def on_message_dir(mosq, obj, msg):
    print(str(msg.payload))
#    if (str(msg.payload)[3]) == '0':
#        lcd.set_cursor(7,2)
#        lcd.message("RL1= 0 RL2= 0")
#    elif (str(msg.payload)[3]) == '1':
#        lcd.set_cursor(7,2)
#        lcd.message("RL1= 1 RL2= 0")
#    elif (str(msg.payload)[3]) == '2':
#        lcd.set_cursor(7,2)
#        lcd.message("RL1= 0 RL2= 1")
#    elif (str(msg.payload)[3]) == '3':
#        lcd.set_cursor(7,2)
#        lcd.message("RL1= 1 RL2= 1")
#    else:
#        lcd.set_cursor(7,2)
#        lcd.message("RELAYs ERROR!")


### HUMIDITY
def on_message_spd(mosq, obj, msg):
    print(str(msg.payload))
#    lcd.set_cursor(7,3)
#    lcd.message(str(msg.payload)[0:4]+chr(37))

### PRESSURE
def on_message_br(mosq, obj, msg):
    print(str(msg.payload))
#    lcd.set_cursor(13,3)
#    lcd.message(str(msg.payload)+"hPa")

### topic message
def on_message(mosq, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

mqttc = paho.Client()

mqttc.message_callback_add('vmi/Break', on_message_br)
mqttc.message_callback_add('vmi/Speed', on_message_spd)
mqttc.message_callback_add('vmi/Direction', on_message_dir)
mqttc.on_message = on_message
mqttc.connect("mqtt.eclipseprojects.io", 1883, 30)
mqttc.subscribe("vmi/#")

mqttc.loop_forever()