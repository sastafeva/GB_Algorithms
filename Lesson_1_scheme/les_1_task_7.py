# Определить, является ли год, который ввел пользователь, високосным или не високосным.

# Високосным является год, который нацело делится на 4 или нацело делится на 100 и 400.
# Проверка корректности ввода по условиям задания не проверяется.
# Проверяем только года после 1582 года (год принятия Григорианского календаря).
a = int(input('Введите год после 1582 года: '))
if a % 4 == 0 and a % 100 != 0:
    print('Это високосный год')
elif a % 400 == 0:
        print ('Это високосный год')
else:
    print ('Это невисокосный год')

