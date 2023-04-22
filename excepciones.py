class PruebaException(Exception):
 pass
try: 
    raise PruebaException("esto es un error")
    print("todo mal")
except PruebaException as excepcion:
    print(excepcion)

print("esto no")