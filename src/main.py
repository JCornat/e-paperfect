import os
from PIL import Image, ImageDraw, ImageFont

screen_width = 800
screen_height = 480
images_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets', 'images')
fonts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets', 'fonts')
# image = Image.open(os.path.join(images_dir, "frieren-p.bmp"))
# print(image.format, image.size, image.mode)

font_extra_large = ImageFont.truetype(os.path.join(fonts_dir, 'Font.ttc'), 80)
font_medium = ImageFont.truetype(os.path.join(fonts_dir, 'Font.ttc'), 24)

font_small = ImageFont.truetype(os.path.join(fonts_dir, 'Font.ttc'), 20)
font_small_height = 16

font_extra_small = ImageFont.truetype(os.path.join(fonts_dir, 'Font.ttc'), 14)
font_extra_small_height = 16

Himage = Image.new('1', (screen_height, screen_width), 255)  # 255: clear the frame
draw_Himage = ImageDraw.Draw(Himage)

margin = 20
card_radius = 8
card_line_width = 1


def import_image(image_name, size):
    image = Image.open(os.path.join(images_dir, image_name))
    new_image = Image.new("RGBA", image.size, "WHITE")
    new_image.paste(image, (0, 0), image)
    return new_image.resize(size)


def date_card():
    card_size = (210, 200)
    origin = (margin, margin)

    draw_Himage.rounded_rectangle((origin[0], origin[1], origin[0] + card_size[0], origin[1] + card_size[1]), width=card_line_width, radius=card_radius, fill=None)

    draw_Himage.text((origin[0] + 16, origin[1] + 16), 'MARS', font=font_medium, fill=0, anchor="la")
    draw_Himage.text((origin[0] + card_size[0] - 16, origin[1] + card_size[1] - 16), 'DIMANCHE', font=font_medium, fill=0, anchor="rs")

    text_center = (origin[0] + card_size[0] / 2, origin[1] + card_size[1] / 2)
    draw_Himage.text(text_center, '24', font=font_extra_large, fill=0, anchor="mm")


def weather_card():
    card_size = (210, 200)
    origin = (margin + 210 + margin, margin)

    draw_Himage.rounded_rectangle((origin[0], origin[1], origin[0] + card_size[0], origin[1] + card_size[1]), width=card_line_width, radius=card_radius, fill=None)

    sun = import_image("sun.png", (38, 38))
    Himage.paste(sun, (origin[0] + 16, origin[1] + 18))
    draw_Himage.text((origin[0] + 70, origin[1] + 16), 'Matin', font=font_extra_small, fill=0, anchor="la")
    draw_Himage.text((origin[0] + 70, origin[1] + 16 + font_extra_small_height), '10°', font=font_small, fill=0, anchor="la")

    cloud = import_image("cloud.png", (38, 38))
    Himage.paste(cloud, (origin[0] + 16, origin[1] + 67))
    draw_Himage.text((origin[0] + 70, origin[1] + 65), 'Midi', font=font_extra_small, fill=0, anchor="la")
    draw_Himage.text((origin[0] + 70, origin[1] + 65 + font_extra_small_height), '14°', font=font_small, fill=0, anchor="la")

    night = import_image("night.png", (38, 38))
    Himage.paste(night, (origin[0] + 16, origin[1] + 116))
    draw_Himage.text((origin[0] + 70, origin[1] + 114), 'Soir', font=font_extra_small, fill=0, anchor="la")
    draw_Himage.text((origin[0] + 70, origin[1] + 114 + font_extra_small_height), '12°', font=font_small, fill=0, anchor="la")

    draw_Himage.text((origin[0] + card_size[0] - 16, origin[1] + card_size[1] - 16), 'Nancy', font=font_medium, fill=0, anchor="rs")


date_card()
weather_card()

# draw_Himage.line((20, 50, 70, 100), fill=0)
# Other = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
Himage.save(os.path.join(images_dir, "output.png"))
