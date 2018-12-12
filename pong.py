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
sense.clear();

raquette=[0,0,255]
balle=(255,255,255)
noir=(0,0,0)
rouge=(255, 0, 0)
depx=1
depy=1
x = 7
y = 3
z=0

# affichage raquette bleu au bord (x, y, r, g, b)
def depraquette(lz):
    if lz < z:
        sense.set_pixel(0, lz+0, noir)
    else:
        sense.set_pixel(0, lz+2, noir)
    sense.set_pixel(0, z+0, raquette)
    sense.set_pixel(0, z+1, raquette)
    sense.set_pixel(0, z+2, raquette)
depraquette(0)

#deplace la raquette vers le haut
def joyup():
    global z
    lz = z    
    if z < 5:
        z += 1
    depraquette(lz)

#deplace la raquette vers le bas
def joydown():
    global z
    lz = z
    if z > 0:
        z -= 1
    depraquette(lz)

#positionne des evt sur le joystick
sense.stick.direction_up = joydown
sense.stick.direction_down = joyup

# affichage balle blanche au centre (x, y, r, g, b)
sense.set_pixel(x, y, balle)

def countdown():
	while n > 0:
		n = n - 1
		if n ==0:
			sense.show_message(n, text_colour=[0, 255, 0]) 

while 1:
    if x == 0:
        if (y < z or y>z+2):
            sense.set_pixel(x, y, 255, 0, 0)
            sense.show_message('Perdu', text_colour=[255, 0, 0])
            countdown()
            break
        else:
            sense.set_pixel(x, y, raquette)
    else:    
        sense.set_pixel(x, y, noir)    
    x -= depx
    if (x == 1 and y+1 >= z and y+1 <= z+2) or x == 7:
        depx *= -1
    y -= depy
    if y == 0 or y == 7:
        depy *= -1
    sense.set_pixel(x, y, balle)
    time.sleep(1.2)




# countdown(5) 
