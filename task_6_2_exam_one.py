# С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько
# согласных. В случае равенства вывести на экран все гласные буквы.


gls = 'eyuoai'
sogl = 'qwrtplkjhgfdszxcvbnm'

count_gl = 0
count_sogl = 0
lst_gl = ''

line = input('Enter a row: ')

for ind in line:
    if ind.lower() in gls.lower():
        count_gl += 1
    elif ind.lower() in sogl:
        count_sogl += 1
        lst_gl += ind

if count_sogl == count_gl:
    print(lst_gl)
else:
    print('Glasn is ', count_gl, 'soglasn', count_sogl)
