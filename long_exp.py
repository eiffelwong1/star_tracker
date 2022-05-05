from picamera import PiCamera
import time
import datetime
import time
import numpy as np
from PIL import Image as im


x_pix, y_pix = 1280, 720

with PiCamera( resolution=(x_pix, y_pix), framerate=1/6, sensor_mode=3 ) as camera:

    # You can change these as needed. Six seconds (6000000)
    # is the max for shutter speed and 800 is the max for ISO.
    camera.shutter_speed = 1000000
    camera.iso = 100
    camera.exposure_mode = 'off'
    #camera.start_preview()
    time.sleep(2)
    image = np.empty( (y_pix,x_pix,3), dtype=np.uint8 )
    print("imaging start")
    t_start = time.time()
    #image = image.reshape( (720,1280,3) )
    for i, image in enumerate( camera.capture_continuous(image, "rgb") ):
        save_image = im.fromarray(image)
        save_image.save(f"./imgs/{i}.jpg")

        print(f"image{i}; elapsed: {time.time() - t_start}" )
        t_start = time.time()
        break
    print("imaging ends")



