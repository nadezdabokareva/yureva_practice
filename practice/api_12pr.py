import tkinter as tk
from tkinter import messagebox
import requests
import json


# Функция для получения данных из GitHub API
def get_repo_info():
    repo_name = entry_repo.get()  # Получаем имя репозитория из поля ввода
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите имя репозитория.")
        return

    url = f"https://api.github.com/repos/{repo_name}"

    try:
        response = requests.get(url)
        data = response.json()

        # Проверяем, если репозиторий существует
        if 'message' in data and data['message'] == 'Not Found':
            messagebox.showerror("Ошибка", "Репозиторий не найден.")
            return

        # Формируем информацию для сохранения
        repo_info = {
            'company': data.get('company', None),
            'created_at': data.get('created_at', None),
            'email': data.get('email', None),
            'id': data.get('id', None),
            'name': data.get('name', None),
            'url': data.get('url', None)
        }

        # Сохраняем данные в файл
        with open("repo_info.json", "w") as file:
            json.dump(repo_info, file, indent=4)

        messagebox.showinfo("Успех", "Информация о репозитории сохранена в файл 'repo_info.json'.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Ошибка при запросе: {e}")


# Создаем главное окно
root = tk.Tk()
root.title("GitHub Репозиторий Информация")
root.geometry("400x200")

# Создаем поле для ввода имени репозитория
label_repo = tk.Label(root, text="Введите имя репозитория:")
label_repo.pack(pady=10)

entry_repo = tk.Entry(root, width=40)
entry_repo.pack(pady=10)

# Кнопка для получения данных о репозитории
button_get_info = tk.Button(root, text="Получить информацию", command=get_repo_info)
button_get_info.pack(pady=20)

# Запуск приложения
root.mainloop()
