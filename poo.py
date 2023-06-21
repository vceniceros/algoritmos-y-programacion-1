class Animal:
    __nombre = ""
    def __init__(self,nombre):
        self.__nombre = nombre
    def obtenerNombre(self):
        print("Mi nombre es: ",self.__nombre)
    def modificarNombre(self, nombre):
        self.__nombre = nombre

perro = Animal("Roco")

perro.obtenerNombre()
