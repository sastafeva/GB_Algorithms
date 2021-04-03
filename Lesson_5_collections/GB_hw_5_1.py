# Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего

# По традиции не проверяем корректность ввода данных пользователем, иначе код несколько усложнится.

from _collections import defaultdict

# создаем функцию, которая позволит сократить время ввода квартальной прибыли
# и посчитает суммарную прибыль за год
def profit(kvartal):
    k1, k2, k3, k4 = kvartal.split(' ')
    return round(float(k1) + float(k2) + float(k3) + float(k4), 2)

N = int(input('Введите количество предприятий: '))

company = defaultdict(float)
av_profit = 0

for i in range(1, N + 1):
    n = input(f'Введите название предприятия {i}: ')
    print('Введите через пробел прибыль предприятия за каждый квартал (в формате 1.1 2.2 3.3 4.4): ')
    kvartal = profit(input())
    company[n] = kvartal
    av_profit += kvartal

#print(company)

av_profit = round(av_profit/N, 2)
print(f'Средняя прибыль за год суммарно по всем предприятиям: {av_profit}')
print()  # пустая строка, чтобы лучше выглядел вывод

print('Прибыль меньше среднего значения у следующих предприятий:')
for k in company:
    if company[k] <= av_profit:
        print(f'Предприятие {k} c прибылью - {company[k]}')

print()  # пустая строка, чтобы лучше выглядел вывод

print('Прибыль больше среднего значения у следующих предприятий:')
for k in company:
    if company[k] > av_profit:
        print(f'Предприятие {k} c прибылью - {company[k]}')


