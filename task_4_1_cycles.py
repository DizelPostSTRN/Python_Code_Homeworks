# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2


firstspisok = [2, 5, 7, 9, 0, 1, 6, 2]
secondspisok = []

for ind in firstspisok:
    secondspisok.append(ind * (-2))

print(secondspisok)

secondspisok.clear()

a = 0

while a < len(firstspisok):
    secondspisok.append(firstspisok[a] * (-2))
    a += 1

print(secondspisok)
