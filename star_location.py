from astropy.coordinates import EarthLocation,SkyCoord
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import AltAz
from datetime import datetime

observing_location = EarthLocation(lat='52.2532', lon='351.63910339111703', height=100*u.m)  
curDT = datetime.now()
observing_time = Time(curDT.strftime("%Y-%m-%d %H:%M:%S"))  
aa = AltAz(location=observing_location, obstime=observing_time)

coord = SkyCoord(ra="04h27m13s", dec="21d43m37s", frame='icrs')
print(coord.transform_to(aa))