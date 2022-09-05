# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1


lst = [1, 2, 3, 4, 5]
newlst = []

for ind in range(1, len(lst)):
    newlst.append(lst[ind])

newlst.append(lst[0])

print(newlst)
