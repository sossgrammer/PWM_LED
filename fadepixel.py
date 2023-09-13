import board
import time
import neopixel


np = neopixel.NeoPixel(board.D2, 30, auto_write = True, brightness=0.5)



color = [255, 0, 255]
color_rgb = [color[0],color[1],color[2]]
np.fill(color_rgb)


def fade_in(color, delay = 0.01):
    red_fade = color[0]/256.0
    green_fade = color[1]/256.0
    blue_fade = color[2]/256.0
    for i in range(256):
        color_rgb[0] = int (color[0] - (red_fade*i))
        color_rgb[1] = int (color[1] - (green_fade*i))
        color_rgb[2] = int (color[2] - (blue_fade*i))
        np.fill(color_rgb)
        print(i, color,red_fade*i,green_fade*i,blue_fade*i)
        time.sleep(0.01)
        
def fade_out(color, delay = 0.01):
    red_fade = color[0]/256.0
    green_fade = color[1]/256.0
    blue_fade = color[2]/256.0
    for i in range(256):
        color_rgb[0] = int (red_fade*i)
        color_rgb[1] = int (green_fade*i)
        color_rgb[2] = int (blue_fade*i)
        np.fill(color_rgb)
        print(i, color,red_fade*i,green_fade*i,blue_fade*i)
        time.sleep(0.01)
    
while True:
    fade_in(color)
    fade_out([0,255,255],0.05)
    fade_in([0,255,255],0.05)
    fade_out(color)
    
