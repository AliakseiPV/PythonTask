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


root.mainloop()