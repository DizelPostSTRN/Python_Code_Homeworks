# Посчитать, сколько раз встречается определенная цифра в числах. Количество
# введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
# рандомно.


from random import randint

count_n = int(input('Enter count : '))
f_num = int(input('enter a numb: '))

lst = [(randint(100, 1000)) for ind in range(count_n)]
print('list', lst)

res = 0

for ind in lst:

    while ind > 0:
        n = ind % 10
        if n == f_num:
            res += 1
        ind = ind // 10

print(res)
