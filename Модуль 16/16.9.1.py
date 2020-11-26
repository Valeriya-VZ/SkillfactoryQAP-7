# Создайте класс любых геометрических фигур, где на выход мы получаем характеристики фигуры.
# Каждый экземпляр должен иметь атрибуты, которые зависят от выбранной фигуры.
# Например, для прямоугольника это будут аргументы x, y, width и height.
# Кроме того вы должны иметь возможность передавать эти атрибуты при создании объекта класса.
# Создайте метод, который возвращает атрибуты вашей фигуры в виде строки.
class Triangle:
    def __init__(self, x, y, side1, side2, side3):
        self.x = x
        self.y = y
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def gettr(self):
        return self.x, self.y, self.side1, self.side2, self.side3


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def getcr(self):
        return self.x, self.y, self.radius


triangle_1 = Triangle(5, 10, 2, 3, 2)
circle_1 = Circle(5, 10, 5)

print('Triangle', triangle_1.gettr())
print('Circle', circle_1.getcr())
