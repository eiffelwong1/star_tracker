#include <stdio.h>
#include <wiringPi.h>

#define IN1 15
#define IN2 16
#define IN3 1
#define IN4 4

#define IN5 5
#define IN6 6
#define IN7 10
#define IN8 11

int Steps1 = 0;
int Direction1 = 1;
int Steps2 = 0;
int Direction2 = 1;

void setup() {
	//Serial.begin(9600);
	pinMode(IN1, OUTPUT);
	pinMode(IN2, OUTPUT);
	pinMode(IN3, OUTPUT);
	pinMode(IN4, OUTPUT);
	
	pinMode(IN5, OUTPUT);
	pinMode(IN6, OUTPUT);
	pinMode(IN7, OUTPUT);
	pinMode(IN8, OUTPUT);
}

void loop() {
	for(int i=0; i<4096; i++){
		stepper1(1);
		delayMicroseconds(800);
	}
	Direction1 = !Direction1;
	for(int i=0; i<4096; i++){
		stepper1(1);
		delayMicroseconds(800);
	}
	
	for(int i=0; i<4096; i++){
		stepper2(1);
		delayMicroseconds(800);
	}
	Direction2 = !Direction2;
	for(int i=0; i<4096; i++){
		stepper2(1);
		delayMicroseconds(800);
	}
}

void stepper1(int xw) {
	for (int x = 0; x < xw; x++) {
		switch (Steps1) {
			case 0:
				digitalWrite(IN1, LOW);
				digitalWrite(IN2, LOW);
				digitalWrite(IN3, LOW);
				digitalWrite(IN4, HIGH);
				break;
			case 1:
				digitalWrite(IN1, LOW);
				digitalWrite(IN2, LOW);
				digitalWrite(IN3, HIGH);
				digitalWrite(IN4, HIGH);
				break;
			case 2:
				digitalWrite(IN1, LOW);
				digitalWrite(IN2, LOW);
				digitalWrite(IN3, HIGH);
				digitalWrite(IN4, LOW);
				break;
			case 3:
				digitalWrite(IN1, LOW);
				digitalWrite(IN2, HIGH);
				digitalWrite(IN3, HIGH);
				digitalWrite(IN4, LOW);
				break;
			case 4:
				digitalWrite(IN1, LOW);
				digitalWrite(IN2, HIGH);
				digitalWrite(IN3, LOW);
				digitalWrite(IN4, LOW);
				break;
			case 5:
				digitalWrite(IN1, HIGH);
				digitalWrite(IN2, HIGH);
				digitalWrite(IN3, LOW);
				digitalWrite(IN4, LOW);
				break;
			case 6:
				digitalWrite(IN1, HIGH);
				digitalWrite(IN2, LOW);
				digitalWrite(IN3, LOW);
				digitalWrite(IN4, LOW);
				break;
			case 7:
				digitalWrite(IN1, HIGH);
				digitalWrite(IN2, LOW);
				digitalWrite(IN3, LOW);
				digitalWrite(IN4, HIGH);
				break;
			default:
				digitalWrite(IN1, LOW);
				digitalWrite(IN2, LOW);
				digitalWrite(IN3, LOW);
				digitalWrite(IN4, LOW);
				break;
		}
		StepOne1();
	}
}

void stepper2(int xw) {
	for (int x = 0; x < xw; x++) {
		switch (Steps2) {
			case 0:
				digitalWrite(IN5, LOW);
				digitalWrite(IN6, LOW);
				digitalWrite(IN7, LOW);
				digitalWrite(IN8, HIGH);
				break;
			case 1:
				digitalWrite(IN5, LOW);
				digitalWrite(IN6, LOW);
				digitalWrite(IN7, HIGH);
				digitalWrite(IN8, HIGH);
				break;
			case 2:
				digitalWrite(IN5, LOW);
				digitalWrite(IN6, LOW);
				digitalWrite(IN7, HIGH);
				digitalWrite(IN8, LOW);
				break;
			case 3:
				digitalWrite(IN5, LOW);
				digitalWrite(IN6, HIGH);
				digitalWrite(IN7, HIGH);
				digitalWrite(IN8, LOW);
				break;
			case 4:
				digitalWrite(IN5, LOW);
				digitalWrite(IN6, HIGH);
				digitalWrite(IN7, LOW);
				digitalWrite(IN8, LOW);
				break;
			case 5:
				digitalWrite(IN5, HIGH);
				digitalWrite(IN6, HIGH);
				digitalWrite(IN7, LOW);
				digitalWrite(IN8, LOW);
				break;
			case 6:
				digitalWrite(IN5, HIGH);
				digitalWrite(IN6, LOW);
				digitalWrite(IN7, LOW);
				digitalWrite(IN8, LOW);
				break;
			case 7:
				digitalWrite(IN5, HIGH);
				digitalWrite(IN6, LOW);
				digitalWrite(IN7, LOW);
				digitalWrite(IN8, HIGH);
				break;
			default:
				digitalWrite(IN5, LOW);
				digitalWrite(IN6, LOW);
				digitalWrite(IN7, LOW);
				digitalWrite(IN8, LOW);
				break;
		}
		StepOne2();
	}
}

void StepOne1() {
	if (Direction1 == 1) {
		Steps1++;
	}
	if (Direction1 == 0) {
		Steps1--;
	}
	if (Steps1 > 7) {
		Steps1 = 0;
	}
	if (Steps1 < 0) {
		Steps1 = 7;
	}
}

void StepOne2() {
	if (Direction2 == 1) {
		Steps2++;
	}
	if (Direction2 == 0) {
		Steps2--;
	}
	if (Steps2 > 7) {
		Steps2 = 0;
	}
	if (Steps2 < 0) {
		Steps2 = 7;
	}
}

int main(void)
{
	if(wiringPiSetup() == -1){
		//if the wiringPi initialization fails, print error message
		printf("setup wiringPi failed !");
		return 1;
	}
	setup();
	loop();
	return 0;
}
