#!/usr/bin/python
# coding: utf-8

try:
    from sense_hat import SenseHat
    sense = SenseHat()
except:
    from sense_emu import SenseHat
    sense = SenseHat()


import time

#sense = SenseHat()
sense.clear()

depx = 1
depy = 1
x = 7
y = 3
z = 0

balle = (255, 255, 255)
noir = (0, 0, 0)
raquette = (0, 0, 255)

#affiche un point
sense.set_pixel(x, y, balle)

#affichage raquette
sense.set_pixel(0, z+0, raquette)
sense.set_pixel(0, z+1, raquette)
sense.set_pixel(0, z+2, raquette)

#déplacement du point vers coin inférieur droit
while 1:

  sense.set_pixel(x, y, noir)

  x -= depx
  if x == 0 or x == 7:
    depx *= -1
  y -= depy
  if y == 0 or y == 7:
    depy *= -1
  
  sense.set_pixel(x, y, balle)
  time.sleep(0.2)