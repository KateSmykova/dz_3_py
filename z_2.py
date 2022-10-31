from random import randint


num = int(input('Введите количество элементов списка: '))
list1 = []
list2 = []

for i in range(num):
    list1.append(randint(0, 99))

for i in range(len(list1)):
    while i < len(list1)/2 and num > len(list1)/2:
        num -= 1
        a = list1[i] * list1[num]
        list2.append(a)
        i += 1

print(list1)
print(list2)