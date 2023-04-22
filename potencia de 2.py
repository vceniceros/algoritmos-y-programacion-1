def es_potencia_de_dos(numero):
    #tu codigo
      potencia = True
      auxiliar1 = 1
      if numero <= 0: 
           potencia = False
      while auxiliar1 < numero:
          auxiliar1 = auxiliar1 * 2
          if auxiliar1 != numero:
              potencia = False
          else:
                  potencia = True
      return potencia
           

n = int(input("ingrese numero: "))
print(es_potencia_de_dos(n))
