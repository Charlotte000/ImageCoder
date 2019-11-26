from random import randint
from math import sqrt
from PIL import Image


import base64
from io import BytesIO


def t2i(text, key=1234):
    if key > 8894:
        key = 8895 - key // 8895
    if key < 1000:
        key += 1000

    size = sqrt(len(text))
    if size != int(size):
        size = size + 1
    size = int(size)

    image = Image.new('RGB', (size, size), (255, 255, 255))

    pos = [0, 0]
    for letter in text:
        number = ord(letter) + key

        red = randint(0, number // 100)
        blue = number // 100 - red
        green = number % 100 + 100
        red += 100
        blue += 100

        rgb = (red, green, blue)

        image.putpixel(pos, rgb)

        pos[0] += 1
        if pos[0] >= size:
            pos[0] = 0
            pos[1] += 1
    if pos[0] == 0:
        pos[1] -= 1
    if pos[1] + 1 < size:
        image.crop((0, 0, size, size - 1))
    return image


def i2t(image, key=1234):
    if key > 8895:
        key = 8895 - key // 8895
    if key < 1000:
        key += 1000
    text = ''
    for y in range(0, image.size[0]):
        for x in range(0, image.size[1]):

            rgb = image.getpixel((x, y))

            if rgb == (255, 255, 255):
                return text

            number = (((rgb[0] - 100) + (rgb[2] - 100)) * 100 + (rgb[1] - 100)) - key
            text += chr(number)
    return text
