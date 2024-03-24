from shared import utils, variables as var
from PIL import Image, ImageDraw


def draw():
    card_size = (440, 140)
    image = Image.new('1', card_size, 255)
    image_draw = ImageDraw.Draw(image)

    image_draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), width=var.card_line_width, radius=var.card_radius, fill=None)

    image_draw.text((16, 16), 'Objectifs', font=var.font_medium, fill=0, anchor="la")

    item_size = (55, 65)
    for i in range(7):
        origin = (16 + i * item_size[0] + i * 12, card_size[1] - item_size[1] - 16)
        image_draw.rounded_rectangle((origin[0], origin[1], origin[0] + item_size[0], origin[1] + item_size[1]), width=var.card_line_width, radius=var.card_radius, fill=None)

    return image
