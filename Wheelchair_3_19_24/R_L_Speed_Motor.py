import time
from gpiozero_extended import Motor
import keyboard
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(37,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)


mymotor1 = Motor(enable1 = 16, pwm1=17, pwm2=18)
mymotor2 = Motor(enable1 = 6, pwm1=14, pwm2=15)
fspeed = 0.5
bspeed=-0.5

def keyboardControl():
	global fspeed
	global bspeed
	
	while keyboard.is_pressed('space'):
		print("Safetly Lock Off")
 
		
		GPIO.output(37,1)
		GPIO.output(38,1)
		
		while(keyboard.is_pressed('up arrow')):
			mymotor1.set_output(fspeed)
			mymotor2.set_output(fspeed)
			
			if(keyboard.is_pressed('f') and fspeed < 2.0 ):
				fspeed+=0.1
				time.sleep(0.5)
			elif(keyboard.is_pressed('s') and fspeed > 0.3 ):
				fspeed-=0.1
				time.sleep(0.5)
				 
			print(fspeed)
			
			#print("Up Arrow")
		while keyboard.is_pressed('down arrow'):
			mymotor1.set_output(bspeed)
			mymotor2.set_output(bspeed)
			if(keyboard.is_pressed('f') and (bspeed > -2.0)):
				bspeed-=0.1
				time.sleep(0.5)
			elif(keyboard.is_pressed('e') and (bspeed < -0.3)):
				bspeed +=0.1
				time.sleep(0.5)
			print(bspeed)
			#print("Back Arrow")
		while(keyboard.is_pressed('left arrow')):
			fspeed = 0.5
			bspeed = -0.5
			mymotor1.set_output(fspeed)
			mymotor2.set_output(bspeed)
			print("Left Arrow")
		while(keyboard.is_pressed('right arrow')):
			fspeed = 0.5
			bspeed = -0.5
			mymotor1.set_output(bspeed)
			mymotor2.set_output(fspeed)
			print("Right Arrow")
		if keyboard.is_pressed('esc'):
			GPIO.cleanup()
			break
	print("Safety Lock ON")
	
	GPIO.output(37,1)
	GPIO.output(38,1)
	fspeed = 0.5
	bspeed =-0.5
	mymotor1.set_output(0, brake = True)
	mymotor2.set_output(0, brake = True)
while True:
	keyboardControl()
	
print('Done.')

del mymotor1
del mymotor2
   
