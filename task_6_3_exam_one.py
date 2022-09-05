# Вводится 2 числа с клавиатуры (от 1 до 20). Так же генерируется 2 числа рандомно.
# Посчитать, сколько раз пара введенных чисел с клавиатуры окажется больше
# рандомной пары. Проверку выполнить 7 раз.
# В случае равенства (количества, когда пара больше и всех остальных случаем)
# вывести случайные числа, полученные в 4 итерации.

from random import randint

num_1 = int(input('Enter the first numb: '))
num_2 = int(input('Enter the second numb: '))

count = 1
res = 0

while count <= 7:
    r_1 = randint(1, 20)
    r_2 = randint(1, 20)

    print(r_1)
    print(r_2)

    if (r_1 + r_2) > (num_1 + num_2):
        res += 1

    if count == 4:
        res1, res2 = r_1, r_2
    count += 1

if res >= 4:
    print('Norandom more ', res)
else:
    print('The 4th oper ', res1, res2)
