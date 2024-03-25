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

    var.screen_height = epd.width
    var.screen_width = epd.height

    Himage = Image.new("1", (epd.height, epd.width), 255)  # 255: clear the frame
    Himage_Other = Image.new("1", (epd.height, epd.width), 255)  # 255: clear the frame
    draw_Himage = ImageDraw.Draw(Himage)

    y = var.margin
    calendar_image = calendar.draw()
    Himage.paste(calendar_image, (var.margin, y))

    weather_image = weather.draw()
    Himage.paste(weather_image, (utils.third_width() + var.margin * 2, y))

    weather_image2 = weather.draw()
    Himage.paste(weather_image2, (utils.third_width() * 2 + var.margin * 3, y))

    y += calendar_image.height + var.margin
    meeting_image = meeting.draw()
    Himage.paste(meeting_image, (var.margin, y))

    todo_image = todo.draw()
    Himage.paste(todo_image, (utils.half_width() + var.margin * 2, y))

    y += todo_image.height + var.margin
    goal_image = goal.draw()
    Himage.paste(goal_image, (var.margin, y))

    y += goal_image.height + var.margin
    graph_image = graph.draw()
    Himage.paste(graph_image, (var.margin, y))

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
