list1 =[]
list2 =[]
N = int(input('Введите длину вашего списка (массива)'))
m=int(input('Введите число'))
print('Введите свой список')
for i in range (N):
    print('Введите', i, 'элемент:')
    list1.append(int(input()))
for i in range (N):
    if abs(list1[i]) > m:
        list2.append(list1[i])




