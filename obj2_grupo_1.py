from tkinter import *

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
    usuario_entry = Entry(login_frame)
    usuario_entry.grid(row = 0, column=1,padx=10,pady=10)
    clave_entry = Entry(login_frame)
    clave_entry.grid(row = 1, column=1,padx=10,pady=10)
    clave_entry.config(show="*")
    raiz.mainloop()
def main():
    ventana()
    
main()