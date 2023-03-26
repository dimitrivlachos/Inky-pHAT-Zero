import requests

from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = auto()
inky_display.set_border(inky_display.WHITE)

'''
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(FredokaOne, 22)

message = "Test this out"

w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), message, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()
'''

def get_weather(city):
    with open('token.bin', 'rb') as f:
        token = f.read().decode('utf-8')

    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID={token}')
    r = r.json()

    print(r)
    return r


def update_display(city):
    weather = get_weather(city)
    temp = weather['main']['temp'] - 273.15
    temp = round(temp, 1)

    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(FredokaOne, 22)

    message = f"{temp}°C"

    w, h = font.getsize(message)
    x = (inky_display.WIDTH / 2) - (w / 2)
    y = (inky_display.HEIGHT / 2) - (h / 2)

    draw.text((x, y), message, inky_display.BLACK, font)

    inky_display.set_image(img)
    inky_display.show()

def display_image():
    img = Image.open('weather.png')
    inky_display.set_image(img)
    inky_display.show()

#update_display('London')