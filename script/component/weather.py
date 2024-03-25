from shared import variables as var
from shared import utils
from PIL import Image, ImageDraw


def draw():
    card_size = (utils.third_width(), 170)
    image = Image.new("1", card_size, 255)
    image_draw = ImageDraw.Draw(image)

    image_draw.text((card_size[0] - 4, 18), "METEO", font=utils.font(size="2xl", weight="Bold"), fill=0, anchor="rb")

    image_draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), width=var.card_line_width, radius=var.card_radius, fill=None)

    image.paste(utils.import_image("sun.png", (38, 38)), (var.padding, 18))
    image_draw.text((70, var.padding), "Matin", font=utils.font(size="xs", italic=1), fill=0, anchor="la")
    image_draw.text((70, var.padding + 12), "10°", font=utils.font(size="base", weight="Bold"), fill=0, anchor="la")

    image.paste(utils.import_image("cloud.png", (38, 38)), (var.padding, 67))
    image_draw.text((70, 65), "Midi", font=utils.font(size="xs", italic=1), fill=0, anchor="la")
    image_draw.text((70, 65 + 12), "14°", font=utils.font(size="base", weight="Bold"), fill=0, anchor="la")

    image.paste(utils.import_image("night.png", (38, 38)), (var.padding, 116))
    image_draw.text((70, 114), "Soir", font=utils.font(size="xs", italic=1), fill=0, anchor="la")
    image_draw.text((70, 114 + 12), "12°", font=utils.font(size="base", weight="Bold"), fill=0, anchor="la")

    image_draw.text((card_size[0] - var.padding, card_size[1] - var.padding), "Nancy", font=utils.font(size="base"), fill=0, anchor="rs")

    return image
