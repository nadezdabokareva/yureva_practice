def task1():
    list1 = []
    N = int(input('Введите длину вашего списка (массива): '))
    print('Введите свой список:')
    for i in range(N):
        print(f'Введите {i + 1}-й элемент:')
        list1.append(float(input()))

    min_abs_element = min(list1, key=abs)
    print(f'Минимальный по модулю элемент: {min_abs_element}')


    print('Массив в обратном порядке:', list1[::-1])

def task2():
    size = 10  # Размер массивов A и B
    A = []
    B = []

    print('Введите элементы массива A:')
    for i in range(size):
        print(f'Введите {i + 1}-й элемент:')
        A.append(float(input()))

    print('Введите элементы массива B:')
    for i in range(size):
        print(f'Введите {i + 1}-й элемент:')
        B.append(float(input()))

    print('Исходный массив A:', A)
    print('Исходный массив B:', B)

    A, B = B, A

    print('Преобразованный массив A:', A)
    print('Преобразованный массив B:', B)

print("Выберите задачу для выполнения:")
print("1 - Найти минимальный по модулю элемент и вывести массив в обратном порядке.")
print("2 - Поменять местами содержимое массивов A и B.")
choice = int(input("Ваш выбор: "))

if choice == 1:
    task1()
elif choice == 2:
    task2()
else:
    print("Неверный выбор.")
