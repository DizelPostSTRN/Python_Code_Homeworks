# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.


a = [1, 2, 1, 3, 4, 5, 2, 3, 1]
counter = 0
for i in range(len(a)):
    print(a[i])
    for j in range(i + 1, len(a)):
        print(a[j])
        if a[i] == a[j]:
            counter += 1
print(counter)
