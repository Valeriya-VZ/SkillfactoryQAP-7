# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)

print(sum(5))