# В отдельный файл импортируйте и создайте объект Cat,
# который выводит имеющихся на сайте котов, с одинаковыми параметрами, но с разными значениями.
from cat import Cat

cat1 = Cat('Baron', 'boy', 2)

print('cat1.name=', cat1.name)
print('cat1.male=', cat1.male)
print('cat1.age=', cat1.age)

cat2 = Cat('Sam', 'boy', 2)

print('cat2.name=', cat2.name)
print('cat2.male=', cat2.male)
print('cat2.age=', cat2.age)