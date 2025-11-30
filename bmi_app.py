# bmi_gui.py

import tkinter as tk
from tkinter import messagebox
from bmi_calculator import calculate_bmi


class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Калькулятор ИМТ")
        root.geometry("400x300")
        root.resizable(False, False)
        root.configure(bg="#f0f8ff")

        # Заголовок
        title_label = tk.Label(
            root,
            text="Калькулятор ИМТ",
            font=("Arial", 18, "bold"),
            bg="#f0f8ff",
            fg="#2c3e50"
        )
        title_label.pack(pady=15)

        # Вес
        weight_frame = tk.Frame(root, bg="#f0f8ff")
        weight_frame.pack(pady=5)
        tk.Label(weight_frame, text="Вес (кг):", bg="#f0f8ff", font=("Arial", 12)).pack(side=tk.LEFT)
        self.weight_entry = tk.Entry(weight_frame, font=("Arial", 12), width=15)
        self.weight_entry.pack(side=tk.LEFT, padx=10)

        # Рост
        height_frame = tk.Frame(root, bg="#f0f8ff")
        height_frame.pack(pady=5)
        tk.Label(height_frame, text="Рост (м):", bg="#f0f8ff", font=("Arial", 12)).pack(side=tk.LEFT)
        self.height_entry = tk.Entry(height_frame, font=("Arial", 12), width=15)
        self.height_entry.pack(side=tk.LEFT, padx=10)

        # Кнопка
        self.calc_button = tk.Button(
            root,
            text="Рассчитать ИМТ",
            command=self.calculate,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            relief="flat",
            padx=20,
            pady=5
        )
        self.calc_button.pack(pady=20)

        # Результат
        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f0f8ff",
            fg="#2c3e50",
            justify="center"
        )
        self.result_label.pack(pady=10)

        # Подсказка
        info_label = tk.Label(
            root,
            text="ИМТ = вес (кг) / рост² (м)\nРекомендации ВОЗ",
            font=("Arial", 10),
            bg="#f0f8ff",
            fg="#7f8c8d"
        )
        info_label.pack(side=tk.BOTTOM, pady=10)

    def calculate(self):
        weight_str = self.weight_entry.get().strip()
        height_str = self.height_entry.get().strip()

        # Проверка на пустой ввод
        if not weight_str or not height_str:
            messagebox.showwarning("Ошибка ввода", "Пожалуйста, заполните оба поля.")
            return

        try:
            weight = float(weight_str)
            height = float(height_str)

            # Вычисление ИМТ (валидация внутри calculate_bmi)
            bmi = calculate_bmi(weight, height)

            # Определение категории
            if bmi < 18.5:
                category = "недостаток веса"
            elif 18.5 <= bmi < 25:
                category = "нормальный вес"
            elif 25 <= bmi < 30:
                category = "избыточный вес"
            else:
                category = "ожирение"

            # Отображение результата
            self.result_label.config(
                text=f"Ваш ИМТ: {bmi}\nКатегория: {category}",
                fg="#27ae60"
            )

        except ValueError as e:
            if "Вес" in str(e) or "Рост" in str(e):
                messagebox.showerror("Ошибка", str(e))
            else:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа.\nПример: 70.5, 1.75")


if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()