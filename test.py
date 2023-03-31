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

def display_image(image_path):
    #img = Image.open(image_path)
    img = image_path
    inky_display.set_image(img)
    inky_display.show()

def resize_image(image_path, resolution):
    """
    Resize an image to a given resolution while maintaining aspect ratio.
    
    :param image_path: Path to the input image.
    :param resolution: Tuple containing the desired resolution in (width, height) format.
    :return: PIL.Image object with the resized image.
    """
    # Open the image file using PIL
    #image = Image.open(image_path)
    image = image_path

    # Get the original width and height of the image
    width, height = image.size

    # Get the new width and height based on the desired resolution
    new_width, new_height = resolution

    # Calculate the scaling factor based on the larger dimension
    scaling_factor = max(new_width / width, new_height / height)

    # Calculate the new width and height based on the scaling factor
    new_width = int(width * scaling_factor)
    new_height = int(height * scaling_factor)

    # Resize the image using the calculated new width and height
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

    return resized_image

#update_display('London')

def add_border(image_path, border_width):
    """
    Add a white border to the right side of an image.
    
    :param image_path: Path to the input image.
    :param border_width: Width of the border in pixels.
    :return: PIL.Image object with the bordered image.
    """
    # Open the image file using PIL
    image = Image.open(image_path)

    # Get the original width and height of the image
    width, height = image.size

    # Calculate the new width and height based on the border width
    new_width = width + border_width
    new_height = height

    # Create a new image with the larger dimensions and fill it with white
    new_image = Image.new(image.mode, (new_width, new_height), color='white')

    # Paste the original image onto the new image, leaving a white border on the right side
    new_image.paste(image, (0, 0))

    return new_image

# Call the add_border function with input image and border width
#bordered_image = add_border("weather.png", 50)

# Call the resize_image function with input image and desired resolution
#resized_image = resize_image(bordered_image, (212, 122))

#display_image(resized_image)

display_image(Image.open('Inky-PHAT-Weather-background.jpg'))