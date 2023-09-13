import board
import time
import neopixel
import random

np = neopixel.NeoPixel(board.D2, 30, auto_write = True, brightness=0.5)


color = [255,255,0]
color2 = [255,0,255]
off = [0,0,0]
color_rgb = [color[0],color[1],color[2]]
np.fill(color_rgb)


def fade_in(color, delay = 0.01):
    red_fade = color[0]/256.0
    green_fade = color[1]/256.0
    color2_fade = color[2]/256.0
    for i in range(256):
        color_rgb[0] = int (color[0] - (red_fade*i))
        color_rgb[1] = int (color[1] - (green_fade*i))
        color_rgb[2] = int (color[2] - (color2_fade*i))
        np.fill(color_rgb)
        print(i, color,red_fade*i,green_fade*i,color2_fade*i)
        time.sleep(0.01)
        
def fade_out(color, delay = 0.01):
    red_fade = color[0]/256.0
    green_fade = color[1]/256.0
    color2_fade = color[2]/256.0
    for i in range(256):
        color_rgb[0] = int (red_fade*i)
        color_rgb[1] = int (green_fade*i)
        color_rgb[2] = int (color2_fade*i)
        np.fill(color_rgb)
        print(i, color,red_fade*i,green_fade*i,color2_fade*i)
        time.sleep(delay)
        
def sparkle(sprk_color, bckg_color = color, delay = 0.01, sprk_num = 10):
    for i in range(100):
        np.fill(color)
        for j in range(sprk_num):
            rand = random.randint(0, 29)
            np[rand] = sprk_color
        time.sleep(delay)
        np[rand] = bckg_color    
    
while True:
    fade_in(color)
    fade_out(color2,0.05)
    fade_in(color2,0.05)
    fade_out(color)
    sparkle(color2, color, 0.05, 5)
