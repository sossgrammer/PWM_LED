import board
import time
from rainbowio import colorwheel
import neopixel

np = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write = False, brightness=0.5)

color = [255,0,0]
decrement = 0
increment = 1
count = 0

while True:
    np.fill(color)
    np.show()
    time.sleep(0.01)
    if count == 255:
        decrement = (decrement + 1) % 3
        increment = (increment + 1) % 3
    else:
        color[decrement] -= 1
        color[increment] += 1
    count = (count + 1) % 256
