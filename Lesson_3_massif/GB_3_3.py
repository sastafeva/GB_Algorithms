# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы


# Создадим массив из 20 произвольных целых чисел.
from random import randint
size = 20
array = [randint(-size, size) for _ in range(size)]

# Распечатаем для наглядности (чтобы можно было проверить корректность кода)
print(array)

# Сначала найдем максимальный и минимальный элементы и их индексы:
min_num = 0
max_num = 0
for i, item in enumerate(array):
    if item > max_num:
        max_num = item
        max_ind = i
    elif item < min_num:
        min_num = item
        min_ind = i

# Поменяем местами:
array[max_ind] = min_num
array[min_ind] = max_num

# Выведем измененный список на печать:
print(array)