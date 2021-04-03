# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

# По традиции не проверяем корректность ввода данных пользователем, иначе код несколько усложнится.

from collections import deque

a = input('Введите первое шестнадцатеричное число, a: ').upper()
b = input('Введите второе шестнадцатеричное число, b: ').upper()
# Проверка.
# print('сумма', hex(int(a, 16) + int(b, 16)))
# print('произведение', hex(int(a, 16) * int(b, 16)))



# Словарь для перевода из 16-тиричной системы в десятиричную и наоборот
numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
           '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
           'C': 12, 'D': 13, 'E': 14, 'F': 15,
           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
           6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
           12: 'C', 13: 'D', 14: 'E', 15: 'F'}

# Для дальнейшего расчета сделаем число a больше, чем b
if len(b) > len(a):
    a, b = deque(b), deque(a)
else:
    a, b = deque(a), deque(b)


# Функция для расчета суммы чисел
def sum_num(a, b):
    # Скопируем исходные очереди, чтобы они не изменились в процессе исполнения функции
    fst = a.copy()
    snd = b.copy()
    result_lst = deque()  # Будем добавлять результат вычисления в очередь
    extra = 0   # переменная для увеличения следующего разряда

    while fst:   # Цикл, пока не закончатся значения в a

        if snd:  # Если в b еще есть значения
            c = numbers[fst.pop()] + numbers[snd.pop()] + extra
        else:
            c = numbers[fst.pop()] + extra

        extra = 0  # обнуляем для дальнейших вычислений

        if c < 16:
            result_lst.appendleft(numbers[c])

        else:
            result_lst.appendleft(numbers[c - 16])
            extra = 1

    # Если значения в a и b закончились, а extra не равна 0, нужно увеличить результат
    if extra:
        result_lst.appendleft('1')

    # Переведем результат в строчный вид, чтобы красиво вывести на печать
    result = ''
    for i in result_lst:
        result += str(i)

    return result

# Функция произведения чисел
def comp_num(a, b):
    # Будем сразу записывать результат в comp_lst
    comp_lst = deque(['0' for i in a])
    spam = 0    # Переменная, необходимая для сдвига индекса comp_lst

    for i in range(len(b)-1,-1, -1):
        spam -= 1
        sdvig = spam    # сдвиг индекса comp_lst для корректной записи результата вычисления
        extra = 0       # переменная увеличения разряда

        for j in range(len(a)-1,-1, -1):

            if abs(sdvig) > len(comp_lst): # Добавляем разряд в comp_lst, если цикл еще не закончился
                comp_lst.appendleft('0')

            c = numbers[a[j]] * numbers[b[i]] + extra + numbers[comp_lst[sdvig]]
            extra = 0

            if c < 16:
                comp_lst[sdvig] = numbers[c]

            else:
                comp_lst[sdvig] = numbers[c % 16]
                extra = c // 16

                if j == 0 and extra != 0:
                    comp_lst.appendleft(numbers[extra % 16])

            sdvig -= 1


    # Переведем результат в строчный вид
    result = ''
    for i in comp_lst:
        result += str(i)
    return result


print(f'Сумма чисел a и b равна {sum_num(a, b)}')
print(f'Произведение чисел a и b равно {comp_num(a, b)}')
