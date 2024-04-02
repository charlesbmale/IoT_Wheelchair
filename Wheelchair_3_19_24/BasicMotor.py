import time
from gpiozero_extended import Motor

tstop = 4

mymotor = Motor(enable1 = 16, pwm1 = 17, pwm2 = 18)
mymotor1 = Motor(enable1 = 6, pwm1 = 14, pwm2 = 15)

tcurr = 0
tstart = time.perf_counter()

while tcurr<= tstop:
	tcurr = time.perf_counter() - tstart
	
	mymotor.set_output(0.9 )
	mymotor1.set_output(-0.9)
print('Done')

mymotor.set_output(0,brake = True)
mymotor1.set_output(0,brake = True)
del mymotor
