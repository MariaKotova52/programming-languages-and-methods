from tkinter import Canvas,Tk,Frame,Entry,END,Button
from tkinter.messagebox import showinfo

root = Tk()

root['bg'] = '#8FBC8F'
root.title('Calculator')
root.geometry('300x300')

canvas = Canvas(root, height = 300, width = 250)
canvas.pack()

root.resizable(False, False)

frame = Frame(root, bg = '#8FBC8F')
frame.place(relx = 0.15, rely = 0, relwidth = 0.7, relheight = 1)


entry1 = Entry(root, width = 7, font = ('', 15))
entry1.place(x = 50, y = 10)

entry2 = Entry(root, width = 7, font = ('', 15))
entry2.place(x = 165, y = 10)

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

def mod_operation():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result = num1 % num2
        showinfo("Результат", f"Остаток от деления: {result}")
    except ValueError:
        showinfo("Ошибка", "Введите корректные числа")
    except ZeroDivisionError:
        showinfo("Ошибка", "Невозможно выполнить деление на 0")

def div_operation():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result = num1 // num2
        showinfo("Результат", f"Целочисленное деление: {result}")
    except ValueError:
        showinfo("Ошибка", "Введите корректные числа")
    except ZeroDivisionError:
        showinfo("Ошибка", "Невозможно выполнить деление на 0")

def minus_sign():
    if entry1.focus_get() == entry1:
        if not entry1.get().startswith('-'):
            entry1.insert(0, '-')
    else:
        if not entry2.get().startswith('-'):
            entry2.insert(0, '-')


btn1 = Button(root, bg = '#F0FFF0', fg = '#000000', text = '1', command = lambda: input_entry('1'))
btn1.place(x = 50, y = 100, width = 50, height = 50)
btn2 = Button(root, bg = '#F0FFF0', fg = '#000000', text = '2', command = lambda: input_entry('2'))
btn2.place(x = 125, y = 100, width = 50, height = 50)
btn3 = Button(root, bg = '#F0FFF0', fg = '#000000', text = '3', command = lambda: input_entry('3'))
btn3.place(x = 200, y = 100, width = 50, height = 50)
btn4 = Button(root, bg = '#F0FFF0', fg = '#000000', text = '4', command = lambda: input_entry('4'))
btn4.place(x = 50, y = 150, width = 50, height = 50)
btn5 = Button(root, bg = '#F0FFF0', fg = '#000000', text = '5', command = lambda: input_entry('5'))
btn5.place(x = 125, y = 150, width = 50, height = 50)
btn6 = Button(root, bg = '#F0FFF0', fg = '#000000', text = '6', command = lambda: input_entry('6'))
btn6.place(x = 200, y = 150, width = 50, height = 50)
btn7 = Button(root, bg = '#F0FFF0', fg = '#000000', text = '7', command = lambda: input_entry('7'))
btn7.place(x = 50, y = 200, width = 50, height = 50)
btn8 = Button(root, bg = '#F0FFF0', fg = '#000000', text = '8', command = lambda: input_entry('8'))
btn8.place(x = 125, y = 200, width = 50, height = 50)
btn9 = Button(root, bg = '#F0FFF0', fg = '#000000', text = '9', command = lambda: input_entry('9'))
btn9.place(x = 200, y = 200, width = 50, height = 50)
btn0 = Button(root, bg = '#F0FFF0', fg = '#000000', text = '0', command = lambda: input_entry('0'))
btn0.place(x = 125, y = 250, width = 50, height = 50)

btn_mod = Button(root, bg = '#F0FFF0', fg = '#000000', text = 'mod', command = mod_operation)
btn_mod.place(x = 125, y = 50, width = 50, height = 50)
btn_div = Button(root, bg = '#F0FFF0', fg = '#000000', text = 'div', command = div_operation)
btn_div.place(x = 200, y = 50, width = 50, height = 50)
btn_minus = Button(root, bg = '#F0FFF0', fg = '#000000', text = '—', command = minus_sign)
btn_minus.place(x = 50, y = 50, width = 50, height = 50)
btn_delete = Button(root, bg = '#F0FFF0', fg = '#000000', text = 'C', command = el_delete)
btn_delete.place(x = 50, y = 250, width = 50, height = 50)

switch_button = Button(root, bg = '#F0FFF0', fg = '#000000', text="<->", command=switch_focus)
switch_button.place(x = 200, y = 250, width = 50, height = 50)
entry1.focus_set()
root.mainloop()
