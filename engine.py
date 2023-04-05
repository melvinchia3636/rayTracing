from image import Image
from point import Point
from ray import Ray
from color import Color
from progress.bar import Bar


class RenderEngine:
    def render(self, scene):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height
        x0 = -1.0
        x1 = +1.0
        x_step = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        y_step = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        with Bar("Rendering", max=height*width) as bar:
            for j in range(height):
                y = y0 + j * y_step
                for i in range(width):
                    x = x0 + i * x_step
                    ray = Ray(camera, Point(x, y) - camera)
                    pixels.set_pixel(i, j, self.ray_trace(ray, scene))
                    bar.next()

        return pixels

    def ray_trace(self, ray, scene):
        color = Color(0, 0, 0)

        dist_hit, object_hit = self.find_nearest_intersection(ray, scene)
        if object_hit is None:
            return color
        hit_pos = ray.origin + ray.direction * dist_hit
        hit_normal = object_hit.normal_at(hit_pos)
        color += self.color_at(object_hit, hit_pos, hit_normal, scene)
        return color

    def find_nearest_intersection(self, ray, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (dist_min is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj
        return dist_min, obj_hit

    def color_at(self, object_hit, hit_pos, normal, scene):
        material = object_hit.material
        obj_color = material.color_at(hit_pos)
        to_camera = scene.camera - hit_pos
        specular_k = 50
        color = material.ambient * Color.from_hex("#000000")
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)

            # Diffuse shading: Lambertian reflection
            color += material.diffuse * obj_color * \
                max(normal.dot(to_light.direction), 0)

            # Specular shading: Blinn-Phong reflection model
            half_vector = (to_light.direction + to_camera).normalize()
            color += material.specular * light.color * \
                max(normal.dot(half_vector), 0) ** specular_k

            return color
