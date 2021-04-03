# Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

# В условиях задачи не указано, что на вход подаются целые числа. Принимаем любые.
# По условиям, мы не делаем проверку на корректность ввода.
# Значит на вход подаются точно числа и они все разные.
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a > b:
    if a > c:
        if b > c: #  получим c < b < a
            m = b
        else:     # получим b < c < a
            m = c
    else:         # получим b < a < c
        m = a
else:
    if b > c:
        if a > c: # получим b < a < c
            m = a
        else:     # получим a < c < b
            m = c
    else:         # получим a < b < c
        m = b
print('Среднее между введенными числами: ', m)