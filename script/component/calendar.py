from shared import variables as var
from PIL import Image, ImageDraw


def draw():
    card_size = (210, 200)
    image = Image.new('1', card_size, 255)
    image_draw = ImageDraw.Draw(image)

    image_draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), width=var.card_line_width, radius=var.card_radius, fill=None)

    image_draw.text((16, 16), 'MARS', font=var.font_medium, fill=0, anchor="la")
    image_draw.text((card_size[0] - 16, card_size[1] - 16), 'DIMANCHE', font=var.font_medium, fill=0, anchor="rs")

    text_center = (card_size[0] / 2, card_size[1] / 2)
    image_draw.text(text_center, '24', font=var.font_extra_large, fill=0, anchor="mm")

    return image