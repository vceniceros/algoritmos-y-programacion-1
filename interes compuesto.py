def interes_compuesto(capital_inicial, tiempo_de_inversion, porcentaje_de_rentabilidad):
    """calcula el interes compuesto
    >>>interes_compuesto(100, 3,3)
     109,2727
    
    """
    #tu codigo
    porcentaje= 1.0+porcentaje_de_rentabilidad/100
    auxiliar = porcentaje**tiempo_de_inversion
    interes_final = auxiliar*capital_inicial
    
    return interes_final
print(interes_compuesto(100,3,3))