# Определить, какое число в массиве встречается чаще всего.

from random import randint

# 1 вариант (с сортировкой)
# Создадим массив из 20 произвольных целых чисел.
# Интервал зададим меньше, чтобы получить больше повторяющихся чисел.
size = 20
array = [randint(0, size / 2) for _ in range(size)]

# Отсортируем массив (используем функцию, показанную в лекциях).
array.sort()
# Распечатаем для наглядности (чтобы можно было проверить корректность кода)
print(array)


# Создадим 3 переменные.
count = 1 # Для текущего пересчета
max_count = 1 # Для хранения максимального количества
max_num = array[0] # Число, входящее в список максимальное количество раз

# Будем с конца двигаться по массиву и считать количество одинаковых элементов
# Как только число сменилось, сравнивать количество его вхождений с максимальным.

for i in range(size-1):
    if array[i] == array[i+1]:
        count += 1
    else:
        if count > max_count:
            max_num = array[i]
            max_count = count
        count = 1
    # Добавляем проверку, если чаще всего встречается последнее число в списке.
    # Это необходимо, т.к. последний элемент мы ни с чем не сравниваем и в цикл не заходим.
    if i == (size-2) and count > max_count:
        max_num = array[i]
        max_count = count

# На случай изменения размера массива и диапазона значений:
if max_count > 1:
    print(f'Чаще всего встречается число {max_num}. Количество вхождений: {max_count}.')
else:
    print('Все элементы встречаются только 1 раз')

# 2 вариант (без сортировки)

size = 20
array = [randint(0, 9) for _ in range(size)]
print(array)

max_num = array[0]
max_count = 1
for i in range(size - 1):
    count = 1
    for j in range(i + 1, size):
        if array[i] == array[j]:
            count += 1
    if count > max_count:
        max_count = count
        max_num = array[i]

if max_count > 1:
    print(f'Чаще всего встречается число {max_num}. Количество вхождений: {max_count}.')
else:
    print('Все элементы встречаются только 1 раз')

# второй вариант даже короче получился


''' На самом деле, задача поставлена некорректно.
В списке могут быть 2 или 3 числа, входящие в него одинаковое максимальное количество раз.
Правильно решать эту задачу с помощью словаря. Считать количество вхождений каждого числа,
потом находить максимальное value и искать, есть ли еще такие же value.
'''

