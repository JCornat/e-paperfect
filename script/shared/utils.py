import os

from PIL import Image, ImageFont
from shared import variables as var

def font(size="base", weight="Regular", family="PTSans", italic=False):
    if italic:
        if weight == "Regular":
            file_name = f"{family}-Italic.ttf"
        else:
            file_name = f"{family}-{weight}Italic.ttf"
    else:
        file_name = f"{family}-{weight}.ttf"

    if size == "xs":
        size_int = 12
    elif size == "sm":
        size_int = 14
    elif size == "base":
        size_int = 16
    elif size == "lg":
        size_int = 20
    elif size == "xl":
        size_int = 24
    elif size == "2xl":
        size_int = 34
    elif size == "3xl":
        size_int = 64
    elif size == "4xl":
        size_int = 72
    elif size == "5xl":
        size_int = 110
    else:
        size_int = 20

    return ImageFont.truetype(os.path.join(var.fonts_dir, file_name), size_int)


def import_image(image_name, size):
    image = Image.open(os.path.join(var.images_dir, image_name))
    new_image = Image.new("RGBA", image.size, "WHITE")
    new_image.paste(image, (0, 0), image)
    return new_image.resize(size)


def save_image(image, name):
    image.save(os.path.join(var.images_dir, name))


# Calculate the width of an element based on 12 columns
def col_width(number):
    return int(((var.screen_width - var.margin) / 12) * number)


# Add a semi-margin to the left and right of the image
# In order to have gap between components
def add_horizontal_margin(image):
    margin_image = Image.new("1", (image.width + var.margin, image.height), 255)
    margin_image.paste(image, (int(var.margin / 2), 0))
    return margin_image
