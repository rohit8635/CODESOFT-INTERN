from tkinter import *
from tkinter import messagebox

def show_list():
    tasklist.delete(0, END)
    with open("rohit.txt", 'r') as f:
        data = f.readlines()
        if data:
            tasklist.insert(END, *data)

def add_data():
    task = getdata.get()
    if task:
        tasklist.insert(END, task)
        getdata.delete(0, END)

def create():
    with open("rohit.txt", 'r') as f:
        data = f.readlines()
    if not data:
        with open("rohit.txt", 'a') as f:
            f.writelines([f"{task}\n" for task in tasklist.get(0, END)])
        messagebox.showinfo(title='Confirmation', message='You created tasklist successfully  !!')
    else:
        messagebox.showerror(title='ATTENTION', message='You already created a task list')

def update():
    task_count = tasklist.size()
    with open("rohit.txt", 'w') as f:
        for i in range(task_count):
            task = tasklist.get(i)
            f.write(f"{task}\n")
    messagebox.showinfo(title='UPDATE', message='You updated tasklist successfully  !!')

def delete():
    to_delete = tasklist.curselection()
    if to_delete:
        for i in reversed(to_delete):  
            tasklist.delete(i)

        with open("rohit.txt", "r") as file:
            lines = file.readlines()

        with open("rohit.txt", "w") as file:
            file.writelines(line for i, line in enumerate(lines) if i not in to_delete)

        messagebox.showinfo(title='DELETE', message='Your deleted task successfully  !!')

def done():
    change = tasklist.curselection()
    if change:
        i = change[0]
        data = tasklist.get(i)
        with open('rohit.txt', 'r', encoding="utf-8") as file:
            file_content = file.read()
        new_data = f"{data} ✔"
        modified_content = file_content.replace(data, new_data)

        with open('rohit.txt', 'w', encoding="utf-8") as file:
            file.write(modified_content)

        tasklist.delete(i)
        tasklist.insert(i, new_data)
        tasklist.itemconfig(i, fg='green')
        messagebox.showinfo(title='COMPLETION', message='You completed the task successfully!!')


root = Tk()
root.title("TO DO LIST")
root.geometry('400x500')


heading = Label(text="TO DO LIST", font=("Rangile", 24, 'bold'), fg='red')
heading.place(x=115, y=0)

frame = Frame(root, height=250, width=300, highlightbackground="red", highlightthickness=3)
frame.place(x=50, y=50)

tasklist = Listbox(frame, font=('times new roman', 12, 'bold'), fg='white', bg='#6F8FAF', selectmode=EXTENDED)
tasklist.place(x=2, y=2, height=243, width=290)

scrollbar = Scrollbar(root, command=tasklist.yview, width=12)
scrollbar.place(x=336, y=54, height=240)
tasklist.config(yscrollcommand=scrollbar.set)

getdata = Entry(root, width=35, highlightbackground='black', highlightthickness=1)
getdata.place(x=50, y=330, height=25)

add_button = Button(root, text='ADD', bg='yellow', width=9, command=add_data)
add_button.place(x=275, y=330, height=25)

create_button = Button(root, text='CREATE', bg='yellow', width=15, command=create)
create_button.place(x=65, y=380, height=30)

update_button = Button(root, text='UPDATE', bg='yellow', width=15, command=update)
update_button.place(x=220, y=380, height=30)

delete_button = Button(root, text='DELETE', bg='yellow', width=15, command=delete)
delete_button.place(x=65, y=430, height=30)

done_button = Button(root, text='DONE', bg='yellow', width=15, command=done)
done_button.place(x=220, y=430, height=30)


show_list()


root.mainloop()
