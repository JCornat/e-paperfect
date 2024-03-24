import os
from PIL import ImageFont

images_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'assets', 'images')
fonts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'assets', 'fonts')

card_line_width = 1
card_radius = 8
margin = 20

font_extra_large = ImageFont.truetype(os.path.join(fonts_dir, 'Font.ttc'), 80)
font_medium = ImageFont.truetype(os.path.join(fonts_dir, 'Font.ttc'), 24)

font_small = ImageFont.truetype(os.path.join(fonts_dir, 'Font.ttc'), 20)
font_small_height = 16

font_extra_small = ImageFont.truetype(os.path.join(fonts_dir, 'Font.ttc'), 14)
font_extra_small_height = 16

