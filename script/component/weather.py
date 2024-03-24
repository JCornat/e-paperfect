from shared import variables as var
from shared import utils
from PIL import Image, ImageDraw


def draw():
    card_size = (210, 200)
    image = Image.new('1', card_size, 255)
    image_draw = ImageDraw.Draw(image)

    image_draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), width=var.card_line_width, radius=var.card_radius, fill=None)

    sun = utils.import_image("sun.png", (38, 38))
    image.paste(sun, (16, 18))
    image_draw.text((70, 16), 'Matin', font=var.font_extra_small, fill=0, anchor="la")
    image_draw.text((70, 16 + var.font_extra_small_height), '10°', font=var.font_small, fill=0, anchor="la")

    cloud = utils.import_image("cloud.png", (38, 38))
    image.paste(cloud, (16, 67))
    image_draw.text((70, 65), 'Midi', font=var.font_extra_small, fill=0, anchor="la")
    image_draw.text((70, 65 + var.font_extra_small_height), '14°', font=var.font_small, fill=0, anchor="la")

    night = utils.import_image("night.png", (38, 38))
    image.paste(night, (16, 116))
    image_draw.text((70, 114), 'Soir', font=var.font_extra_small, fill=0, anchor="la")
    image_draw.text((70, 114 + var.font_extra_small_height), '12°', font=var.font_small, fill=0, anchor="la")

    image_draw.text((card_size[0] - 16, card_size[1] - 16), 'Nancy', font=var.font_medium, fill=0, anchor="rs")

    return image
