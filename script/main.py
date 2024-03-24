from PIL import Image, ImageDraw
import logging
import time
from component import calendar, weather, goal, graph, meeting, todo
from shared import utils, variables as var
from lib import epdfake

logging.basicConfig(level=logging.DEBUG)

epd = epdfake.EPD()

try:
    from lib import epd7in5b_V2
    logging.info("epd7in5b_V2 Demo")
    epd = epd7in5b_V2.EPD()

except RuntimeError as e:
    logging.error(e)


try:
    epd.init()
    epd.Clear()

    Himage = Image.new("1", (epd.height, epd.width), 255)  # 255: clear the frame
    Himage_Other = Image.new("1", (epd.height, epd.width), 255)  # 255: clear the frame
    draw_Himage = ImageDraw.Draw(Himage)

    Himage.paste(calendar.draw(), (var.margin, var.margin))
    Himage.paste(weather.draw(), (250, var.margin))
    Himage.paste(todo.draw(), (250, 240))
    Himage.paste(goal.draw(), (var.margin, 490))
    Himage.paste(graph.draw(), (var.margin, 640))
    Himage.paste(meeting.draw(), (var.margin, 240))

    if hasattr(epd, "fake"):
        utils.save_image(Himage, "output.png")
    else:
        epd.display(epd.getbuffer(Himage), epd.getbuffer(Himage_Other))
        epd.sleep()
        time.sleep(180)

    epd.init()
    epd.Clear()
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    from lib import epd7in5b_V2
    epd7in5b_V2.epdconfig.module_exit(cleanup=True)
    exit()
