import unittest
import math
from raytracer.vector import Vec3


class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vec3(1, -2, -2)
        self.v2 = Vec3(3, 6, 9)

    def test_mag(self):
        self.assertEqual(self.v1.mag(), 3)
        self.assertEqual(self.v2.mag(), math.sqrt(3 * 3 + 6 * 6 + 9 * 9))

    def test_dot(self):
        self.assertEqual(self.v1.dot(self.v2), -27)

    def test_normalize(self):
        self.assertEqual(self.v1.normalize(), Vec3(1 / 3, -2 / 3, -2 / 3))
        self.assertEqual(self.v2.normalize(), Vec3(3 / math.sqrt(3 * 3 + 6 * 6 + 9 * 9),
                         6 / math.sqrt(3 * 3 + 6 * 6 + 9 * 9), 9 / math.sqrt(3 * 3 + 6 * 6 + 9 * 9)))

    def test_add(self):
        self.assertEqual(self.v1 + self.v2, Vec3(4, 4, 7))

    def test_sub(self):
        self.assertEqual(self.v1 - self.v2, Vec3(-2, -8, -11))

    def test_mul(self):
        self.assertEqual(self.v1 * 3, Vec3(3, -6, -6))
        self.assertEqual(self.v2 * 3, Vec3(9, 18, 27))

    def test_rmul(self):
        self.assertEqual(3 * self.v1, Vec3(3, -6, -6))
        self.assertEqual(3 * self.v2, Vec3(9, 18, 27))


if __name__ == "__main__":
    unittest.main()
