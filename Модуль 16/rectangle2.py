# Создадим файл rectangle_2.py
# Выполним импорт класса Rectangle:
from rectangle1 import Rectangle, Square, Circle

# Далее создаем два прямоугольника
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# Выводим площади наших двух прямоугольников:
print(rect_1.get_area())
print(rect_2.get_area())

# Квадраты:
square_1 = Square(5)
square_2 = Square(10)

# Выводим площади квадратов
print(square_1.get_area_square(),
      square_2.get_area_square())

# Теперь мы хотим в нашей программе все объекты перенести в единую коллекцию.
# Назовем фигуры (figures). Коллекция содержит список,
# в который мы помещаем наш первый прямоугольник, квадрат и т.д.
figures = [rect_1, rect_2, square_1, square_2]
# Далее пройдемся по циклу for:
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())
# Это необходимо, чтобы найти площадь каждой фигуры, сохраненной в списке figures.
# Обратите внимание, мы будем работать с прямоугольниками и квадратами с помощью разных методов:
# get_area() и get_area_square(). Внутри цикла проверяем:
# 1)Если экземпляр класса figure является квадратом, то вызываем метод get_area_square().
# 2)В противном случае — обрабатываем данные для прямоугольника методом get_area().

# В условии есть функция isinstance, поддерживающая наследование.
# Она проверяет, является ли аргумент объекта экземпляром класса или экземпляром класса из кортежа.
# В случае если является, функция возвращает True, если не является — False.

# Добавляем два круга
circle_1 = Circle(5)
circle_2 = Circle(2)

# Выводим площади кругов
print(circle_1.get_area_circle(),
      circle_2.get_area_circle())

# Добавляем круг в figures
figures.append(circle_1)
figures.append(circle_2)
# И в цикл for
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())