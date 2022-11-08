from tkinter import *

master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ['Luis', 'José', 'Juan', 'Lucía', 'Ana', 'Miguel']:
  listbox.insert(END, item)

listbox.pack()
label =Label(text='Lista de nombres')
label.pack()
master.mainloop()  