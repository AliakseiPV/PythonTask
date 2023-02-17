import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tkinter.END, task)
        entry.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(message="Enter a task.")

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except: 
        tkinter.messagebox.showwarning(message="Select a task.")   

def save_task():  
    tasks = listbox.get(0, listbox.size())
    pickle.dump(tasks, open("tasks.dat", "wb")) 

def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox.delete(0,tkinter.END)
        for task in tasks:
            listbox.insert(tkinter.END, task)
    except:   
        tkinter.messagebox.showwarning(message="No data file.")  

def clear_task():
      listbox.delete(0,tkinter.END)                

frame = tkinter.Frame(root)
frame.pack()

listbox = tkinter.Listbox(frame, height=10, width=50)
listbox.pack(side=tkinter.LEFT)

scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tkinter.Entry(root,width=50)
entry.pack()

button_add = tkinter.Button(root, text="Add", width=48, command=add_task)
button_add.pack()

button_delete = tkinter.Button(root, text="Deelete", width=48, command=delete_task)
button_delete.pack()

button_save = tkinter.Button(root, text="Save tasks", width=48, command=save_task)
button_save.pack()

button_load = tkinter.Button(root, text="Load tasks", width=48, command=load_task)
button_load.pack()

button_clear = tkinter.Button(root, text="Clear tasks", width=48, command=clear_task)
button_clear.pack()

root.mainloop()