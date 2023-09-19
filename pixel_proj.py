import board
import time
import neopixel
import random

np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness=0.5)

color = [127,176,171]
color2 = [100,26,161]
off = [0,0,0]
color_rgb = [color[0],color[1],color[2]]
np.fill(color_rgb)

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
        time.sleep(0.01)

"""
function: fade_out
description: function will make lights fade out from being at its maximum value to completely off
parameters: color(list), delay(float)
return value: prints color values as it updates
"""
def fade_out(color, delay = 0.01):
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
function: sparkle
description: function will make lights sopradically flash at random places on neopixel LED strip
parameters: sprk_color(list), bckg_color(list), delay(float), sprk_num(int)
return value: n/a
"""
def sparkle(sprk_color, bckg_color = color, delay = 0.01, sprk_num = 10):
    for i in range(100):
        np.fill(color)
        for j in range(sprk_num):
            rand = random.randint(0, 29)
            np[rand] = sprk_color
        time.sleep(delay)
        np[rand] = bckg_color
        np.show()

"""
function: chase
description: function will create illusion of groups of lights "chasing" or following each other
parameters: parameters: color(list), delay(float)
return type: backgroud and foreground colors printed on console
"""
def chase(color = off, delay = 0.005):
    for i in range(30):
        np.show()
        for j in range(30):
            if j % 3 != 0:
                led = (j+i) % 30 
                np[led] = color2
                print("bckg. color: ",i,np[i])
            elif j % 3 == 0:
                led = (j+i) % 30
                np[led] = color
                print("frg. color: ",i,np[i])
            time.sleep(delay)

while True:
    fade_in(color)
    fade_out(color2)
    fade_in(color2)
    fade_out(color)
    sparkle(color2, color, 0.05, 5)
    chase(color)
