import tkinter as tk
from tkinter import messagebox
import random

def generate_pass():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '@#$&'

    try:
        n_letters = int(letters_entry.get())
        n_symbols = int(symbols_entry.get())
        n_numbers = int(numbers_entry.get())
    except ValueError:
        messagebox.showerror(title='ATTENTION', message='Please enter valid numbers.')
        return

    if n_letters < 0 or n_symbols < 0 or n_numbers < 0:
        messagebox.showerror(title='ATTENTION', message='Please enter positive numbers.')
        return

    password_list = [random.choice(letters) for _ in range(n_letters)]
    password_list += [random.choice(symbols) for _ in range(n_symbols)]
    password_list += [random.choice(numbers) for _ in range(n_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    messagebox.showinfo(title='CONFIRMATION', message='Password generated successfully!!')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x400')
    root.title("Password Generator")

    # Labels
    labels = {'n_letters': 'letters:', 'n_symbols': 'Symbols:', 'n_numbers': 'Digits:'}
    for key, value in labels.items():
        label = tk.Label(text=value)
        label.place(x=120, y=140 + 40 * list(labels.keys()).index(key), width=50)

    # Entries
    letters_entry = tk.Entry(width=15)
    letters_entry.place(x=175, y=140)
    symbols_entry = tk.Entry(width=15)
    symbols_entry.place(x=175, y=180)
    numbers_entry = tk.Entry(width=15)
    numbers_entry.place(x=175, y=220)
    password_entry = tk.Entry(width=30)
    password_entry.place(x=130, y=70, height=40)

    # Button
    generate = tk.Button(root, text='GENERATE', bg='green', command=generate_pass)
    generate.place(x=175, y=350, height=25, width=92)

    root.mainloop()
