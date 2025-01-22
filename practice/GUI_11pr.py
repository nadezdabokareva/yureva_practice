import tkinter as tk
from tkinter import ttk, messagebox, filedialog


# Функция для калькулятора
def calculator():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Ошибка: деление на ноль!"
            else:
                result = num1 / num2
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: введите правильные числа.")


# Функция для обработки чекбоксов
def handle_checkbox():
    selected = []
    if checkbox1_var.get():
        selected.append("Первый")
    if checkbox2_var.get():
        selected.append("Второй")
    if checkbox3_var.get():
        selected.append("Третий")

    if selected:
        messagebox.showinfo("Выбранные варианты", f"Вы выбрали: {', '.join(selected)}")
    else:
        messagebox.showinfo("Выбор", "Вы не выбрали ни один вариант.")


# Функция для загрузки текста из файла
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
            text_box.delete(1.0, tk.END)  # Очищаем старый текст
            text_box.insert(tk.END, text_content)  # Загружаем новый текст


# Создаем главное окно
root = tk.Tk()
root.title("Юрьева Надежда Сергеевна")  # Название приложения
root.geometry("400x400")  # Размер окна

# Создаем вкладки
tab_control = ttk.Notebook(root)  # Используем ttk.Notebook для вкладок

# Первая вкладка (Калькулятор)
tab1 = tk.Frame(tab_control)
tab_control.add(tab1, text="Калькулятор")

# Ввод чисел для калькулятора
entry_num1 = tk.Entry(tab1)
entry_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(tab1)
entry_num2.grid(row=0, column=2, padx=10, pady=10)

# Выпадающий список для операций
operation_var = tk.StringVar()
operation_menu = tk.OptionMenu(tab1, operation_var, '+', '-', '*', '/')
operation_menu.grid(row=0, column=1, padx=10, pady=10)

# Кнопка для вычисления
calculate_button = tk.Button(tab1, text="Вычислить", command=calculator)
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Метка для вывода результата
result_label = tk.Label(tab1, text="Результат:")
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Вторая вкладка (Чекбоксы)
tab2 = tk.Frame(tab_control)
tab_control.add(tab2, text="Чекбоксы")

checkbox1_var = tk.BooleanVar()
checkbox2_var = tk.BooleanVar()
checkbox3_var = tk.BooleanVar()

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=checkbox1_var)
checkbox1.grid(row=0, column=0, padx=10, pady=10)
checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=checkbox2_var)
checkbox2.grid(row=1, column=0, padx=10, pady=10)
checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=checkbox3_var)
checkbox3.grid(row=2, column=0, padx=10, pady=10)

# Кнопка для обработки чекбоксов
checkbox_button = tk.Button(tab2, text="Показать выбор", command=handle_checkbox)
checkbox_button.grid(row=3, column=0, padx=10, pady=10)

# Третья вкладка (Работа с текстом)
tab3 = tk.Frame(tab_control)
tab_control.add(tab3, text="Текст")

# Кнопка для загрузки файла
load_button = tk.Button(tab3, text="Загрузить текст из файла", command=load_file)
load_button.grid(row=0, column=0, padx=10, pady=10)

# Текстовое поле для вывода текста из файла
text_box = tk.Text(tab3, wrap=tk.WORD, height=10, width=40)
text_box.grid(row=1, column=0, padx=10, pady=10)

# Добавляем вкладки в главное окно
tab_control.pack(expand=1, fill="both")

# Запуск приложения
root.mainloop()
