# Напишите функцию, которая будет возвращать количество делителей числа а.
# Пример ввода: 5
# Пример вывода программы: 2
def get_multipliers(a):
   count = 0
   for n in range(1, a + 1):
       if a % n == 0:
           count += 1
   print(count)
   return count

get_multipliers(5)  # 2
get_multipliers(4)  # 3