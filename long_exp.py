from picamera import PiCamera
import time
import datetime
import time

camera = PiCamera(framerate = 6, sensor_mode=3)

# You can change these as needed. Six seconds (6000000)
# is the max for shutter speed and 800 is the max for ISO.
camera.shutter_speed = 6000000
camera.iso = 800

time.sleep(2)
camera.exposure_mode = 'off'

print("imaging start")
t_start = time.time()
for i in range(100):
    camera.capture(f"{i}.jpg")
    print(f"image {i}; time elapsed: {time.time() - t_start}")
print("imaging ends")

camera.close()
