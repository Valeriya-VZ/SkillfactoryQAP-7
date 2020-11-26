# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода  __init__().
# На выходе в консоли вам необходимо получить длину и ширину с итоговыми значениями.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getrt(self):
        return self.width, self.height

    def getarea(self):
        return self.width * self.height


rectangle_1 = Rectangle(10, 20)

print('Rectangle', rectangle_1.getrt(), ",", 'square:', rectangle_1.getarea())
