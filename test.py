from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = auto()
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))

draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 22)

draw.text((10, 10), "Hello World", inky_display.BLACK, font)