import board
import displayio
from adafruit_st7789 import ST7789
spi = board.SPI()

tft_cs = board.D5
tft_dc = board.D6
displayio.release_displays()

disp_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(
    disp_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53
)
my_group = displayio.Group()

background = displayio.Bitmap(display.width, display.height, 1)
my_palette = displayio.Palette(1)
my_palette[0] = 0x0000
my_tg = displayio.TileGrid(background, x=0, y=0, pixel_shader=my_palette)
my_tg = displayio.TileGrid(background, x=0, y=0, pixel_shader=my_palette)
my_group.append(my_tg)
display.show(my_group)
from adafruit_display_shapes.rect import Rect

while True:
    pass
