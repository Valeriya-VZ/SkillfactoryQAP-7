# Чему равно количество сравнений, которые производятся в алгоритме сортировки вставками?
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
cnt = 0


def cmp(ind, x):
    global cnt
    cnt = cnt + 1
    return array[ind] > x


for i in range(1, len(array)):
    x = array[i]
    idx = i
    # while idx > 0 and array[idx - 1] > x:
    while idx > 0 and cmp(idx - 1, x):
        array[idx] = array[idx - 1]
        idx -= 1
    array[idx] = x

print(array)
print(cnt)
