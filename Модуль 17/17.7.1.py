# Напишите функцию count, которая возвращает количество вхождений элемента в массив
def count(array, element):
    count = 0
    for a in array:
        if a == element:
            count += 1
    return count