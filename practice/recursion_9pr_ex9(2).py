def task1():
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))

    remainder = a % b
    print(f"Остаток от деления {a} на {b}: {remainder}")


def task2():
    print("Введите последовательность натуральных чисел, заканчивающуюся нулем:")
    sequence = []

    while True:
        number = int(input())
        if number == 0:
            break
        sequence.append(number)

    if len(sequence) < 2:
        print("Последовательность слишком короткая для определения второго по величине элемента.")
        return

    max_element = max(sequence)
    sequence = [num for num in sequence if num != max_element]

    if not sequence:
        print("Нет второго по величине элемента.")
    else:
        second_largest = max(sequence)
        print(f"Второй по величине элемент: {second_largest}")


# Запуск задач
print("Выберите задачу для выполнения:")
print("1 - Вычислить остаток от деления a на b.")
print("2 - Найти второй по величине элемент в последовательности.")
choice = int(input("Ваш выбор: "))

if choice == 1:
    task1()
elif choice == 2:
    task2()
else:
    print("Неверный выбор.")
