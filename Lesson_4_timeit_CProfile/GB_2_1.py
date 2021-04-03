# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# 1 функция: Решето Эратосфена
# Без рекурсии

import cProfile

test_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
             53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
             109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
             173, 179, 181, 191, 193, 197, 199]

def simp_er(n):
    count = 1
    a = 3
    b = 4 * n
    sieve = [i for i in range(a, b) if i % 2 != 0]
    result = [2]

    if n == 1:
        return 2

    while count < n:
        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        result.extend([i for i in sieve if i != 0])

        a, b = b, b + 2 * n
        sieve = [i for i in range(a, b) if i % 2 != 0]

        for i in range(len(sieve)):

            for j in result:

                if sieve[i] % j == 0:
                    sieve[i] = 0
                    break

print(simp_er(100))
# Проверим, корректно ли работает функция:
# for i in range(len(test_list)):
#     if simp_er(i+1) == test_list[i]:
#         print('Ok')
#     else:
#         print('Error')


# Проверим timeit
# size = 20
# python -m timeit -n 1000 -s "import GB_2_1" "GB_2_1.simp_er(20)"
# 1000 loops, best of 5: 44.1 usec per loop

# size = 100
# python -m timeit -n 1000 -s "import GB_2_1" "GB_2_1.simp_er(100)"
# 1000 loops, best of 5: 843 usec per loop

# size = 500
# python -m timeit -n 1000 -s "import GB_2_1" "GB_2_1.simp_er(500)"
# 1000 loops, best of 5: 22.2 msec per loop

# size = 1000
# python -m timeit -n 1000 -s "import GB_2_1" "GB_2_1.simp_er(1000)"
# 1000 loops, best of 5: 72.5 msec per loop

# Проверим cProfile
cProfile.run('simp_er(20)')
# 56 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 GB_2_1.py:13(simp_er)
# 51    0.000    0.000    0.000    0.000 {built-in method builtins.len}

cProfile.run('simp_er(100)')
# 353 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 GB_2_1.py:13(simp_er)
# 345    0.000    0.000    0.000    0.000 {built-in method builtins.len}

cProfile.run('simp_er(500)')
# 2040 function calls in 0.023 seconds
# 1    0.021    0.021    0.023    0.023 GB_2_1.py:13(simp_er)
# 2029    0.000    0.000    0.000    0.000 {built-in method builtins.len}

cProfile.run('simp_er(1000)')
# 4289 function calls in 0.074 seconds
# 1    0.071    0.071    0.074    0.074 GB_2_1.py:13(simp_er)
# 4278    0.001    0.000    0.001    0.000 {built-in method builtins.len}
