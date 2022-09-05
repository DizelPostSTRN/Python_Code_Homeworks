# Дан список целых чисел. Подсчитать сколько четных чисел в списке

firstlist = [2, 4, 5, 9, 7, 13, 53, 44]
answer = 0

for ind in firstlist:
    if ind % 2 == 0:
        answer += 1

print(answer)

answer = 0

a = 0

while a < len(firstlist):
    if firstlist[a] % 2 == 0:
        answer += 1
    a += 1

print(answer)
