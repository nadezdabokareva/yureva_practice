def read_matrix_from_file(filename):
    """Чтение матрицы из файла."""
    with open(filename, 'r') as file:
        n = int(file.readline())  # Читаем размерность матрицы (n x n)
        matrix = [list(map(int, file.readline().split())) for _ in range(n)]
    return matrix


def write_output_to_file(filename, data):
    """Запись результатов в файл."""
    with open(filename, 'w') as file:
        file.write(data)


def task1_from_file(input_filename, output_filename):
    """Задача 1: Найти число элементов, кратных k, и наибольший из них в квадратной матрице."""
    matrix = read_matrix_from_file(input_filename)

    k = int(input("Введите число k: "))
    multiples = [element for row in matrix for element in row if element % k == 0]

    if multiples:
        max_multiple = max(multiples)
        result = f"Число элементов, кратных {k}: {len(multiples)}\n"
        result += f"Наибольший элемент, кратный {k}: {max_multiple}\n"
    else:
        result = f"Нет элементов, кратных {k}\n"

    write_output_to_file(output_filename, result)


def task2_from_file(input_filename, output_filename):
    """Задача 2: Найти наибольший по модулю элемент и получить новую матрицу порядка n-1."""
    matrix = read_matrix_from_file(input_filename)

    max_element = max(max(matrix, key=lambda row: max(row, key=abs)), key=abs)
    result = f"Наибольший по модулю элемент: {max_element}\n"

    max_row, max_col = next((i, row.index(max_element)) for i, row in enumerate(matrix) if max_element in row)

    new_matrix = [
        [matrix[i][j] for j in range(len(matrix)) if j != max_col]
        for i in range(len(matrix)) if i != max_row
    ]

    result += "Полученная матрица порядка n-1:\n"
    for row in new_matrix:
        result += ' '.join(map(str, row)) + '\n'

    write_output_to_file(output_filename, result)


# Запуск задач
input_filename = "Юрьева Надежда Сергеевна_ЗИТ-24М_vvod.txt"
output_filename = "Юрьева Надежда Сергеевна_ЗИТ-24М_vivod.txt"

print("Выберите задачу для выполнения:")
print("1 - Найти число элементов, кратных k, и наибольший из них в квадратной матрице.")
print("2 - Найти наибольший по модулю элемент и получить новую матрицу порядка n-1.")
choice = int(input("Ваш выбор: "))

if choice == 1:
    task1_from_file(input_filename, output_filename)
elif choice == 2:
    task2_from_file(input_filename, output_filename)
else:
    print("Неверный выбор.")
