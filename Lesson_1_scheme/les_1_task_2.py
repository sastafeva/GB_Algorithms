{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите координату x первой точки: 5.2\n",
      "Введите координату y первой точки: 6\n",
      "Введите координату x второй точки: 7.2\n",
      "Введите координату y второй точки: 6\n",
      "Уравнение прямой y = 6.0\n"
     ]
    }
   ],
   "source": [
    "'''По введенным пользователем координатам двух точек вывести уравнение \n",
    "прямой вида y = kx + b, проходящей через эти точки.'''\n",
    "\n",
    "# В условиях задачи не указано, что на вход подаются целые числа. Принимаем любые.\n",
    "x1 = float(input('Введите координату x первой точки: '))\n",
    "y1 = float(input('Введите координату y первой точки: '))\n",
    "x2 = float(input('Введите координату x второй точки: '))\n",
    "y2 = float(input('Введите координату y второй точки: '))\n",
    "\n",
    "# Коэффициенты k и b могут равняться нулю. \n",
    "if x1 == x2 and y1 == y2:\n",
    "    print('Это точка')\n",
    "elif x1 == x2:\n",
    "    print(f'Уравнение прямой x = {x1}')\n",
    "elif y1 == y2:\n",
    "    print(f'Уравнение прямой y = {y1}')\n",
    "else:\n",
    "    # округлим вычисленные коэффициенты до 2-х знаков после запятой\n",
    "    k = round((y1 - y2) / (x1 - x2), 2)\n",
    "    b = round((y1 - k*x1), 2)\n",
    "    print(f'Уравнение прямой y = {k}x + {b}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Полезные функции из разбора ДЗ"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Возвращает числовое представление для указанного символа\n",
    "ord('a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# антипод для ord()\n",
    "chr(97)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x1 = 0.23\n"
     ]
    }
   ],
   "source": [
    "# Округление с помощью f строк\n",
    "x = 0.23456\n",
    "print(f'x1 = {x:.2f}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0b101\n",
      "0b110\n",
      "4 0b100\n",
      "7 0b111\n",
      "3 0b11\n",
      "1 0b1\n",
      "20 0b10100\n"
     ]
    }
   ],
   "source": [
    "# Побитовые операции\n",
    "# преобразует целое число в двоичную строку\n",
    "a = 5\n",
    "b = 6\n",
    "print(bin(a))\n",
    "print(bin(b))\n",
    "print(a&b, bin(a&b)) # побитовое И\n",
    "print(a|b, bin(a|b)) # побитовое ИЛИ\n",
    "print(a^b, bin(a^b)) # побитовое исключающее ИЛИ\n",
    "print(a>>2, bin(a>>2)) # сдвиг вправо (в данном случае двойной)\n",
    "print(a<<2, bin(a<<2)) # сдвиг влево (в данном случае двойной)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0x1e240\n",
      "0o361100\n"
     ]
    }
   ],
   "source": [
    "# преобразует число в 16-тиричную и 8-ричную систему\n",
    "m = 123456\n",
    "print(hex(m))\n",
    "print (oct(m))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
