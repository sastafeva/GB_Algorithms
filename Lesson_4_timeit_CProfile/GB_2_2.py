# 2 функция: Не решето Эратосфена
# Без рекурсии
# Находим следующее простое число, записываем его в список простых чисел.
# Продолжаем поиск до тех пор, пока не находим n простых чисел.

import cProfile

# test_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
#              53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
#              109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
#              179, 181, 191, 193, 197, 199]


def simp_num(n):
    count = 1
    num = 1
    result = [2]

    if n == 1:
        return 2

    while count != n:
        num += 2

        for i in result:
            if num % i == 0:
                break
        else:
            count += 1
            result.append(num)

    return num

print(simp_num(100))

# Проверим, корректно ли работает функция:
# for i in range(len(test_list)):
#     if simp_num(i+1) == test_list[i]:
#         print('Ok')
#     else:
#         print('Error')


# Проверим timeit
# size = 20
# python -m timeit -n 1000 -s "import GB_2_2" "GB_2_2.simp_num(20)"
# 1000 loops, best of 5: 44.3 usec per loop

# size = 100
# python -m timeit -n 1000 -s "import GB_2_2" "GB_2_2.simp_num(100)"
# 1000 loops, best of 5: 811 usec per loop

# size = 500
# python -m timeit -n 1000 -s "import GB_2_2" "GB_2_2.simp_num(500)"
# 1000 loops, best of 5: 20.5 msec per loop

# size = 1000
# python -m timeit -n 1000 -s "import GB_2_2" "GB_2_2.simp_num(1000)"
# 1000 loops, best of 5: 86 msec per loop

# Проверим cProfile
cProfile.run('simp_num(20)')
# 23 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 GB_2_2.py:12(simp_num)
# 19    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('simp_num(100)')
# 103 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 GB_2_2.py:12(simp_num)
# 99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('simp_num(500)')
# 503 function calls in 0.023 seconds
# 1    0.022    0.022    0.022    0.022 GB_2_2.py:12(simp_num)
# 499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('simp_num(1000)')
# 1003 function calls in 0.087 seconds
# 1    0.087    0.087    0.087    0.087 GB_2_2.py:12(simp_num)
# 999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}