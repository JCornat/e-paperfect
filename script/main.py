import logging

from component import calendar, weather, goal, graph, meeting, todo
from shared import draw

logging.basicConfig(level=logging.DEBUG)

try:
    lines = [
        {
            "height": 170,
            "components": [
                {"component": calendar, "col": 5},
                {"component": weather, "col": 7},
            ],
        },
        {
            "height": 330,
            "components": [
                {"component": meeting, "col": 6},
                {"component": todo, "col": 6},
            ],
        },
        {
            "height": 100,
            "components": [
                {"component": goal, "col": 12},
            ],
        },
        {
            "height": 140,
            "components": [
                {"component": graph, "col": 12},
            ],
        },
    ]

    draw.init(lines)

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    from lib import epd7in5b_V2
    epd7in5b_V2.epdconfig.module_exit(cleanup=True)
    exit()
