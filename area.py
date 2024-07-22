import math


# Класс для представления круга
class Circle:
    # Создает объект круга
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError()
        self.radius = radius

    # вычисление площадь круга
    def area_circle(self):
        result = 3.14 * (self.radius ** 2)
        return result


# Класс для представления треугольника
class Triangle:
    # Создание объекта треугольника
    def __init__(self, side_1, side_2, side_3):
        if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
            raise ValueError()
        if side_1 + side_2 <= side_3 or side_1 + side_3 <= side_2 or side_2 + side_3 <= side_1:
            raise ValueError()

        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    # Вычисляет площадь треугольника по трем сторонам
    def area_triangle(self):
        half_perimetr = (self.side_1 + self.side_2 + self.side_3) / 2
        result = math.sqrt(half_perimetr * (half_perimetr - self.side_1) * (half_perimetr - self.side_2) * (
                half_perimetr - self.side_3))
        return round(result, 2)

    # Проверка на прямоугольный треугольник
    def right_triangle(self):
        side = sorted([self.side_1, self.side_2, self.side_3])
        if side[0] ** 2 + side[1] ** 2 == side[2] ** 2:
            return f'Треугольник прямоугольный'
        else:
            return f'Треугольник не прямоугольный'
