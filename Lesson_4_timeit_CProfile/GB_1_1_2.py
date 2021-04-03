
# 2 вариант. С использованием несортированного массива:

from random import randint
import cProfile


def count_ar(size):
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

    return f'В произвольном массиве размера {size} ' \
           f'чаще всего встречается число {max_num}. ' \
           f'Количество вхождений: {max_count}.'


# Проверим timeit
# size = 20
# python -m timeit -n 1000 -s "import GB_1_1_2" "GB_1_1_2.count_ar(20)"
# 1000 loops, best of 5: 162 usec per loop

# size = 100
# python -m timeit -n 1000 -s "import GB_1_1_2" "GB_1_1_2.count_ar(100)"
# 1000 loops, best of 5: 1.43 msec per loop

# size = 500
# python -m timeit -n 1000 -s "import GB_1_1_2" "GB_1_1_2.count_ar(500)"
# 1000 loops, best of 5: 27.8 msec per loop

# size = 1000
# python -m timeit -n 1000 -s "import GB_1_1_2" "GB_1_1_2.count_ar(1000)"
# 1000 loops, best of 5: 109 msec per loop

cProfile.run('count_ar(20)')
# 111 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 GB_1_1_2.py:8(count_ar)
# 20    0.000    0.000    0.000    0.000 random.py:174(randrange)

cProfile.run('count_ar(100)')
# 534 function calls in 0.002 seconds
# 1    0.001    0.001    0.002    0.002 GB_1_1_2.py:8(count_ar)
# 100    0.000    0.000    0.001    0.000 random.py:174(randrange)

cProfile.run('count_ar(500)')
# 2515 function calls in 0.030 seconds
# 1    0.026    0.026    0.030    0.030 GB_1_1_2.py:8(count_ar)
# 500    0.001    0.000    0.003    0.000 random.py:174(randrange)

cProfile.run('count_ar(1000)')
# 5033 function calls in 0.111 seconds
# 1    0.103    0.103    0.111    0.111 GB_1_1_2.py:8(count_ar)
# 1000    0.003    0.000    0.006    0.000 random.py:174(randrange)

