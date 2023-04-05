from vector import Vec3
from PIL import Image as PILImage


class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[Vec3(0, 0, 0) for _ in range(width)]
                       for _ in range(height)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def write_ppm(self, filename):
        RGB_string = "\n".join([" ".join(
            [" ".join(map(lambda k: str(round(min(255, max(0, k*255)))),
                          [j.x, j.y, j.z])) for j in i]) for i in self.pixels])

        content = f'''
P3 {self.width} {self.height}

255

{RGB_string}
        '''

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(content)

    def write_jpg(self, filename):
        image = PILImage.new("RGB", (self.width, self.height))

        for y in range(self.height):
            for x in range(self.width):
                color = self.pixels[y][x]
                image.putpixel((x, y), tuple(map(lambda k: round(
                    min(255, max(0, k*255))), [color.x, color.y, color.z])))

        image.save(filename)
