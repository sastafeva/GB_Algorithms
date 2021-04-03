
# 1 вариант. С использованием отсортированного массива:

from random import randint
import cProfile


def count_sort(size):
    array = [randint(0, size / 2) for _ in range(size)]
    array.sort()
    count = 1  # Для текущего пересчета
    max_count = 1  # Для хранения максимального количества
    max_num = array[0]

    for i in range(size - 1):

        if array[i] == array[i + 1]:
            count += 1
        else:
            if count > max_count:
                max_num = array[i]
                max_count = count
            count = 1

        # Добавляем проверку, если чаще всего встречается последнее число в списке.
        # Это необходимо, т.к. последний элемент мы ни с чем не сравниваем и в цикл не заходим.
        if i == (size - 2) and count > max_count:
            max_num = array[i]
            max_count = count

    return f'В произвольном массиве размера {size} ' \
           f'чаще всего встречается число {max_num}. ' \
           f'Количество вхождений: {max_count}.'


# Проверим timeit
# size = 20
# python -m timeit -n 1000 -s "import GB_1_1_1" "GB_1_1_1.count_sort(20)"
# 1000 loops, best of 5: 119 usec per loop

# size = 100
# python -m timeit -n 1000 -s "import GB_1_1_1" "GB_1_1_1.count_sort(100)"
# 1000 loops, best of 5: 554 usec per loop

# size = 500
# python -m timeit -n 1000 -s "import GB_1_1_1" "GB_1_1_1.count_sort(500)"
# 1000 loops, best of 5: 2.75 msec per loop

# size = 1000
# python -m timeit -n 1000 -s "import GB_1_1_1" "GB_1_1_1.count_sort(1000)"
# 1000 loops, best of 5: 5.91 msec per loop

cProfile.run('count_sort(20)')
# 123 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 GB_1_1_1.py:8(count_sort)
# 20    0.000    0.000    0.000    0.000 random.py:174(randrange)

cProfile.run('count_sort(100)')
# 540 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 GB_1_1_1.py:8(count_sort)
# 100    0.000    0.000    0.001    0.000 random.py:174(randrange)

cProfile.run('count_sort(500)')
# 2515 function calls in 0.004 seconds
# 1    0.000    0.000    0.004    0.004 GB_1_1_1.py:8(count_sort)
# 500    0.001    0.000    0.003    0.000 random.py:174(randrange)

cProfile.run('count_sort(1000)')
# 5028 function calls in 0.012 seconds
# 1    0.001    0.001    0.012    0.012 GB_1_1_1.py:8(count_sort)
# 1000    0.005    0.000    0.008    0.000 random.py:174(randrange)

