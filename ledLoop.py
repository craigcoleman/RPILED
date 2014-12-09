import time
import common
from random import randrange, uniform

# 
# this says, hey we have a led strip
# with 32 LED's (pixels) 
# 
leds = common.LedPixel(33)

# please turn them all off
leds.allOff()
for i in range(0,1):
	for x in xrange(0,32,1):
# then simply color things
# colors range from 0 to 255 (the size of a byte)
		random_red  = randrange(0, 255)
		random_green  = randrange(0, 255)
		random_blue  = randrange(0, 255)
		leds.colorLed(x, random_red, 	random_green,   random_blue)		# first 	is red
		leds.writeAll()
		time.sleep(0.4)
		
	time.sleep(1)
	for y in xrange(32,-1,-1):
		leds.colorLed(y, 0, 	0,   0)		# first 	is red
		leds.writeAll()
		time.sleep(0.3)	
# colors range from 0 to 255 (the size of a byte)
#for x in range(0, 3):
#    print "We're on time %d" % (x)
