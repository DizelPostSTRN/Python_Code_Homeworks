# Ввести почтовый адрес. Проверить доменной имя. В случае если оно
# gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
# “DOMAIN NAME is not supported’


a = input("Введите емейл: ")

b = a.find('@')
c = a[b:len(a)]

if c == '@gmail.com':
    print(a)
elif c != '@gmail.com':
    print('DOMAIN NAME is not supported')