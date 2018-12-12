from sense_hat import SenseHat
import time

sense = SenseHat()
x=0
y=0
balle = (255, 255, 255)
noir = (0, 0, 0)

sense.set_pixel(x, y, balle)

while x <7 and y < 7:

  sense.clear()

  x = x+1
  y = y+1
  
  sense.set_pixel(x, y, balle)
  time.sleep(0.2)