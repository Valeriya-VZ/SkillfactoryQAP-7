# Пусть на вход программы поступает массив из произвольного количества целых чисел
# и ещё одно целое число, которое будем проверять на вхождение в этот массив.
# Задача состоит в том, чтобы вернуть индекс первого вхождения элемента,
# если он входит в него, и False если не входит.
def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

array = list(map(int, input().split()))
element = int(input())

print(find(array, element))


# Двоичный поиск:
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = int(input())
array = [i for i in range(1, 100)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, 99))