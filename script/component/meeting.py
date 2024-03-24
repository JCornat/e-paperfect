from PIL import Image, ImageDraw
from shared import utils, variables as var


def draw():
    card_size = (210, 230)
    image = Image.new("1", card_size, 255)
    image_draw = ImageDraw.Draw(image)

    list = [
        {
            "name": "Aujourd'hui",
            "list": [
                {"hour": "11:00", "name": "Point informatique"},
                {"hour": "14:00", "name": "Réunion 1:1"},
                {"hour": "19:00", "name": "Cinéma"},
            ]
        },
        {
            "name": "Demain",
            "list": [
                {"hour": "12:00", "name": "Dentiste"},
                {"hour": "14:00", "name": "Repas de famille"},
            ]
        },
    ]

    y = 16
    for i, item in enumerate(list):
        if i > 0:
            y += 8
            image_draw.line((70, y, card_size[0] - 70, y), fill=0)
            y += 12

        image_draw.text((16, y), item["name"], font=utils.font(size="base"), fill=0, anchor="la")
        y += 34

        for j, item2 in enumerate(item["list"]):
            image_draw.text((16, y), item2["hour"], font=utils.font(size="sm", italic=1), fill=0, anchor="lm")
            image_draw.text((60, y), item2["name"], font=utils.font(size="base", weight="Bold"), fill=0, anchor="lm")
            y += 21

    image_draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), width=var.card_line_width, radius=var.card_radius, fill=None)

    return image
