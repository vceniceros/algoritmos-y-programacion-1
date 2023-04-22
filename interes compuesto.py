def interes_compuesto(capital_inicial, tiempo_de_inversion, porcentaje_de_rentabilidad):
    #tu codigo
   
    for i in range(1,tiempo_de_inversion):
         porcentaje = capital_inicial * porcentaje_de_rentabilidad/100
        capital = capital_inicial + porcentaje
        ganancia_total= capital+porcentaje
        
    return ganancia_total
print(interes_compuesto(100,3,3))
