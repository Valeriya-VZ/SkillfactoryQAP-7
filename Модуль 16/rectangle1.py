# Нам необходимо рассчитать площадь геометрической фигуры на основе полиморфизма:
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

# Итак, у нас есть класс Rectangle с двумя параметрами: ширина и высота (a и b).
# Мы можем найти площадь прямоугольника. Для этого нужно длину умножить на высоту
# Для решения используем специальный метод get_area.
# Он принимает аргумент self, то есть сам класс Rectangle,
# и возвращает произведение атрибута a (ширина) на b (высота).
# Создадим файл rectangle_2.py

# Добавим в нашу программу еще один объект, например Square (квадрат)
class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2

# Добавьте еще один класс — круг (class Circle), который принимает в качестве аргументов свой радиус.
class Circle:
    def __init__(self, a):
        self.a = a
    def get_area_circle(self):
        return (self.a ** 2) * 3.14