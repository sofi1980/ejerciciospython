 
import math # tiene las funciones pi
radio =float(input("radio -> "))
area = math.pi* radio**2
longitud = 2 * math.pi* radio
#:.2f numeros de decimales
print(f"El area es: {area:.3f}")
print(f"La longitud de la circunferencia es: {longitud:.3f}")