# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы
# с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить
# в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

# Я выбрала задачу из тех, что делала:
# Определить, какое число в массиве встречается чаще всего.

# Будем считать суммарную память, затрачиваемую на название переменных и на их содержание.
# На момент завершения функции.


from random import randint

# Чтобы корректно запускать функции, обозначим сразу размер исследуемых массивов
SIZE = 10


# 1 вариант. С использованием отсортированного массива:
dict_var_1 = {}  # Словарь для получения локальный переменных из count_sort


def count_sort(size=SIZE):
    array = [randint(0, size / 2) for _ in range(size)]
    array.sort()
    count = 1
    max_count = 1
    max_num = array[0]

    for i in range(size - 1):

        if array[i] == array[i + 1]:
            count += 1
        else:
            if count > max_count:
                max_num = array[i]
                max_count = count
            count = 1

        if i == (size - 2) and count > max_count:
            max_num = array[i]
            max_count = count

    global dict_var_1
    dict_var_1 = locals()

    return f'В произвольном массиве размера {size} ' \
           f'чаще всего встречается число {max_num}. ' \
           f'Количество вхождений: {max_count}.'


# 2 вариант. С использованием несортированного массива:
dict_var_2 = {}  # Словарь для получения локальный переменных из count_ar


def count_ar(size=SIZE):
    array = [randint(0, size / 2) for _ in range(size)]
    max_count = 1
    max_num = array[0]

    for i in range(size - 1):
        count = 1
        for j in range(i + 1, size):
            if array[i] == array[j]:
                count += 1
        if count > max_count:
            max_count = count
            max_num = array[i]

    global dict_var_2
    dict_var_2 = locals()

    return f'В произвольном массиве размера {size} ' \
           f'чаще всего встречается число {max_num}. ' \
           f'Количество вхождений: {max_count}.'


# 3 вариант. С использованием сортированного массива и метода count:
dict_var_3 = {}  # Словарь для получения локальный переменных из count_count


def count_count(size=SIZE):
    array = [randint(0, size / 2) for _ in range(size)]
    array.sort()
    max_count = 1
    max_num = array[0]

    for i in range(size):
        if array[i] != array[i-1] or i == (size - 1):
            count = array.count(array[i])
        if count > max_count:
            max_count = count
            max_num = array[i]

    global dict_var_3
    dict_var_3 = locals()


    return f'В произвольном массиве размера {size} ' \
           f'чаще всего встречается число {max_num}. ' \
           f'Количество вхождений: {max_count}.'


# Проводим анализ эффективности использования памяти.

import sys
# print('Версия Python ', sys.version, sys.platform)
# Версия Python  3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] win32


