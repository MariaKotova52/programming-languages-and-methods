from tkinter import Canvas, Tk, Frame, Entry, END, Button
from tkinter.messagebox import showinfo
from rationalFraction import RationalFraction

root = Tk()

root["bg"] = "#8FBC8F"
root.title("Calculator")
root.geometry("350x350")

root.resizable(False, False)

frame = Frame(root, bg="#8FBC8F")
frame.place(relx=0.15, rely=0, relwidth=0.7, relheight=1)


entry1 = Entry(root, width=10, font=("", 15))
entry1.place(x=50, y=10)

entry2 = Entry(root, width=10, font=("", 15))
entry2.place(x=205, y=10)


def block_keyboard(event):
    return "break"


def block_mouse(event):
    return "break"


entry1.bind("<Key>", block_keyboard)
entry2.bind("<Key>", block_keyboard)

entry1.bind("<Button-1>", block_mouse)
entry2.bind("<Button-1>", block_mouse)


def input_entry(a):
    if entry2.focus_get() == entry2:
        entry2.insert(END, a)
    else:
        entry1.insert(END, a)


def switch_focus():
    if entry1.focus_get() == entry1:
        entry2.focus()
    else:
        entry1.focus()


def el_delete():
    if entry1.focus_get() == entry1:
        entry1.delete(0, END)
    else:
        entry2.delete(0, END)


def parse_rational_fractions():
    try:
        numerator1, denominator1 = entry1.get().split("/")
        numerator2, denominator2 = entry2.get().split("/")
        frac1 = RationalFraction(int(numerator1), int(denominator1))
        frac2 = RationalFraction(int(numerator2), int(denominator2))
        return frac1, frac2
    except ValueError:
        showinfo("Ошибка", "Введите корректные числа в формате 'числитель/знаменатель'")
        return None, None
    except ZeroDivisionError:
        showinfo("Ошибка", "Нельзя разделить на дробь, числитель которой равен 0")
        return None, None


def parse_integer():
    try:
        return int(entry2.get())
    except ValueError:
        showinfo("Ошибка", "Введите корректное целое число")
        return None


def div_operation():
    frac1, frac2 = parse_rational_fractions()
    if frac1 and frac2:
        try:
            result = frac1.division(frac2)
            showinfo("Результат", f"Частное: {result}")
        except ZeroDivisionError:
            showinfo("Ошибка", "Невозможно выполнить деление на 0")


def add_operation():
    frac1, frac2 = parse_rational_fractions()
    if frac1 and frac2:
        result = frac1.addition(frac2)
        showinfo("Результат", f"Сумма: {result}")


def sub_operation():
    frac1, frac2 = parse_rational_fractions()
    if frac1 and frac2:
        result = frac1.subtraction(frac2)
        showinfo("Результат", f"Разность: {result}")


def power_operation():
    try:
        numerator1, denominator1 = entry1.get().split("/")
        frac1 = RationalFraction(int(numerator1), int(denominator1))
        power = parse_integer()
        if frac1 and power is not None:
            try:
                result = frac1.power(power)
                showinfo("Результат", f"Результат возведения в степень: {result}")
            except Exception as e:
                showinfo("Ошибка", f"Ошибка при возведении в степень: {e}")
    except ValueError:
        showinfo("Ошибка", "Введите корректные числа в формате 'числитель/знаменатель'")
        return None, None
    except ZeroDivisionError:
        showinfo("Ошибка", "Нельзя разделить на дробь, числитель которой равен 0")


def mult_operation():
    frac1, frac2 = parse_rational_fractions()
    if frac1 and frac2:
        result = frac1.multiply(frac2)
        showinfo("Результат", f"Произведение: {result}")


def minus_sign():
    if entry1.focus_get() == entry1:
        if not entry1.get().startswith("-"):
            entry1.insert(0, "-")
    else:
        if not entry2.get().startswith("-"):
            entry2.insert(0, "-")


# numpad
btn1 = Button(
    root, bg="#F0FFF0", fg="#000000", text="1", command=lambda: input_entry("1")
)
btn1.place(x=50, y=100, width=50, height=50)
btn2 = Button(
    root, bg="#F0FFF0", fg="#000000", text="2", command=lambda: input_entry("2")
)
btn2.place(x=125, y=100, width=50, height=50)
btn3 = Button(
    root, bg="#F0FFF0", fg="#000000", text="3", command=lambda: input_entry("3")
)
btn3.place(x=200, y=100, width=50, height=50)
btn4 = Button(
    root, bg="#F0FFF0", fg="#000000", text="4", command=lambda: input_entry("4")
)
btn4.place(x=50, y=150, width=50, height=50)
btn5 = Button(
    root, bg="#F0FFF0", fg="#000000", text="5", command=lambda: input_entry("5")
)
btn5.place(x=125, y=150, width=50, height=50)
btn6 = Button(
    root, bg="#F0FFF0", fg="#000000", text="6", command=lambda: input_entry("6")
)
btn6.place(x=200, y=150, width=50, height=50)
btn7 = Button(
    root, bg="#F0FFF0", fg="#000000", text="7", command=lambda: input_entry("7")
)
btn7.place(x=50, y=200, width=50, height=50)
btn8 = Button(
    root, bg="#F0FFF0", fg="#000000", text="8", command=lambda: input_entry("8")
)
btn8.place(x=125, y=200, width=50, height=50)
btn9 = Button(
    root, bg="#F0FFF0", fg="#000000", text="9", command=lambda: input_entry("9")
)
btn9.place(x=200, y=200, width=50, height=50)
btn0 = Button(
    root, bg="#F0FFF0", fg="#000000", text="0", command=lambda: input_entry("0")
)
btn0.place(x=125, y=250, width=50, height=50)

# operations
btn_div = Button(root, bg="#F0FFF0", fg="#000000", text="div", command=div_operation)
btn_div.place(x=270, y=50, width=50, height=50)

btn_add = Button(root, bg="#F0FFF0", fg="#000000", text="+", command=add_operation)
btn_add.place(x=270, y=100, width=50, height=50)

btn_sub = Button(root, bg="#F0FFF0", fg="#000000", text="-", command=sub_operation)
btn_sub.place(x=270, y=150, width=50, height=50)

btn_mult = Button(root, bg="#F0FFF0", fg="#000000", text="*", command=mult_operation)
btn_mult.place(x=270, y=200, width=50, height=50)

btn_pow = Button(
    root, bg="#F0FFF0", fg="#000000", text="^", command=power_operation
)  # Возведение в степень
btn_pow.place(x=270, y=250, width=50, height=50)

btn_minus = Button(root, bg="#F0FFF0", fg="#000000", text="—", command=minus_sign)
btn_minus.place(x=50, y=50, width=50, height=50)

btn_delete = Button(root, bg="#F0FFF0", fg="#000000", text="C", command=el_delete)
btn_delete.place(x=50, y=250, width=50, height=50)

btn_slash = Button(
    root, bg="#F0FFF0", fg="#000000", text="/", command=lambda: input_entry("/")
)
btn_slash.place(x=125, y=50, width=50, height=50)

switch_button = Button(
    root, bg="#F0FFF0", fg="#000000", text="<->", command=switch_focus
)
switch_button.place(x=200, y=250, width=50, height=50)
entry1.focus_set()
root.mainloop()
