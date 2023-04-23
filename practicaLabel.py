from tkinter import *

root=Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

miNombre = StringVar()

cuadro_de_nombre = Entry(miFrame, textvariable=miNombre)
cuadro_de_nombre.grid(row=0,column=1,padx=10,pady=10)

nombreLable= Label(miFrame,text="Nombre:")
nombreLable.grid(row=0,column=0,sticky="e",padx=10,pady=10)

cuadro_de_apellido = Entry(miFrame)
cuadro_de_apellido.grid(row=1,column=1,padx=10,pady=10)

apellidoLable= Label(miFrame,text="Apellido:")
apellidoLable.grid(row=1,column=0, sticky="e",padx=10,pady=10)

cuadro_de_direccion = Entry(miFrame)
cuadro_de_direccion.grid(row=2,column=1,padx=10,pady=10)

direccionLable= Label(miFrame,text="Direccion:")
direccionLable.grid(row=2,column=0,sticky="e",padx=10,pady=10)
def sendButton():
    miNombre.set("valentino")

boton = Button(root, text="enviar", command=sendButton)
boton.pack()
root.mainloop()