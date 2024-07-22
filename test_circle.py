import unittest
from area import Circle


class TestCircleArea(unittest.TestCase):
    def test_circle(self):
        circle = Circle(2)
        self.assertEqual(circle.area_circle(), 3.14 * 2 ** 2)

    def test_values(self):
        for radius in [0, -1]:
            with self.subTest(radius=radius):
                with self.assertRaises(ValueError):
                    circle = Circle(radius)
