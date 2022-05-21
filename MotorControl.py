import wiringpi

IN1 = 15
IN2 = 16
IN3 = 1
IN4 = 4

IN5 = 5
IN6 = 6
IN7 = 10
IN8 = 11

OUTPUT = 1

caseMap = [
	[0,0,0,1],
	[0,0,1,1],
	[0,0,1,0],
	[0,1,1,0],
	[0,1,0,0],
	[1,1,0,0],
	[1,0,0,0],
	[1,0,0,1]
]

Steps1 = 0
Direction1 = True
Steps2 = 0
Direction2 = True

def setup():
	# Serial.begin(9600)
	wiringpi.wiringPiSetupGpio()
	
	wiringpi.pinMode(IN1, OUTPUT)
	wiringpi.pinMode(IN2, OUTPUT)
	wiringpi.pinMode(IN3, OUTPUT)
	wiringpi.pinMode(IN4, OUTPUT)
	
	wiringpi.pinMode(IN5, OUTPUT)
	wiringpi.pinMode(IN6, OUTPUT)
	wiringpi.pinMode(IN7, OUTPUT)
	wiringpi.pinMode(IN8, OUTPUT)


def loop():
	for i in range(4096):
		stepper1(1)
		delayMicroseconds(800)
	
	Direction1 = not Direction1
	for i in range(4096):
		stepper1(1)
		delayMicroseconds(800)
	
	
	for i in range(4096):
		stepper2(1)
		delayMicroseconds(800)
	
	Direction2 = not Direction2
	for i in range(4096):
		stepper2(1)
		delayMicroseconds(800)
	

def stepper1(xw):
	for x in range(xw):
		wiringpi.digitalWrite(IN1, caseMap[Steps1][0])
		wiringpi.digitalWrite(IN2, caseMap[Steps1][1])
		wiringpi.digitalWrite(IN3, caseMap[Steps1][2])
		wiringpi.digitalWrite(IN4, caseMap[Steps1][3])
		StepOne1()
	

def stepper2(xw):
	for x in range(xw):
		wiringpi.digitalWrite(IN5, caseMap[Steps1][0])
		wiringpi.digitalWrite(IN6, caseMap[Steps1][1])
		wiringpi.digitalWrite(IN7, caseMap[Steps1][2])
		wiringpi.digitalWrite(IN8, caseMap[Steps1][3])
		StepOne2()


def StepOne1():
	if Direction1:
		Steps1 += 1
	else:
		Steps1 -= 1
	
	if Steps1 > 7:
		Steps1 = 0
	
	if Steps1 < 0:
		Steps1 = 7


def StepOne2():
	if Direction2:
		Steps2 += 1
	else:
		Steps2 -= 1
	
	if Steps2 > 7:
		Steps2 = 0
	
	if Steps2 < 0:
		Steps2 = 7
	


def main():
	if wiringpi.wiringPiSetup() == -1:
		# if the wiringPi initialization fails, print error message
		print("setup wiringPi failed !")
		return 1
	
	setup()
	loop()
	return 0
