import os
from PIL import Image, ImageDraw, ImageFont

imagesDir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets', 'images')
im = Image.open(os.path.join(imagesDir, "frieren-p.bmp"))
print(im.format, im.size, im.mode)
im.save(os.path.join(imagesDir, "frieren-p.png"))
