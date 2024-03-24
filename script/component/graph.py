from shared import utils, variables as var
from PIL import Image, ImageDraw


def draw():
    card_size = (440, 140)
    image = Image.new("1", card_size, 255)
    image_draw = ImageDraw.Draw(image)

    item_size = (15, 15)
    margin = 2
    for y in range(7):
        for x in range(24):
            origin = (card_size[0] - ((x + 1) * item_size[0] + (x + 1) * margin), card_size[1] - ((y + 1) * item_size[1] + (y + 1) * margin))
            image_draw.rounded_rectangle((origin[0], origin[1], origin[0] + item_size[0], origin[1] + item_size[1]), width=var.card_line_width, radius=3, fill=None)

    for i, day in enumerate(reversed(("Lun", "Mer", "Ven", "Dim"))):
        image_draw.text((0, card_size[1] - (item_size[1] + margin) - ((i * item_size[1] * 2) + (i * margin * 2))), day, font=utils.font(size="xs", italic=1), fill=0, anchor="la")

    for i, day in enumerate(reversed(("Mai", "Jun", "Jul", "Aou", "Sep", "Oct", "Nov", "Dec"))):
        image_draw.text((card_size[0] - ((i * item_size[0] * 3) + (i * margin * 3)), 0), day, font=utils.font(size="xs", italic=1), fill=0, anchor="ra")

    return image
