import RPi.GPIO as GPIO
import time
import keyboard

from astropy.coordinates import EarthLocation,SkyCoord
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import AltAz
from datetime import datetime


class TrackerMotor():
    def __init__(self):
        # reference object is the moon
        ref_obj_ra = '07h24m37s'
        ref_obj_dec = '+26h15m39s'

        self.cur_lat = '32.874663'
        self.cur_lon = '-117.223806'

        self.observing_location = EarthLocation(lat=self.cur_lat, lon=self.cur_lon, height=100*u.m)  
        curDT = datetime.now()
        self.observing_time = Time(curDT.strftime("%Y-%m-%d %H:%M:%S"))  
        aa = AltAz(location=self.observing_location, obstime=self.observing_time)

        coord = SkyCoord(ra=ref_obj_ra, dec=ref_obj_dec, frame='icrs')
        ref_coord = coord.transform_to(aa)

        #motor control stuff
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

        self.vert_dir = 0
        self.hori_dir = 0
        self.hori_count = 0
        self.vert_count = 0

        self.x_counter = 0
        self.y_counter = 0
        self.x_speed = 0.001
        self.y_speed = 0.001
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

    def get_mount_deg():
        ratio = 360/(4096*50)
        return self.hori_count * ratio, self.vert_count * ratio

    def set_mount_counter(hori_deg, vert_deg):
        #this is not go-to function
        ratio = (4096*50)/360
        self.hori_count = hori_deg * ratio
        self.vert_count = vert_deg * ratio

    def track_this():
        alt, az = get_mount_deg()

        target = SkyCoord(alt = alt*u.deg, az = az*u.deg, obstime = self.observing_time, frame = 'altaz', location = self.observing_location)
        target = target.icrs 
            

    def change_dir(self, event):
        #broad change
        if event.name == 'a':
            self.hori_dir = min( 1, self.hori_dir+1 )
        if event.name == 'd':
            self.hori_dir = max(-1, self.hori_dir-1 )
        if event.name == 'w':
            self.vert_dir = max(-1, self.vert_dir-1 )
        if event.name == 's':
            self.vert_dir = min( 1, self.vert_dir+1 )

        #fine change
        if event.name == 'j':
            self._hori_step(1)
        if event.name == 'l':
            self._hori_step(1)
        if event.name == 'i':
            self._vert_step(-1)
        if event.name == 'k':
            self._vert_step(1)

        if event.name == 'p':
            #comfirm it pointed to reference object
            self.set_mount_counter(ref_coord.alt.degree, ref_coord.az.degree)

        if event.name == 't':
            self.tracking = True
            self.track_this()
            

        if event.name == 'x':
            self.set_pos() # set how many steps, press enter first
        if event.name == 'v':
            self.set_speed() # set the interval between each step, press enter first
        if event.name == 'e':
            self.go = False
    
    def set_pos(self):
        input()
        print('x-distance: ')
        x = int(input())
        print('y-distance: ')
        y = int(input())
        
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
    
    def set_speed(self):
        input()
        print('x-speed: ')
        x = float(input())
        print('y-speed: ')
        y = float(input())
        
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
        self._vert_step(self.get_seq_by_direction(self.vert_dir))

    def hori_step(self):
        self._hori_step(self.get_seq_by_direction(self.hori_dir))

    def _vert_step(self, v_dir):
        x_counter += self.vert_dir
        for seq in self.get_seq_by_direction(v_dir):
            for pin in range(4):
              GPIO.output(self.top_motor_pins[pin], self.halfstep_seq[ seq ][pin])
            time.sleep(self.y_speed)

    def _hori_step(self, h_dir):
        y_counter += self.hori_dir
        for seq in self.get_seq_by_direction(h_dir):
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
    print("start, please move the mount to the close position using WASD")
    motor.end()

    motor = TrackerMotor()
    print('move to a known star using WASD, then hit "p" to calibrating the mount')

    print('use WASD to control diraction, use X then ENTER for go to, use V then ENTER for tracking, use E for exit.')
    print('Have fun!')
    
    while(motor.go):
        if motor.x_counter == 0:
            motor.hori_dir = 0
        if motor.y_counter == 0:
            motor.vert_dir = 0
        motor.x_counter -= 1
        motor.y_counter -= 1
        
        print(motor.hori_dir, motor.hori_count, motor.vert_dir, motor.vert_count)
        motor.hori_step()
        motor.vert_step()
        time.sleep(0.001)
    motor.end()



if __name__ == "__main__":
    main()
