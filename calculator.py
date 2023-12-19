from tkinter import *
from tkinter import messagebox

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "errord"

def modules(a, b):
    if b != 0:
        return a % b
    else:
        return "errorm"

def handle_operation(operator, a, b):
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide, '%': modules}
    if operator in operations:
        return operations[operator](a, b)
    return None

def button_click(value):
    current_text = calsi.get()
    calsi.delete(0, END)
    calsi.insert(END, current_text + str(value))

def clear_entry():
    calsi.delete(0, END)

def calculate():
    try:
        expression = calsi.get()
        result = eval(expression)
        clear_entry()
        calsi.insert(0, result)
    except ZeroDivisionError:
        messagebox.showerror(title='ATTENTION', message='Division by zero is not possible')
    except Exception as e:
        messagebox.showerror(title='ATTENTION', message=f'Error: {e}')

def create_button(root, text, x, y, height, width, command):
    button = Button(root, text=text, font=('Serif', 12, 'bold'), command=command)
    button.place(x=x, y=y, height=height, width=width)

root = Tk()
root.title("Simple Calculator")
root.geometry("400x400")
root.config(bg='#81D8D0')

frame = Frame(root, height=500, width=300, bg='#FAF9F6')
frame.place(x=50, y=60)

name = Label(text="CALCULATOR", fg='black', font=('times new roman', 20, 'bold'), bg='#81D8D0')
name.place(x=130, y=20)

calsi = Entry(frame)
calsi.place(x=30, y=40, width=240, height=40)

buttons = [
    ('1', 30, 110, lambda: button_click(1)), ('2', 90, 110, lambda: button_click(2)),
    ('3', 150, 110, lambda: button_click(3)), ('4', 30, 160, lambda: button_click(4)),
    ('5', 90, 160, lambda: button_click(5)), ('6', 150, 160, lambda: button_click(6)),
    ('7', 30, 210, lambda: button_click(7)), ('8', 90, 210, lambda: button_click(8)),
    ('9', 150, 210, lambda: button_click(9)), ('0', 90, 260, lambda: button_click(0)),
    ('+', 210, 110, lambda: button_click('+')), ('-', 210, 160, lambda: button_click('-')),
    ('*', 210, 210, lambda: button_click('*')), ('/', 210, 260, lambda: button_click('/')),
    ('=', 150, 260, calculate), ('C', 30, 260, clear_entry)
]

for (text, x, y, command) in buttons:
    create_button(frame, text, x, y, 30, 40, command)

root.mainloop()
