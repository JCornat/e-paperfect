from shared import variables as var
from shared import utils
from PIL import Image, ImageDraw


def draw():
    card_size = (210, 200)
    image = Image.new("1", card_size, 255)
    image_draw = ImageDraw.Draw(image)

    image_draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), width=var.card_line_width, radius=var.card_radius, fill=None)

    image.paste(utils.import_image("sun.png", (38, 38)), (16, 18))
    image_draw.text((70, 16), "Matin", font=utils.font(size="xs", italic=1), fill=0, anchor="la")
    image_draw.text((70, 16 + 12), "10°", font=utils.font(size="base", weight="Bold"), fill=0, anchor="la")

    image.paste(utils.import_image("cloud.png", (38, 38)), (16, 67))
    image_draw.text((70, 65), "Midi", font=utils.font(size="xs", italic=1), fill=0, anchor="la")
    image_draw.text((70, 65 + 12), "14°", font=utils.font(size="base", weight="Bold"), fill=0, anchor="la")

    image.paste(utils.import_image("night.png", (38, 38)), (16, 116))
    image_draw.text((70, 114), "Soir", font=utils.font(size="xs", italic=1), fill=0, anchor="la")
    image_draw.text((70, 114 + 12), "12°", font=utils.font(size="base", weight="Bold"), fill=0, anchor="la")

    image_draw.text((card_size[0] - 16, card_size[1] - 16), "Nancy", font=utils.font(size="base"), fill=0, anchor="rs")

    return image
