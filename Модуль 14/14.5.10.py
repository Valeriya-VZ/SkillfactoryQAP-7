# Напишите рекурсивную функцию, которая зеркально разворачивает число.
# Предполагается, что число не содержит нули.
def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res 