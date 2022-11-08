from tkinter import *

def seleccionar():
  monitor.config(text="{}".format(opcion.get()))

def reset():
  opcion.set(None)
  monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)

Radiobutton(root, text= 'Adidas', variable=opcion, value='Adidas', command=seleccionar).pack(anchor=W)

Radiobutton(root, text= 'Nike', variable=opcion, value='Nike', command=seleccionar).pack(anchor=W)

Radiobutton(root, text= 'Reebook', variable=opcion, value='Reebook', command=seleccionar).pack(anchor=W)

Radiobutton(root, text= 'Puma', variable=opcion, value='Puma', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text='Reiniciar', command=reset).pack()

root.mainloop()
