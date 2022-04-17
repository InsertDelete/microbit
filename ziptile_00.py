from microbit import *
from neopixel import NeoPixel

np = NeoPixel(pin0, 64)  # 64 LEDs controlled through pin0
np.clear()               # all LEDs off

i = 16   # LED intensity

red = i,0,0
green = 0,i,0
blue = 0,0,i
white = i//2,i//2,i//2
dim = 0,0,0

np[0] = red
np[18] = white
np[45] = green
np[63] = blue

np.show()

