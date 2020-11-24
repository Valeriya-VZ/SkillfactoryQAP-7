# Линейная функция a*x = b, отсюда х = b/a
def linear_solve(a, b):
    return b/a


print(linear_solve(2, 9))

# Однако при делении на ноль будет ошибка
print(linear_solve(0,1))


# Модифицируем ее код, чтобы она могла учитывать такое поведение.
def linear_solve(a, b):
    if a:  # помним, что 0 интерпретируется как False, иначе True
        return b/a
    elif not a and not b: # снова используем числа в логических выражениях (когда и б и а равны 0)
        return "Бесконечное количество корней"
    else:
        return "Нет корней"