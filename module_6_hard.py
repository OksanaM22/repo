# Они все так похожи
import math
from sys import flags

class Figure:
    sides_count = 0
    def __init__(self, color, sides, filled = True):
        self.__sides = sides
        self.__color = list(color)

        self.filed = filled

    def get_color(self): #геттер -отдает атрибут
        return self.__color

    def __is_valid_color(self, r, g, b):
        return (isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and  0 <= r <= 255 and 0 <= g <= 255
                and 0 <= b <= 255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side < 0:
                return False
        if len(sides) != self.sides_count:
            return False
        return True
    def get_sides(self): # геттер
        return self.__sides

    def __len__ (self):#переопределяем функцию лен
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):# *-распаковывает наш параметр -картеж
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides, filled = True):
        super().__init__(color, sides, filled)
        self.__radius = sides/ 2 * math.pi

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides, filled = True):
        super().__init__(color, sides,  filled)

    def __calculate_height(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return (2 * area) / a

    def get_square(self):
        return 0.5 * self.__sides[0] * self.__calculate_height()

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides, filled = True):
        super().__init__(color, [sides]*self.sides_count, filled) # передаем в родительский класс в атрибут объекта __sides список из 12 сторон
        self.__sides = [sides]*self.sides_count
    def get_volume(self):
        return self.__sides[1] ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())












