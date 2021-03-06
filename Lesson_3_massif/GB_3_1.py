#В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов

# Создадим список делимых
list_nat = [i for i in range(2, 100)]

# Создадим список делителей
list_del = [i for i in range(2, 10)]

# Создадим пустой список с ответами
ans = [0]*8

# Напишем цикл, который разделит каждое число из list_nat
# на каждое число из list_del и выберет только те решения,
# в которых остаток от деления равен 0.

for item in list_del:
    for num in list_nat:
        if num % item == 0:
            ans[item - 2] += 1 #item начинаются с 2, а индексы с 0.

# Выведем на печать красиво:
print('Количество чисел в диапазоне от 2 до 99, которые кратны числам в диапазоне от 2 до 9')

for i, item in enumerate(ans):
    print(f'{list_del[i]} - {item}')

