def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper

# Нам всего лишь нужно передать в качестве аргумента имя функции,
# которую мы хотим выполнить, а все остальное сделает обёртка (в нашем случае wrapper).

#Эту функцию мы будем декорировать
def my_first_decorator():
    print("Это мой первый декоратор!")

my_first_decorator = my_decorator(my_first_decorator)


# Давайте рассмотрим пример функции, которая выполняется только в рабочие часы
# Если текущее время соответствует промежутку с 9 до 18, то мы выполняем функцию,
# в противном случае мы пропускаем этот шаг.
def working_hours(func):
    def wrapper():
        if 9 <= datetime.now().hour < 18:
            func()
        else:
            pass  # Нерабочее время, выходим
    return wrapper

def writing_tests():
    print("Я пишу тесты на python!")

writing_tests = working_hours(writing_tests)
# Вызов в консоли writing_tests() в нерабочее время в итоге ничего не выведет.
writing_tests()


# первый пример, написанный с использованием «синтаксического сахара»:
def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper


@my_decorator
def my_first_decorator():
    print("Это мой первый декоратор!")

# всего лишь пишем @my_decorator над именем функции, и Python понимает,
# что эта конструкция равносильна my_decorator(my_first_decorator),
# что более удобно как для понимая, так и для чтения кода.
