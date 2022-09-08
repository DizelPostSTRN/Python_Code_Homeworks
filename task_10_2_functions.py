# Написать программу для работы с матрицами:
# 1. Создание
# 2. Вывод
# 3. Сумма всех элементов
# 4. Нахождение максимального элемента
# 5. Нахождение минимального элемента.


from random import randint


def create_matrix(n):
    matr = [[randint(1, 10) for j in range(n)]for i in range(n)]
    return matr


def out_matr(matr):
    for row in matr:
        print(row)


def get_sum(matr):
    s = 0
    for i in matr:
        s += sum(i)
    print('Summ', s)
    return s


def get_max(matr):
    return max([max(row) for row in matr])


if __name__ == '__main__':
    m = 5
    matrix = create_matrix(m)

    out_matr(matrix)

    res_sum = get_sum(matrix)

    res_max = get_max(matrix)
    print(res_max)


def temp(n, m):
    if n < m:
        return n + m
    elif n > m:
        return n - m


a = 10
b = 1
res = temp(a, b)
print(res)