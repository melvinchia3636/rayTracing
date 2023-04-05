import math


class Vec3:
    """3D vector class
    """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def mag(self):
        """Return the magnitude of the vector
        """
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self):
        """Return a normalized version of the vector

        Normalized means that the magnitude of the vector is 1

        Returns:
            Vec3: The normalized vector
        """
        mag = self.mag()
        return Vec3(self.x / mag, self.y / mag, self.z / mag)

    def dot(self, other):
        """Return the dot product of the vector and another vector

        Args:
            other (Vec3): The other vector

        Returns:
            Vec3: The dot product
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __repr__(self):
        return "Vec3({:.3f}, {:.3f}, {:.3f})".format(self.x, self.y, self.z)

    def __str__(self):
        return "{:.3f} {:.3f} {:.3f}".format(self.x, self.y, self.z)

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
