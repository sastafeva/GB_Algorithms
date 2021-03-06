# Сформировать из введенного числа обратное
# по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

n = int(input('Введите натуральное число, n: '))

res = ''

while n != 0:
    m = n%10
    n //= 10
    res += str(m)

print (f'Обратное число {res}')

# Второй вариант:
num = input('Введите натуральное число, n: ')
result = ''
for i in num:
    result = i + result

print (f'Обратное число {result}')

# Другая задача про вывод таблицы ASCII

for i in range(32, 128):
    print (f'\t{i} - {chr(i)}', end = '')
    if i % 10 == 1:
        print()