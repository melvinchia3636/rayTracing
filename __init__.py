from image import Image
from vector import Vec3
from sphere import Sphere
from scene import Scene
from color import Color
from engine import RenderEngine
from light import Light
from point import Point
from material import Material

WIDTH = 320
HEIGHT = 200
camera = Vec3(0, 0, -1)
objects = [
    Sphere(Point(0, 0, 0), 0.5, Material(Color.from_hex("#ff0000"))),
    Sphere(Point(1, -0.5, 1), 0.5, Material(Color.from_hex("#ffff00"))),
    Sphere(Point(-1, 0.2, 1), 0.5, Material(Color.from_hex("#00ff00")))
]
lights = [Light(Point(1.5, -5.5, -10.0), Color.from_hex("#ffffff"))]
scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
engine = RenderEngine()
image = engine.render(scene)

image.write_jpg("output.jpg")
