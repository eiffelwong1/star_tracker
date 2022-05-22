import RPi.GPIO as GPIO
import time
import keyboard


class TrackerMotor():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.top_motor_pins = [14,15,18,23]
        self.base_motor_pins = [24,25,8,7]

        for pin in self.top_motor_pins:
          GPIO.setup(pin, GPIO.OUT)
          GPIO.output(pin, 0)
        for pin in self.base_motor_pins:
          GPIO.setup(pin, GPIO.OUT)
          GPIO.output(pin, 0)


        keyboard.on_press( self.change_dir )

        self.vert_count = 0
        self.hori_count = 0
        self.vert_dir = 0
        self.hori_dir = 0

        self.halfstep_seq = [
          [1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,1,1,0],
          [0,0,1,0],
          [0,0,1,1],
          [0,0,0,1],
          [1,0,0,1]
        ]

    def change_dir(self, event):
        print("dir changed")
        if event.name == 'a':
            self.hori_dir = min( 1, self.hori_dir+1 )
        if event.name == 'd':
            self.hori_dir = max(-1, self.hori_dir-1 )
        if event.name == 'w':
            self.vert_dir = max(-1, self.vert_dir-1 )
        if event.name == 's':
            self.vert_dir = min( 1, self.vert_dir+1 )

    def vert_step(self):
        for seq in self.get_seq_by_direction(self.vert_dir):
            for pin in range(4):
              GPIO.output(self.top_motor_pins[pin], self.halfstep_seq[ seq ][pin])
            time.sleep(0.001)

    def hori_step(self):
        for seq in self.get_seq_by_direction(self.hori_dir):
            for pin in range(4):
              GPIO.output(self.base_motor_pins[pin], self.halfstep_seq[ seq ][pin])
            time.sleep(0.001)

    def get_seq_by_direction(self, direction):
        if direction > 0:
            return range(8)
        elif direction < 0:
            return range(7,0,-1)
        else:
            return []
    
    def end(self):
        GPIO.cleanup()



def main():
    motor = TrackerMotor()
    print("start")
    for i in range(50000):
        print(motor.hori_dir, motor.hori_count, motor.vert_dir, motor.vert_count)
        motor.hori_step()
        motor.vert_step()
        time.sleep(0.001)
    motor.end()



if __name__ == "__main__":
    main()
