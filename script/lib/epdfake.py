# A fake EPD class in order to test the script on a computer
class EPD:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fake = 1

    def init(self):
        return

    def sleep(self):
        return

    def display(self, imageblack, imagered):
        return

    def Clear(self):
        return

