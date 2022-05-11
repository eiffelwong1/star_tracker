# star_tracker
a smart Alt-Az type star tracker

## documents

idea ppt: https://docs.google.com/presentation/d/1V09LMWxtM6EQ7cZHFbPJ3HRUoUjyuCmjtu40eXvP8dM/edit?usp=sharing  
Project Overview: https://docs.google.com/document/d/1-RgK3QuJ4uykZ0ImFwVufxx7JOQnr-Ly_n8QABVvBu4/edit?usp=sharing  
H/W handwritten notes: see `3d_print_file/hardware_combinded_handwritten_notes.pdf`

## Hardware

3D Printing requirements:
File: f3d ->3mf
Max Size: 200mm^3

documentation: https://docs.google.com/document/d/1L_Es6k-k7RpyGgrmrHhm6hPq1YzO1r2z4-Yxdts5CSU/edit?usp=sharing  
pi camera spec: https://www.raspberrypi.com/documentation/accessories/camera.html  
worm gear: https://www.thingiverse.com/thing:4458332  

### all amazon link for purchase

1/4" to 1/4" screw: https://www.amazon.com/SmallRig-Double-Head-Stud-Microphone/dp/B007LTH1X2  
bearings: https://www.amazon.com/BESIY-Skateboards-Longboards-Miniature-ABEC%EF%BC%88Pack/dp/B07S1B3MS6  
stepper motors: https://www.amazon.com/ELEGOO-28BYJ-48-ULN2003-Stepper-Arduino/dp/B01CP18J4A  

*gyroscope

## Software

pi4 gadget mode: https://howchoo.com/pi/raspberry-pi-gadget-mode#flash-raspberry-pi-os-onto-your-sd-card

connect pi4 via: `ssh -X pi@raspberrypi.local` (-X for enabling X11 server)

plate solving:

astronet API (internet needed): https://astroquery.readthedocs.io/en/latest/astrometry_net/astrometry_net.html  
unknown (needs internet): https://github.com/tkarabela/platesolve-polar-align/blob/master/platesolve-polar-align.ipynb  
all github plte solve topics: https://github.com/topics/plate-solving  

# Papers

https://link.springer.com/content/pdf/10.1023/A:1016391518972.pdf

Star Shape  
https://www.spiedigitallibrary.org/conference-proceedings-of-spie/8451/84512K/The-improvement-of-CCD-auto-guiding-system-for-25m-telescope/10.1117/12.925642.full?SSO=1

https://www.spiedigitallibrary.org/journals/optical-engineering/volume-33/issue-8/0000/Description-and-analysis-of-an-algorithm-for-star-identification-pointing/10.1117/12.173587.full

https://aip.scitation.org/doi/pdf/10.1063/1.1715829

historical  
https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1948ApJ...107...73B&defaultprint=YES&filetype=.pdf

cite this astropi
https://www.astropy.org/acknowledging.html