# Функция для определения размера переменных
def show_size (x, level = 0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


# Функция для расчета суммы памяти
def var_size(x, level=0):
    res = sys.getsizeof(x)

    if hasattr(x, '__iter__'):

        if hasattr(x, 'items'):
            for key, value in x.items():
                res += var_size(key, level + 1)
                res += var_size(value, level + 1)

        elif not isinstance(x, str):
            for item in x:
                res += var_size(item, level + 1)

    return res

# Сначала запустим функции, чтобы заполнить наши словари:
count_sort()
count_ar()
count_count()

# Распечатаем словари, чтобы увидеть содержимое:
# print('Словарь функции count_sort ', dict_var_1)
# print('Словарь функции count_ar ', dict_var_2)
# print('Словарь функции count_count ', dict_var_3)
# Словарь функции count_sort  {'array': [0, 0, 0, 1, 1, 3, 3, 4, 4, 4], 'count': 3, 'max_count': 3, 'max_num': 0, 'i': 8, 'size': 10}
# Словарь функции count_ar  {'array': [1, 1, 5, 0, 2, 2, 3, 0, 5, 5], 'max_count': 3, 'max_num': 5, 'i': 8, 'count': 2, 'j': 9, 'size': 10}
# Словарь функции count_count  {'array': [0, 2, 2, 2, 3, 3, 3, 5, 5, 5], 'max_count': 3, 'max_num': 2, 'i': 9, 'count': 3, 'size': 10}


# Считаем суммарный объем памяти для SIZE = 10
res = 0
for k in dict_var_1:  # Первая функция count_sort
    show_size(k)
    show_size(dict_var_1[k])
    res += var_size(k) + var_size(dict_var_1[k])

print('Суммарный объем памяти на переменные: ', res)
#  type= <class 'str'>, size= 54, object= array
#  type= <class 'list'>, size= 192, object= [0, 0, 0, 1, 1, 3, 3, 4, 4, 4]
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 1
# 	 type= <class 'int'>, size= 28, object= 1
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 4
# 	 type= <class 'int'>, size= 28, object= 4
# 	 type= <class 'int'>, size= 28, object= 4
#  type= <class 'str'>, size= 54, object= count
#  type= <class 'int'>, size= 28, object= 3
#  type= <class 'str'>, size= 58, object= max_count
#  type= <class 'int'>, size= 28, object= 3
#  type= <class 'str'>, size= 56, object= max_num
#  type= <class 'int'>, size= 24, object= 0
#  type= <class 'str'>, size= 50, object= i
#  type= <class 'int'>, size= 28, object= 8
#  type= <class 'str'>, size= 53, object= size
#  type= <class 'int'>, size= 28, object= 10
# Суммарный объем памяти на переменные:  921

res = 0
for k in dict_var_2:  # Вторая функция count_ar
    show_size(k)
    show_size(dict_var_2[k])
    res += var_size(k) + var_size(dict_var_2[k])

print('Суммарный объем памяти на переменные: ', res)
#  type= <class 'str'>, size= 54, object= array
#  type= <class 'list'>, size= 192, object= [1, 1, 5, 0, 2, 2, 3, 0, 5, 5]
# 	 type= <class 'int'>, size= 28, object= 1
# 	 type= <class 'int'>, size= 28, object= 1
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 2
# 	 type= <class 'int'>, size= 28, object= 2
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 5
#  type= <class 'str'>, size= 58, object= max_count
#  type= <class 'int'>, size= 28, object= 3
#  type= <class 'str'>, size= 56, object= max_num
#  type= <class 'int'>, size= 28, object= 5
#  type= <class 'str'>, size= 50, object= i
#  type= <class 'int'>, size= 28, object= 8
#  type= <class 'str'>, size= 54, object= count
#  type= <class 'int'>, size= 28, object= 2
#  type= <class 'str'>, size= 50, object= j
#  type= <class 'int'>, size= 28, object= 9
#  type= <class 'str'>, size= 53, object= size
#  type= <class 'int'>, size= 28, object= 10
# Суммарный объем памяти на переменные:  1007

res = 0
for k in dict_var_3:  # Третья функция count_count
    show_size(k)
    show_size(dict_var_3[k])
    res += var_size(k) + var_size(dict_var_3[k])
print('Суммарный объем памяти на переменные: ', res)
#  type= <class 'str'>, size= 54, object= array
#  type= <class 'list'>, size= 192, object= [0, 2, 2, 2, 3, 3, 3, 5, 5, 5]
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 2
# 	 type= <class 'int'>, size= 28, object= 2
# 	 type= <class 'int'>, size= 28, object= 2
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 5
#  type= <class 'str'>, size= 58, object= max_count
#  type= <class 'int'>, size= 28, object= 3
#  type= <class 'str'>, size= 56, object= max_num
#  type= <class 'int'>, size= 28, object= 2
#  type= <class 'str'>, size= 50, object= i
#  type= <class 'int'>, size= 28, object= 9
#  type= <class 'str'>, size= 54, object= count
#  type= <class 'int'>, size= 28, object= 3
#  type= <class 'str'>, size= 53, object= size
#  type= <class 'int'>, size= 28, object= 10
# Суммарный объем памяти на переменные:  933


# Для count_sort 921
# Для count_ar 1007
# Для count_sort 933

# Проверим для SIZE = 500:
count_sort(500)
count_ar(500)
count_count(500)

res = 0
for k in dict_var_1:  # Первая функция count_sort
    res += var_size(k) + var_size(dict_var_1[k])

print('Суммарный объем памяти на переменные count_sort: ', res)

res = 0
for k in dict_var_2:  # Вторая функция count_ar
    res += var_size(k) + var_size(dict_var_2[k])

print('Суммарный объем памяти на переменные count_ar: ', res)


res = 0
for k in dict_var_3:  # Третья функция count_count
    res += var_size(k) + var_size(dict_var_3[k])

print('Суммарный объем памяти на переменные count_count: ', res)

# Суммарный объем памяти на переменные count_sort:  18721
# Суммарный объем памяти на переменные count_ar:  18807
# Суммарный объем памяти на переменные count_count:  18721

# Версия Python  3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] win32

# Выводы:
# Суммарный объем памяти, который Python выделяет под переменные не отличается для этих функций.
# Возможно, отличается время, затрачиваемое на исполнение кода.
# Возможно, объем памяти, который зартачивается на исполнение операций этих функций, различается.
# Но проверка этого не входила в условия задачи.
