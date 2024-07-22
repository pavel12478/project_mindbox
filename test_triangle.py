import unittest
from area import Triangle


class TestTriangleArea(unittest.TestCase):
    def test_triangle(self):
        triangle = Triangle(5, 7, 8)
        self.assertEqual(triangle.area_triangle(), 17.32)

    def test_value_negative(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(1, 2, -3)

    def test_value_sum_sides(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(1, 2, 3)

    def test_right_triangle(self):
        triangle_1 = Triangle(3, 4, 5)
        triangle_2 = Triangle(1, 1, 1)

        self.assertTrue(triangle_1.right_triangle() == 'Треугольник прямоугольный')
        self.assertTrue(triangle_2.right_triangle() == 'Треугольник не прямоугольный')
