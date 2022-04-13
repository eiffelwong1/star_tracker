from PIL import Image, ImageChops
import glob
import numpy as np

imgs = glob.glob("./*.jpg")

if len(imgs) > 0:
    final_img = Image.open( imgs[0] ) 
    for img in imgs:
        final_img = ImageChops.lighter( final_img, Image.open( img ) )
        

    final_img.save("final.jpg")
    
