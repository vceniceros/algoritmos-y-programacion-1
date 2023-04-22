cant = 0
peso = 1
acmpeso = 0
while cant <= 7 and acmpeso < 400 and peso !=0:
  peso = int(input("ingrese peso de la persona: "))
  acmpeso = acmpeso+peso
  cant = cant+1  
  if acmpeso > 400 :
     print("exceso de peso")
  else:
      if cant > 7:
          print("exceso de personas")
else:
    if cant <= 7 and acmpeso < 400:
        print("ascensor subiendo")
  
      
 
 
