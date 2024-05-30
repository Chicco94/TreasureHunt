from dataclasses import dataclass
from math import pi,sin,cos,atan2

@dataclass
class Position():
    latitude:float
    longitude:float
    hintMessage:str = ''
    infoMessage:str = ''
    distance:float = 999999999
    distanceMessage:str = ''


def deg2grad(deg):
    return deg*pi/100


def distance(p1:Position,p2:Position)->float:
    R = 6371 # Raggio medio della Terra in km
    d_lat = deg2grad(p2.latitude-p1.latitude)
    d_lon = deg2grad(p2.longitude-p1.longitude)
    a = sin(d_lat/2)*sin(d_lat/2) \
        + cos(deg2grad(p1.latitude)) * cos(deg2grad(p2.latitude)) \
        * sin(d_lon/2) * sin(d_lon/2)
    c = 2*atan2(a**0.5,(1-a)**0.5)
    return round(R*c*1000)    

