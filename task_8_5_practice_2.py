# Cоздать словарь. ключ - символ, значенине - индекс, если встречается несколько
# раз - вывести список индексов


s = 'An apple a day keeps the doctor away'
dct = {}

for i, v in enumerate(s):
    if v == ' ':
        continue
    if v in dct.keys():
        l = []
        l.append(dct.get(v))
        l.append(i)
        dct[v] = l
    else :
        dct[v] = i
print(dct)