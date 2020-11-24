# Отфильтровать из заданного списка только четные элементы. [-2, -1, 0, 1, -3, 2, -3]
def even_numbers(x):
    return x % 2 == 0  # функция возвращает только True или False

result = filter(even_numbers, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [-2, 0, 2]