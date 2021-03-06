myfile = open('filename.txt')

print(myfile.read(20))  # Если в метод read() передать число, то вернётся указанное число символов.

print(myfile.readline())
# Важно! Как только мы применили этот метод,
# то повторное его применение выдаст вторую строку, ещё одно — третью строку и так далее.

print(myfile.readlines())  # вернёт список, в котором элементами будут строки из файла.

# Самый часто используемый в реальности способ — чтение файла построчно в цикле for.
myfile = open('filename.txt')
for line in myfile:
    print(line)
