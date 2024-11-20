from tkinter import *

# Глобальная переменная для хранения выражения
expression = ""


def btn_click(item):
    global expression
    # Разрешить редактирование поля ввода
    input_field.config(state="normal")
    # Добавляем символ к выражению
    expression += item
    # Вставляем символ в поле ввода
    input_field.insert(END, item)
    # Если нажали кнопку "="
    if item == "=":
        try:
            # Вычислить результат выражения без последнего символа ("=").
            result = eval(expression[:-1])
            # Очистка текущего содержимого поля ввода перед вставкой результата.
            input_field.delete(0, END)
            input_field.insert(0, result)
            # Сброс выражения после вычисления
            expression = ""
        # Обработка возможных исключений при вычислении
        except ZeroDivisionError:
            input_field.delete(0, END)
            input_field.insert(0, 'Ошибка (деление на 0)')
        except SyntaxError:
            input_field.delete(0, END)
            input_field.insert(0, 'Ошибка')
        finally:
            # Запретить редактирование поля ввода после завершения операции
            input_field.config(state="readonly")
    else:
        # Запретить редактирование поля ввода после добавления символа
        input_field.config(state="readonly")


def bt_clear():
    global expression
    # Очищаем выражение
    expression = ""
    # Разрешаем редактирование поля ввода
    input_field.config(state="normal")
    # Очищаем содержимое поля ввода
    input_field.delete(0, END)
    # Запрещаем редактирование поля ввода
    input_field.config(state="readonly")


# Создаем главное окно приложения
root = Tk()
root.geometry("368x296")  # Увеличили размер окна для удобства
root.title("Калькулятор")
root.resizable(0, 0)  # Запрещаем изменение размера окна

# Рамка для поля ввода
frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Поле ввода
input_field = Entry(frame_input, font='Arial 20 bold',
                    justify='right')  # Изменение шрифта и выравнивание по правому краю
input_field.pack(fill=X, ipady=10)  # Увеличиваем высоту поля ввода и заполняем его по горизонтали

# Кнопки калькулятора
buttons = (
    ('7', '8', '9', '/'),  
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
)

# Кнопка очистки
Button(root, text='C', command=bt_clear).grid(row=1, column=0, columnspan=4, sticky="we",
                                              pady=(0, 5))  # Кнопку C растянули на всю ширину и добавили отступ снизу

# Создание кнопок калькулятора
for row in range(len(buttons)):
    for col in range(len(buttons[row])):
        button_text = buttons[row][col]
        Button(
            root,
            text=button_text,
            command=lambda text=button_text: btn_click(text),  # Используем late binding для передачи аргументов
            font='Arial 14'
        ).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)

# Запуск главного цикла программы
root.mainloop()

"""Глобальные переменные: Переменную объявляем как глобальную внутри функций, чтобы избежать ошибки.
Метод config() вместо доступа через[]: Использование метода config() для изменения состояния виджета
("normal" и "readonly").
Обновление макета: Кнопка "C" растянута на весь ряд сверху, добавлен небольшой отступ между ней и основными кнопками.
Исправлены лямбда - выражения: Для корректной работы лямбд - функций использовали технику "late binding".
Выравнивание текста в поле ввода: Установили выравнивание по правому краю(justify='right'), что более привычно
для калькуляторов."""
