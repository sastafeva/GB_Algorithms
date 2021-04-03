#В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.


from random import randint
size = 20
elem = 20
array = [randint(-elem, elem) for _ in range(size)]

# Распечатаем для наглядности (чтобы можно было проверить корректность кода)
print(array)

# Максимальный отрицательный элемент - это тот, который ближе всего к 0.
# Будем искать минимальное значение разницы (0-item)

max_el = 0
max_ind = 0
min_dif = elem

for i, item in enumerate(array):
    if item < 0:
        if (0 - item) < min_dif:
            max_el = item
            max_ind = i
            min_dif = 0 - item

# Выведем на печать:
print(f'Максимальный отрицательный элемент {max_el}. Его позиция в массиве: {max_ind}.')