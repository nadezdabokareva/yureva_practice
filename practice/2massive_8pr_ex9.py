def task1():
    n = int(input("Введите порядок квадратной матрицы: "))
    k = int(input("Введите число k: "))

    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = [int(input(f"Введите элемент ({i + 1}, {j + 1}): ")) for j in range(n)]
        matrix.append(row)

    multiples = [element for row in matrix for element in row if element % k == 0]

    if multiples:
        max_multiple = max(multiples)
        print(f"Число элементов, кратных {k}: {len(multiples)}")
        print(f"Наибольший элемент, кратный {k}: {max_multiple}")
    else:
        print(f"Нет элементов, кратных {k}")


def task2():
    n = int(input("Введите порядок квадратной матрицы: "))

    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = [float(input(f"Введите элемент ({i + 1}, {j + 1}): ")) for j in range(n)]
        matrix.append(row)

    max_element = max(max(matrix, key=lambda row: max(row, key=abs)), key=abs)
    print(f"Наибольший по модулю элемент: {max_element}")

    # Найти индексы строки и столбца с этим элементом
    max_row, max_col = next((i, row.index(max_element)) for i, row in enumerate(matrix) if max_element in row)

    # Создать новую матрицу порядка n-1, исключив строку и столбец с найденным элементом
    new_matrix = [
        [matrix[i][j] for j in range(n) if j != max_col]
        for i in range(n) if i != max_row
    ]

    print("Полученная матрица порядка n-1:")
    for row in new_matrix:
        print(row)


# Запуск задач
print("Выберите задачу для выполнения:")
print("1 - Найти число элементов, кратных k, и наибольший из них в квадратной матрице.")
print("2 - Найти наибольший по модулю элемент и получить новую матрицу порядка n-1.")
choice = int(input("Ваш выбор: "))

if choice == 1:
    task1()
elif choice == 2:
    task2()
else:
    print("Неверный выбор.")
