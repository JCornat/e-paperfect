from shared import utils, variables as var
from PIL import Image, ImageDraw


def draw():
    card_size = (210, 230)
    image = Image.new("1", card_size, 255)
    image_draw = ImageDraw.Draw(image)

    image_draw.text((16, 16), "A faire", font=utils.font(size="base", italic=0), fill=0, anchor="la")

    list = [
        "Acheter du pain",
        "Faire le ménage",
        "Ranger la chambre",
    ]

    y = 44
    for i, item in enumerate(list):
        image.paste(utils.import_image("check_box_outline_blank.png", (20, 20)), (16, y))
        image_draw.text((42, y), item, font=utils.font(size="sm", italic=1), fill=0, anchor="la")
        y += 25

    image_draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), width=var.card_line_width, radius=var.card_radius, fill=None)


    return image
