class Scene:
    def __init__(self, camera, objects, lights, width, height):
        self.camera = camera
        self.lights = lights
        self.objects = objects
        self.width = width
        self.height = height
