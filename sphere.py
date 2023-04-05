import math


class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        sphere_to_ray = ray.origin - self.center
        a = 1
        b = 2 * (ray.direction.dot(sphere_to_ray))
        c = sphere_to_ray.dot(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return None
        dist = (-b - math.sqrt(discriminant)) / (2 * a)
        if dist < 0:
            return None
        return dist

    def normal_at(self, hit_pos):
        return (hit_pos - self.center).normalize()
