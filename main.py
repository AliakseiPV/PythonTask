import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")


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


root.mainloop()