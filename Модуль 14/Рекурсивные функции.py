# Найти факториал числа (это произведение натуральных чисел от 1 до самого числа (включая данное число).
def fact(n):
    if n == 1:  # терминальный случай, который остановит рекурсивные вызовы
        return 1
    return n * fact(n - 1)  # рекурсивный вызов


# Вчисление чисел Фибоначчи
# Как известно, последовательность Фибоначчи начинается с 1 и 1,
# после чего каждое новое число является результатом сложения двух предыдущих чисел:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …
# Если разделить два последовательных числа в этом ряду, например 144/89,
# в конечном итоге получится число 1,618, которое называется «Золотое число
def rec_fibb(n):
   if n == 1:
       return 1
   if n == 2:
      return 1
   return rec_fibb(n - 1) + rec_fibb(n - 2)

rec_fibb(10)  # 55