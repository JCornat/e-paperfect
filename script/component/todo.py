from shared import utils, variables as var
from PIL import Image, ImageDraw


def draw():
    card_size = (210, 230)
    image = Image.new("1", card_size, 255)
    image_draw = ImageDraw.Draw(image)

    image_draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), width=var.card_line_width, radius=var.card_radius, fill=None)

    image_draw.text((16, 16), "A faire", font=utils.font(size="base"), fill=0, anchor="la")

    return image
