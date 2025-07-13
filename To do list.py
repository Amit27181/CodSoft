from tkinter import *
import tkinter.messagebox as tmsg
import json
import os

def add():
    task = entry_task.get()
    if task:
        task_listbox.insert(ACTIVE,entry_task.get())

    else:
        tmsg.showwarning("Error", "Please enter a task to add!")

def delete():
    try:
        selected_task = task_listbox.curselection()
        task_listbox.delete(selected_task)

    except:
        tmsg.showwarning("Error", "Please select a task to delete!")

def done():
    try:
        selected_task = task_listbox.curselection()
        task = task_listbox.get(selected_task)
        if task.endswith("✔"):
            tmsg.showwarning("Error", "This task is already done!")
        else:
            task_listbox.delete(selected_task)
            task_listbox.insert(ACTIVE, f"{task}✔")
    except:
        tmsg.showwarning("Error", "Please select a task to done!")

def SaveTask():
    tasks = task_listbox.get(0, END)  # Get all tasks from Listbox
    with open("tasks.json", "w") as file:
        json.dump(list(tasks), file)

def LoadTask():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task_listbox.insert(END, task)

root = Tk()

root.geometry("644x700")
root.maxsize(644,700)
root.minsize(644,700)
root.title("To-Do List")
root.configure(bg = "grey")

task_label = Label(root,text = "TO-Do List",font = "Bierstadt 20 bold",bg = "grey",fg = "white")
task_label.pack()

frame = Frame(root,borderwidth = 6, relief = SUNKEN,bg = "grey")
frame.pack()

entry_task = Entry(frame,font = "Bierstadt 20",width = 400)
entry_task.pack()

Button(root, text="Add Task", width=12, command=add,fg = "white",bg = "black").pack()

f1 = Frame(root,borderwidth = 6, relief = SUNKEN,bg = "grey")
f1.pack()

task_listbox = Listbox(f1,width = 622,height = 15,font = "Bierstadt 20", selectbackground="grey")
task_listbox.pack()

f2 = Frame(root)
f2.pack()

Button(f2, text="Mark Done", width=12, command=done,fg = "white",bg = "black").grid(row=0, column=0)
Button(f2, text="Delete Task", width=12, command=delete,fg = "white",bg = "black").grid(row=0, column=1)
Button(root, text="Save Task",font = "Bierstadt 12",fg = "white",bg = "black", command=SaveTask).pack(pady = 10)

LoadTask()
root.mainloop()