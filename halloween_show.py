import board
import time
import neopixel
import random

np = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write = False, brightness=0.25)

red = [255,0,0]
orange = [255,65,0]
yellow = [255,100,0]
flamecol = [red,orange,yellow]

cloud = [15,15,15]
white = [255,255,255]

color = orange
color2 = [100,26,161]
green = [0,255,0]
off = [0,0,0]

color_rgb = [color[0],color[1],color[2]]
np.fill(color_rgb)

"""
function: flame
description: function will make lights flicker in a campflame-esque fashion
parameters: primary(list), bckg_color(list), sprk_num(int)
return value: n/a
"""

def flame(primary = red, bckg_color = off, sprk_num = 5):
    for i in range(200):
        np.fill(bckg_color)
        np.show()
        for j in range(sprk_num):
            rnd_color = random.choice(flamecol)
            rnd_int = random.randrange(0, 10)
            rnd_intT = random.randrange(0, 10)
            rnd_sleep = random.random()/100
            np[rnd_int] = primary
            np[rnd_intT] = orange
            np.show()
            time.sleep(rnd_sleep)
        np[rnd_int] = bckg_color
        np.show()

"""
function: lightning
description: function will make lights flash at random times, impersonating the nature of lightning
parameters: bckg_color(list), flash(list), pix_num(int)
return value: n/a
"""
def lightning(bckg_color = off, flash = white, pix_num = np.n):
    for i in range(5):
        rnd_sleep = random.random()*10
        rnd_pix = random.randrange(3,8)
        np.fill(bckg_color)
        np.show()
        time.sleep(rnd_sleep)
        for j in range(rnd_pix):
            np.fill(flash)
            np.show()
            time.sleep(0.05)
            np.fill(bckg_color)
            np.show()
            time.sleep(0.01)

"""
function: fade_in
description: function will make lights fade in from being completely off to its maximum value
parameters: color(list), delay(float)
return value: prints color values as it updates
"""
def fade_in(color, delay = 0.01):
    red_fade = color[0]/256.0
    green_fade = color[1]/256.0
    color2_fade = color[2]/256.0
    for i in range(256):
        color_rgb[0] = int (color[0] - (red_fade*i))
        color_rgb[1] = int (color[1] - (green_fade*i))
        color_rgb[2] = int (color[2] - (color2_fade*i))
        np.fill(color_rgb)
        np.show()
        print(i, color,red_fade*i,green_fade*i,color2_fade*i)
        time.sleep(0.001)

"""
function: fade_out
description: function will make lights fade out from being at its maximum value to completely off
parameters: color(list), delay(float)
return value: prints color values as it updates
"""
def fade_out(color, delay = 0.001):
    red_fade = color[0]/256.0
    green_fade = color[1]/256.0
    color2_fade = color[2]/256.0
    for i in range(256):
        color_rgb[0] = int (red_fade*i)
        color_rgb[1] = int (green_fade*i)
        color_rgb[2] = int (color2_fade*i)
        np.fill(color_rgb)
        np.show()
        print(i, color,red_fade*i,green_fade*i,color2_fade*i)
        time.sleep(delay)


"""
function: chase
description: function will create illusion of a single light moving
parameters: parameters: color(list), delay(float)
return type: backgroud and foreground colors printed on console
"""
def chase(color = off, delay = 0.01):
    for i in range(10):
        np.show()
        for j in range(10):
            if j % 10 != 0:
                led = (j+i) % 10 
                np[led] = color
                print("bckg. color: ",i,np[i])
            elif j % 10 == 0:
                led = (j+i) % 10
                np[led] = color2
                print("frg. color: ",i,np[i])
            time.sleep(delay)
            

while True:
    flame(red)
    lightning(cloud)
    for i in range(3):
        fade_in(color)
        fade_out(color2)
        fade_in(color2)
        fade_out(color)
    for i in range(10):
        chase(green)
