# В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу


l = []

with open('class.txt', 'r') as f:
    for line in f:
        line = line[0:len(line) - 2]
        for ind in line:
            if ind.isdigit():
                l.append(int(ind))
                if int(ind) <= 3:
                    print(line.split(' ')[0])

print(sum(l) / len(l))
