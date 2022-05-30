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
        self.x_counter = 0
        self.y_counter = 0
        self.x_speed = 0.001
        self.y_speed = 0.001
        self.DEFAULT_SPEED = 0.001
        self.go = True
        

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
        #print("dir changed")
        if event.name == 'a':
            self.hori_dir = min( 1, self.hori_dir+1 )
        if event.name == 'd':
            self.hori_dir = max(-1, self.hori_dir-1 )
        if event.name == 'w':
            self.vert_dir = max(-1, self.vert_dir-1 )
        if event.name == 's':
            self.vert_dir = min( 1, self.vert_dir+1 )
        if event.name == 'x':
            input()
            print('x-distance: ')
            x = float(input())
            print('y-distance: ')
            y = float(input())
            
            x = int(x / 360.0 * 4096)
            y = int(y / 360.0 * 4096)
            self.set_pos(x,y) # set how many steps, press enter first
        if event.name == 'v':
            input()
            print('x-speed: ')
            x = float(input())
            print('y-speed: ')
            y = float(input())
            self.set_speed(x,y) # set the interval between each step, press enter first
        if event.name == 'e':
            self.go = False
    
    def set_pos(self, x, y):
        if x > 0:
            self.hori_dir = 1
            self.x_counter = x
        else:
            self.hori_dir = -1
            self.x_counter = -x
            
        if y > 0:
            self.vert_dir = 1
            self.y_counter = y
        else:
            self.vert_dir = -1
            self.y_counter = -y
        self.x_speed = self.DEFAULT_SPEED
        self.y_speed = self.DEFAULT_SPEED
    
    def set_speed(self, x, y):
        if x > 0:
            self.hori_dir = 1
            self.x_speed = x
        if x < 0:
            self.hori_dir = -1
            self.x_speed = -x
        if x == 0:
            self.hori_dir = 0
            
        if y > 0:
            self.vert_dir = 1
            self.y_speed = y
        if y < 0:
            self.vert_dir = -1
            self.y_speed = -y
        if y == 0:
            self.vert_dir = 0

    def vert_step(self):
        for seq in self.get_seq_by_direction(self.vert_dir):
            for pin in range(4):
              GPIO.output(self.top_motor_pins[pin], self.halfstep_seq[ seq ][pin])
            time.sleep(self.y_speed)

    def hori_step(self):
        for seq in self.get_seq_by_direction(self.hori_dir):
            for pin in range(4):
              GPIO.output(self.base_motor_pins[pin], self.halfstep_seq[ seq ][pin])
            time.sleep(self.x_speed)

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
    print('use WASD to control diraction, use X then ENTER for go to, use V then ENTER for tracking, use E for exit.')
    print('Have fun!')
    
    while(motor.go):
        if motor.x_counter == 0:
            motor.hori_dir = 0
        if motor.y_counter == 0:
            motor.vert_dir = 0
        motor.x_counter -= 1
        motor.y_counter -= 1
        
        #print(motor.hori_dir, motor.hori_count, motor.vert_dir, motor.vert_count)
        motor.hori_step()
        motor.vert_step()
        time.sleep(motor.DEFAULT_SPEED)
    motor.end()



if __name__ == "__main__":
    main()
