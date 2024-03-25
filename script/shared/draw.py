from shared import utils, variables as var
from PIL import Image, ImageDraw
import time
import logging
from lib import epdfake

epd = None
image_black = None
image_red = None


def init(lines):
    global epd
    global image_black, image_red

    # Initialize EPDFake for development environment
    epd = epdfake.EPD(800, 480)

    try:
        # Try load the e-ink display library
        from lib import epd7in5b_V2
        epd = epd7in5b_V2.EPD()

    except RuntimeError as e:
        # If the library is not found, then continue in development mode
        logging.error(e)

    epd.init()
    epd.Clear()

    # Set the screen size in portrait mode
    var.screen_height = epd.width
    var.screen_width = epd.height

    # Generate black and red images
    image_black = Image.new("1", (epd.height, epd.width), 255)
    image_red = Image.new("1", (epd.height, epd.width), 255)

    # Draw the screen
    draw_screen(lines)
    show_image()

    epd.init()
    epd.Clear()
    epd.sleep()


def show_image():
    global epd
    if hasattr(epd, "fake"):
        utils.save_image(image_black, "output.png")
    else:
        epd.display(epd.getbuffer(image_black), epd.getbuffer(image_red))
        epd.sleep()
        time.sleep(180)


def draw_screen(lines):
    y = var.margin
    for line in lines:
        dimension = draw_line(line, y)
        y += dimension["height"] + var.margin


def draw_line(line, y):
    left_margin = int(var.margin / 2)
    height = 0
    for component in line["components"]:
        dimension = draw_component(component["component"], component["col"], left_margin, y)
        left_margin += dimension["width"] + var.margin
        height = max(height, dimension["height"])

    return {
        "height": height
    }


def draw_component(component, col, left_margin, y):
    global image_black
    image_component = component.draw(width=utils.col_width(col))
    image_black.paste(image_component, (left_margin, y))

    return {
        "width": image_component.width,
        "height": image_component.height,
    }
