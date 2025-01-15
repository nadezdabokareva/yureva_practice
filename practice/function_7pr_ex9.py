def task1():
    num = int(input("Введите число: "))
    steps = 0

    while num > 0:
        sum_digits = sum(int(digit) for digit in str(num))
        num -= sum_digits
        steps += 1

    print(f"Количество действий до получения нуля: {steps}")


def task2():
    arrays = []

    for i in range(3):
        array = []
        print(f"Введите элементы {i + 1}-го массива:")
        n = int(input("Сколько элементов в массиве? "))

        for j in range(n):
            element = int(input(f"Введите {j + 1}-й элемент: "))
            array.append(element)

        arrays.append(array)

    for i, array in enumerate(arrays):
        product = 1
        for num in array:
            product *= num

        average = sum(array) / len(array)

        print(f"Массив {i + 1}: {array}")
        print(f"Произведение элементов массива {i + 1}: {product}")
        print(f"Среднее арифметическое массива {i + 1}: {average:.2f}")


# Запуск задач
print("Выберите задачу для выполнения:")
print("1 - Вычесть сумму цифр из числа до получения нуля.")
print("2 - Найти произведение и среднеарифметическое значение элементов трех массивов.")
choice = int(input("Ваш выбор: "))

if choice == 1:
    task1()
elif choice == 2:
    task2()
else:
    print("Неверный выбор.")
