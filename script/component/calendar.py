from shared import utils, variables as var
from PIL import Image, ImageDraw


def draw(width=0, height=0):
    card_size = (width - var.margin, height)
    image = Image.new("1", card_size, 255)
    image_draw = ImageDraw.Draw(image)

    image_draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), width=var.card_line_width, radius=var.card_radius, fill=None)

    image_draw.text((var.padding, var.padding), "DIMANCHE", font=utils.font(size="base"), fill=0, anchor="la")
    image_draw.text((card_size[0] - var.padding, card_size[1] - var.padding), "MARS", font=utils.font(size="lg", weight="Bold"), fill=0, anchor="rs")

    text_center = (int(card_size[0] / 2), int(card_size[1] / 2))
    image_draw.text(text_center, "24", font=utils.font(size="5xl", weight="Bold"), fill=0, anchor="mm")

    return utils.add_horizontal_margin(image)
