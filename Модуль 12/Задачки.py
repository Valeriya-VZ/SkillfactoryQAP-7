# Записать условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.
# Иногда проще записать все условия и не пытаться упростить их.
A = int(input("Введите число А:\n"))
B = int(input("Введите число B:\n"))
C = int(input("Введите число C:\n"))

if ((A < 45) and (B >= 45) and (C >= 45)) or \
        ((A >= 45) and (B < 45) and (C >= 45)) or \
        ((A >= 45) and (B >= 45) and (C < 45)):
    print("Есть число меньше 45 и оно только одно\n")
else:
    print("Числа меньше 45 нет или их несколько")

# Записать логическое выражение, которые определяют,
# что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.
A = int(input("Введите число:\n"))

if not (-10 < A > -1 or 2 < A > 15):
    print("Число не принадлежит интервалу")
else:
    print("Число в интервале")

# Дано двузначное число. Определить: входит ли в него цифра 5.
# Попробуйте решить её с использованием целочисленного деления и деления с остатком.
A = int(input("Введите двузначное число:\n"))

if A % 5 == 0 and (not (A // 5) % 2 == 0):
    print("В число входит цира 5")
# правильное решение:
n = 15
first_digit = n // 10
second_digit = n % 10
print((first_digit == 5) or (second_digit == 5))

# Проверить все ли элементы в списке являются уникальными.
list_ = [-5, 2, 4, 8, 12, -7, 5]
print(len(list_) == len(set(list_)))

# Дано натуральное восьмизначное число.
# Выясните, является ли оно палиндромом (читается одинаково слева направо и справа налево).
N = input('Введите восьмизначное число:\n')
NN = list(N)
if NN[:] == NN[::-1]:
    print(N)
# Решение задачки от курса:
num = 12345678
print(str(num) == str(num)[::-1])
