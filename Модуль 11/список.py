L = ["а", "б", "в", 1, 2, 3, 4]
print (L[:3:-1])

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # cписок чисел

print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка