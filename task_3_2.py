# Получить на ввод количество рублей и копеек и вывести в правильной
# форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки


a = int(input("Ваести кол-во копеек: "))

b = a // 100
c = a % 100

if b == 1:
    print(str(b) + (" Рубль"))
elif b > 4:
    print(str(b) + (" Рублей"))
elif b < 5:
    print(str(b) + (" Рубля"))

if c == 1:
    print(str(c) + (" Копейка"))
elif c > 4:
    print(str(c) + (" Копеек"))
elif c < 5:
    print(str(c) + (" Копейки"))
