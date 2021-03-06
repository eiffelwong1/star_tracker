import RPi.GPIO as GPIO
import time

baseMotorPins = (5,6,13,19)    # define pins connected to four phase ABCD of stepper motor
quarterMotorPins = (12, 25, 24, 23)    # define pins connected to four phase ABCD of stepper motor
quarterSwitch = 17
baseSwitch = 27
CCWStep = (0x01,0x02,0x04,0x08) # define power supply order for rotating anticlockwise 
CWStep = (0x08,0x04,0x02,0x01)  # define power supply order for rotating clockwise

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(quarterSwitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(baseSwitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	for pin in baseMotorPins:
		GPIO.setup(pin,GPIO.OUT)
	for pin in quarterMotorPins:
		GPIO.setup(pin,GPIO.OUT)

# as for four phase stepping motor, four steps is a cycle. the function is used to drive the stepping motor clockwise or anticlockwise to take four steps    
def moveOnePeriod(motor, direction, ms):    
    for j in range(0,4,1):      # cycle for power supply order
        for i in range(0,4,1):  # assign to each pin
            if (direction == 1):# power supply order clockwise
                GPIO.output(motor[i],((CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
            else :              # power supply order anticlockwise
                GPIO.output(motor[i],((CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
        if(ms<3):       # the delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
            ms = 3
        time.sleep(ms*0.001)    
        
# continuous rotation function, the parameter steps specifies the rotation cycles, every four steps is a cycle
def moveSteps(motor, direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(motor, direction, ms)
        
# function used to stop motor
def motorStop(motor):
    for i in range(0,4,1):
        GPIO.output(motor[i],GPIO.LOW)
            
def calibrate():
	while (True):
		moveSteps(baseMotorPins, 1,3,1)  # rotating 360 deg clockwise, a total of 2048 steps in a circle, 512 cycles
		if (GPIO.input(baseSwitch) == GPIO.HIGH):
			print ('Base limit reached')
			motorStop(baseMotorPins)
			break
	time.sleep(1)
	while (True):
		# moveSteps(quarterMotorPins, 1,3,1)  # rotating 360 deg clockwise, a total of 2048 steps in a circle, 512 cycles
		print ('simulating the quarter gear motor movement')
		if (GPIO.input(quarterSwitch) == GPIO.HIGH):
			print('Quarter limit reached')
			motorStop(quarterMotorPins)
			break


def loop():
    while True:
        moveSteps(baseMotorPins, 1,3,1)  # rotating 360 deg clockwise, a total of 2048 steps in a circle, 512 cycles
        time.sleep(0.01)

def destroy():
    GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        calibrate()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
