# 3 вариант. С использованием сортированного массива и метода count

from random import randint
import cProfile


def count_count(size):
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


    return f'В произвольном массиве размера {size} ' \
           f'чаще всего встречается число {max_num}. ' \
           f'Количество вхождений: {max_count}.'

print(count_count(4))

# Проверим timeit
# size = 20
# python -m timeit -n 1000 -s "import GB_1_1_3" "GB_1_1_3.count_count(20)"
# 1000 loops, best of 5: 131 usec per loop

# size = 100
# python -m timeit -n 1000 -s "import GB_1_1_3" "GB_1_1_3.count_count(100)"
# 1000 loops, best of 5: 723 usec per loop

# size = 500
# python -m timeit -n 1000 -s "import GB_1_1_3" "GB_1_1_3.count_count(500)"
# 1000 loops, best of 5: 7.06 msec per loop

# size = 1000
# python -m timeit -n 1000 -s "import GB_1_1_3" "GB_1_1_3.count_count(1000)"
# 1000 loops, best of 5: 23.4 msec per loop


# # Проверим cProfile
# cProfile.run('count_count(20)')
# # 123 function calls in 0.000 seconds
# # 1    0.000    0.000    0.000    0.000 GB_1_1_3.py:7(count_count)
# # 20    0.000    0.000    0.000    0.000 random.py:174(randrange)
#
# cProfile.run('count_count(100)')
# # 566 function calls in 0.001 seconds
# # 1    0.000    0.000    0.001    0.001 GB_1_1_3.py:7(count_count)
# # 100    0.000    0.000    0.001    0.000 random.py:174(randrange)
#
# cProfile.run('count_count(500)')
# # 2734 function calls in 0.009 seconds
# # 1    0.000    0.000    0.009    0.009 GB_1_1_3.py:7(count_count)
# # 500    0.001    0.000    0.003    0.000 random.py:174(randrange)
#
# cProfile.run('count_count(1000)')
# # 5461 function calls in 0.026 seconds
# # 1    0.001    0.001    0.026    0.026 GB_1_1_3.py:7(count_count)
# # 1000    0.003    0.000    0.005    0.000 random.py:174(randrange)