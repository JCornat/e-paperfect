from PIL import Image, ImageDraw
from component import calendar, weather, goal, graph, meeting, todo
from shared import utils, variables as var

screen_width = 800
screen_height = 480

Himage = Image.new('1', (screen_height, screen_width), 255)  # 255: clear the frame
draw_Himage = ImageDraw.Draw(Himage)

Himage.paste(calendar.draw(), (var.margin, var.margin))
Himage.paste(weather.draw(), (250, var.margin))
Himage.paste(meeting.draw(), (var.margin, 240))
Himage.paste(todo.draw(), (250, 240))
Himage.paste(goal.draw(), (var.margin, 480))
Himage.paste(graph.draw(), (var.margin, 640))

utils.save_image(Himage, "output.png")
