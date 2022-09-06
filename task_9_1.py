# Найти сумму всех столбцов
# Найти из суммы всех столбцов максимальную сумму (из полученного списка)

import random

st = 5
stolb = 7

matrix = [[random.randint(0, 10) for j in range(stolb)] for i in range(st)]
# print(matrix)

max_sum = sum(matrix[0])
ind_max = 1
# print(matrix)
for i in matrix:
    print(i)

for ind, values in enumerate(matrix):
    temp_sum = sum(values)
    # print(ind)
    # print(values)
    if temp_sum > max_sum:
        ind_max = ind + 1

print(ind_max)