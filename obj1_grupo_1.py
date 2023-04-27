from tkinter import *

def ventana():
    raiz = Tk()
    raiz.title("login grupo 1")
    raiz.resizable(0,0)
    raiz.geometry("300x120")
    raiz.iconbitmap("bocajuniors.ico")
    raiz.config(bg="blue")
    raiz.mainloop()
def main():
    ventana()
    
main()