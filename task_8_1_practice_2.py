# Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списке.


from random import randint
lst = [randint(1, 10) for i in range(10)]
print(lst)

for i in lst:
    c = lst.count(i)
    if c == 1:
        print(i)
