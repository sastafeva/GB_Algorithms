# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import shuffle

size = 50
array = [i for i in range(-size,size)]
shuffle(array)  # перемешать массив
print('Исходный массив', array, sep = '\n')

# Функция разделения массива и слияния его обратно в отсортированном виде
def merge_sort(unsorted_list):

    # Конечная итерация рекурсии (или возврат массива, в котором не более 1 эл-та)
    if len(unsorted_list) <= 1:
        return unsorted_list

    # Находим середину и делим массив на 2 подмассива (левый и правый)
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    # применяем функцию рекурсивно к левой и правой части массива
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    # возвращаем массив, собранный из отсортированных половин
    return list(merge(left_list, right_list))


# Функция сортировки 2-х массивов
def merge(left_half, right_half):

    # Лист для сборки отсортированных частей исходного массива
    res = []

    # Цикл перебора элементов 2-х массивов
    while len(left_half) != 0 and len(right_half) != 0:

        # Сравниваем первые элементы массивов, добавляем в результирующий тот, который меньше.
        # И убираем этот элемент из исходного массива.
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])

    # Если один из сравниваемых массивов "закончился", остаток от второго добавляем в результирующий
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half

    # Возвращаем результирующий массив
    return res


# Короткий массив для тестирования функции
# size = 10
# array_test = [i for i in range(-size,size)]
# shuffle(array_test)  # перемешать массив
# print(array_test)
# print(merge_sort(array_test))


print('Отсортированный по возрастанию массив', merge_sort(array), sep = '\n')