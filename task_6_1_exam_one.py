# 1. С клавиатуры вводится 7 значное число. Если четных цифр в нем больше, чем
# нечетных, то найти сумму всех его цифр, если нечетных больше, то найти
# произведение 1 3 и 6 цифры.


n = int(input('Введите семизначное число: '))
numbers = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,
           n % 10]
chet = 0
nechet = 0

for number in numbers:
    if number % 2 == 0:
        chet += 1
    else:
        nechet += 1

if chet > nechet:
    print(sum(numbers))
else:
    print(numbers[0] * numbers[2] * numbers[5])


# Вариант из рабора
numb = input('Enter a numb: ')

nechet = 0
chet = 0
sum = 0

for ind in str(numb):
    if int(ind) % 2 == 0:
        chet += 1
    else:
        nechet += 1
    sum += int(ind)

if chet > nechet:
    print('Summa is', sum)
else:
    print('Multiplication is', int(numb[0]) * int(numb[2]) * int(numb[5]))
