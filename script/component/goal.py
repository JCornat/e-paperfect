from shared import utils, variables as var
from PIL import Image, ImageDraw


def draw(width=0, height=0):
    card_size = (width - var.margin, height)
    image = Image.new("1", card_size, 255)
    image_draw = ImageDraw.Draw(image)

    list = [
        {"name": "Basson", "icon": "music_note.png"},
        {"name": "Sport", "icon": "fitness_center.png"},
        {"name": "Lecture", "icon": "book_2.png", "done": 1},
        {"name": "Etirement", "icon": "physical_therapy.png", "done": 1},
        {"name": "Travaux", "icon": "handyman.png", "done": 1},
        {"name": "Projet", "icon": "deployed_code.png", "done": 1},
        {"name": "Projet", "icon": "deployed_code.png", "done": 1},
    ]

    image_draw.text((card_size[0] - 4, 18), "OBJECTIFS", font=utils.font(size="2xl", weight="Bold"), fill=0, anchor="rb")

    item_size = (55, 65)
    for i, item in enumerate(list):
        origin = (12 + i * item_size[0] + i * 12, card_size[1] - item_size[1] - 12)
        image_draw.rounded_rectangle((origin[0], origin[1], origin[0] + item_size[0], origin[1] + item_size[1]), width=var.card_line_width, radius=var.card_radius, fill=None)
        image_draw.text((int(item_size[0] / 2) + origin[0], origin[1] + item_size[1] - 10), item["name"], font=utils.font(size="xs"), fill=0, anchor="mm")
        image.paste(utils.import_image(item["icon"], (40, 40)), (origin[0] + int(item_size[0] / 2) - 20, origin[1] + 6))

        if item.get("done"):
            image.paste(utils.import_image("done.png", (20, 20)), (origin[0] + item_size[0] - 20, origin[1] + 2))

    image_draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), width=var.card_line_width, radius=var.card_radius, fill=None)

    return utils.add_horizontal_margin(image)
