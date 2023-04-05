from color import Color


class Light:
    def __init__(self, position, color=Color.from_hex("#ffffff")):
        self.position = position
        self.color = color
