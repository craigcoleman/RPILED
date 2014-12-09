import time

class LedPixel:
   dev = "/dev/spidev0.0"
   spidev = file(dev, "wb")

   NUM_LEDS = 32
   def __init__(self, numleds):
      self.NUM_LEDS = numleds
      #self.leds = bytearray(3 * self.NUM_LEDS)
      self.gamma = bytearray(256)
      self.buffer = [0 for x in range(self.NUM_LEDS)]
      self.wheelOffset = 0
      for led in range(self.NUM_LEDS):
          self.buffer[led] = bytearray(3)
      for i in range(256):
          # Color calculations from
          # http://learn.adafruit.com/light-painting-with-raspberry-pi
          self.gamma[i] = 0x80 | int(
              pow(float(i) / 255.0, 2.5) * 127.0 + 0.5
          )
	
   def writeAll(self):
      for x in range(self.NUM_LEDS):
          self.spidev.write(self.buffer[x])
          self.spidev.flush()
      self.spidev.write(bytearray(b'\x00'))
      self.spidev.flush()
      #self.spidev.write(self.leds)
      #self.spidev.flush()
      #self.spidev.write(bytearray(b'\x00'))
      #self.spidev.flush()

   def allOff(self):
      self.allColor(0, 0, 0)

   #NOTE: this does not write to strip
   def colorLed(self, index, r, g, b):
      self.buffer[index][0] = self.gamma[g]
      self.buffer[index][1] = self.gamma[r]
      self.buffer[index][2] = self.gamma[b]
      
   def allColor(self, r, g, b):
      for i in range(self.NUM_LEDS - 1):
         self.colorLed(i, r, g, b)
      self.writeAll() 

   def goCougs(self):
      self.allOff()
      for i in range(self.NUM_LEDS - 1):
         if i % 8 == 0:
            #self.colorLed(i, 0, 255, 0)
            self.colorLed(i, 255, 255, 255)
         else:
            self.colorLed(i, 255, 0, 2)
            #self.colorLed(i, 0, 0, 255)
         self.writeAll()
         time.sleep(.1)
      for j in range(self.NUM_LEDS - 1):
         #self.colorLed(self.NUM_LEDS - 1 - j, 0, 0, 0)
         self.colorLed(j, 0, 0, 0)
         self.writeAll()
         time.sleep(.1)
