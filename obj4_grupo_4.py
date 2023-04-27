from tkinter import *
from tkinter import messagebox
def validar(usuario,clave):
        datos = {"juaco": "123456","tomasito": "rocha","nico": "mistica","martinez":"dibu","ceni":"bocayoteamo7","matias":"messi"}
        if usuario in datos and datos[usuario]== clave:
           messagebox.showinfo(title="success",message="Usuario y clave correctos")
        else: messagebox.showerror(title="error",message="los datos ingresados son incorrectos")

def ventana():
    raiz = Tk()
    raiz.title("login grupo 1")
    raiz.resizable(0,0)
    raiz.geometry("300x130")
    raiz.iconbitmap("bocajuniors.ico")
    raiz.config(bg="blue")
    
    login_frame = Frame(raiz,width="200", height="130",bg="yellow")
    login_frame.pack()
    
    usuario = Label(login_frame,text="Usuario alumno: ")
    usuario.grid(row=0, column=0,sticky="w",padx= 10,pady=10)
    
    clave = Label(login_frame,text="Clave: ")
    clave.grid(row =1, column=0,sticky="w",padx=10,pady=10)
    
    usuario_entry = Entry(login_frame,textvariable="usuario")
    usuario_entry.grid(row = 0, column=1,padx=10,pady=10)
    
    clave_entry = Entry(login_frame,textvariable="clave")
    clave_entry.grid(row = 1, column=1,padx=10,pady=10)
    clave_entry.config(show="*")
    
    
  
    ingresar_boton = Button(login_frame,text="Ingresar",command=lambda: validar(usuario=usuario_entry.get(),clave=clave_entry.get()))
    ingresar_boton.grid(row=2,column=0,padx=10,pady=10)
    raiz.mainloop()
def main():
    ventana()
    
main()