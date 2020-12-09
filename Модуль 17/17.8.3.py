# Сортировка пузырьком
# Его суть сводится к тому, что максимальные элементы шаг за шагом «всплывают» вправо -
# в отсортированную часть массива. И по ходу совершаются ещё перестановки,
# если это необходимо, ведь каждый раз мы сравниваем только соседние элементы!
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)


# Сортировка вставками
# В начале итерации устанавливается ведущий элемент.
# На первой итерации — самый первый элемент, и по умолчанию он считается уже отсортированным.
# Сохраняем ведущий элемент в дополнительную переменную.
# Далее происходит поиск места, куда должен встать ведущий элемент в уже отсортированной (левой) части массива.
# Можно, например, использовать цикл while с условием достижения границы и/или успешным нахождением элемента.
# Пока условие цикла выполняется, происходит сдвиг каждого элемента вправо.
# По завершении цикла сохранённое значение переменной помещается на освободившееся место. Алгоритм завершается.
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x