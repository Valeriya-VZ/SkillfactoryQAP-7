# Напишите функцию, которая проверяет является ли число n, делителем числа a.
# И выводит на экран соответствующее сообщение, является ли число делителем или нет.
def divider(n, a):
    if a % n == 0:
        print(f"Число {n} делитель числа {a}")
    else:
        print(f"Число {n} не делитель числа {a}")

divider(3,6)
