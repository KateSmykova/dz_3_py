from random import uniform


num = int(input('Введите количество элементов списка: '))
list = []

for i in range(num):
    a = uniform(0, 99)
    list.append(round(a, 2))

min = list[0]
max = 0
for i in range(len(list)):
    
    if max < list[i]:
        max = list[i]
    if min > list[i]:
        min = list[i]
dif = (max - int(max)) - (min - int(min))

print(list)
print(min, max)
print(round(dif,2))