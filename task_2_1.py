# 1.	Пользователь вводит число от 1 до 9999 (сумму выдачи в банкомате).
# Необходимо вывести на экран словами введенную сумму и в конце написать название
# валюты с правильным окончанием. Например: 7431 – семь тысяч четыреста тридцать один доллар,
# 2149 – две тысячи сто сорок девять долларов, 15 – пятнадцать долларов, 3 – три доллара.
# Для решения этой задачи вам необходимо будет применять оператор % (остаток от деления).


print("Введите число от 1 до 9999: ")
n = int(input())

if n > 9999:
    print('Число введено неверно')
elif n < 1:
    print('Число введено неверно')
else:
    pass

o = str(n)

x = len(o)

if x == 4:
    w = n % 100
    a = n % 10
    n = n // 10
    b = n % 10
    n = n // 10
    c = n % 10
    n = n // 10
    d = n
elif x == 3:
    w = n % 100
    a = n % 10
    n = n // 10
    b = n % 10
    n = n // 10
    c = n
    d = 0
elif x == 2:
    w = n % 100
    a = n % 10
    n = n // 10
    b = n % 10
    n = n // 10
    c = 0
    d = 0
elif x == 1:
    a = n
    b = 0
    c = 0
    d = 0

if d == 1:
    print("Одна тысяча")
elif d == 2:
    print("две тысячи")
elif d == 3:
    print('три тысячи')
elif d == 4:
    print('четыре тысячи')
elif d == 5:
    print('пять тысяч')
elif d == 6:
    print('шесть тысяч')
elif d == 7:
    print('семь тысяч')
elif d == 8:
    print('восемь тысяч')
elif d == 9:
    print('девять тысяч')
elif d == 0:
    pass

if c == 1:
    print('сто')
elif c == 2:
    print('двести')
elif c == 3:
    print('триста')
elif c == 4:
    print('четыреста')
elif c == 5:
    print('пятьсот')
elif c == 6:
    print('шестьсот')
elif c == 7:
    print('семьсот')
elif c == 8:
    print('восемьсот')
elif c == 9:
    print('девятьсот')
elif c == 0:
    pass

if w == 11:
    print('одинадцать')
    b = 0
    a = 0
elif w == 12:
    print('двенадцать')
    b = 0
    a = 0
elif w == 13:
    print('тринадцать')
    b = 0
    a = 0
elif w == 14:
    print('четырнадцать')
    b = 0
    a = 0
elif w == 15:
    print('пятнадцать')
    b = 0
    a = 0
elif w == 16:
    print('шестнадцать')
    b = 0
    a = 0
elif w == 17:
    print('семьнадцать')
    b = 0
    a = 0
elif w == 18:
    print('восемьнадцать')
    b = 0
    a = 0
elif w == 19:
    print('деветнадцать')
    b = 0
    a = 0
else:
    pass

if b == 1:
    print('десять')
elif b == 2:
    print('двадцать')
elif b == 3:
    print('тридцать')
elif b == 4:
    print('сорок')
elif b == 5:
    print('пятьдесят')
elif b == 6:
    print('шестьдесят')
elif b == 7:
    print('семьдесят')
elif b == 8:
    print('восемьдесят')
elif b == 9:
    print('девяносто')
elif b == 0:
    pass

if a == 1:
    print('один доллар')
elif a == 2:
    print('два доллара')
elif a == 3:
    print('три доллара')
elif a == 4:
    print('четыре доллара')
elif a == 5:
    print('пять долларов')
elif a == 6:
    print('шесть долларов')
elif a == 7:
    print('семь долларов')
elif a == 8:
    print('восемь долларов')
elif a == 9:
    print('девять долларов')
elif a == 0:
    print('долларов')
