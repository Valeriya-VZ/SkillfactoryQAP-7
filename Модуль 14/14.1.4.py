# Напишите функцию, которая печатает “обратную лесенку” следующего типа:
# n = 3
# ***
# **
# *
def print_star(n):
    while n >= 1:
        print('*' * n)
        n -= 1

print_star(8)

# решение от курса:
def reverse_stair(n):
   for i in range(n, 0, -1):  # ф-ция for -делай несколько раз, ф-ция range задаем шаг: от n до 0 с шагом -1
       print("*" * i)

reverse_stair(5)