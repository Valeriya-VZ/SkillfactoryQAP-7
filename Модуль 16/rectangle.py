# Создадим конструктор, который будет описывать прямоугольник с имеющимися характеристиками: ширина и высота.
# Вычислим площадь фигуры (area)
# Выполним наследование из основного прямоугольника (Rectangle)
# возьмем оттуда все свойства, такие как width (ширина) и height (высота), и создадим псевдопрямоугольник r1.
# Прямоугольник r1 должен наследовать те же характеристики, что и базовый прямоугольник (Rectangle)
# Выполняется это через импортирование.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
# метод расчитывающий площадь
    def getArea(self):
        return self.width * self.height