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
    left_margin = int(var.margin / 2)

    calendar_image = calendar.draw(width=utils.col_width(5))
    Himage.paste(calendar_image, (left_margin, y))

    weather_image = weather.draw(width=utils.col_width(4))
    Himage.paste(weather_image, (left_margin + calendar_image.width, y))

    weather_image2 = weather.draw(width=utils.col_width(3))
    Himage.paste(weather_image2, (left_margin + calendar_image.width + weather_image.width, y))

    y += calendar_image.height + var.margin
    meeting_image = meeting.draw(width=utils.col_width(6))
    Himage.paste(meeting_image, (left_margin, y))

    todo_image = todo.draw(width=utils.col_width(6))
    Himage.paste(todo_image, (left_margin + meeting_image.width, y))

    y += todo_image.height + var.margin
    goal_image = goal.draw(width=utils.col_width(12))
    Himage.paste(goal_image, (left_margin, y))

    y += goal_image.height + var.margin
    graph_image = graph.draw(width=utils.col_width(12))
    Himage.paste(graph_image, (left_margin, y))

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
