# 1. Создать произвольный список
# 2. Добавить новый элемент типа str в конец списка
# 3. Добавить новый элемент типа int на место с индексом
# 4. Добавить новый элемент типа list в конец списка
# 5. Добавить новый элемент типа tuple на место с индексом
# 6. Получить элемент по индексу
# 7. Удалить элемент
# 8. Найти число повторений элемента списка
# 9. Получите первый и последний элемент списка
# 10. Поменяйте значения переменных a и b местами
# 11. Проверить, есть ли в последовательности дубликаты


lst = []

lst.append(str('String'))
lst.append(int(3))
lst.append(list())
lst.append(tuple())
print(lst)

element = lst.index(3)
print(element)

dell_element = lst.pop(0)
print(lst)

lst_one = str(lst)
my_dict = {i: lst_one.count(i) for i in lst_one}
print(my_dict)

print(lst[0])
print(lst[-1])

# Зачем то меняем значения переменных a и b исходя из условия
a = 384
b = 7
a, b = b, a
print(a, b)

# Теперь проверим список на наличие дубликатов. Мы знаем что дубликатов там нет, поэтому заведем новый
# список, с которым будем работать
new_lst = [3, 5, 2, 1, 4, 4, 1]

new_lst.sort()
for x in range(0, len(new_lst)-1):
               if new_lst[x] == new_lst[x + 1]:
                   print(str(new_lst[x]) + ' This is a duplicates')
