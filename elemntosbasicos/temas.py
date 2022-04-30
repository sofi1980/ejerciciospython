#tipado dinamico
"""
    se puede cambiar los datos
"""
from logging import logMultiprocessing
from pdb import Restart


suma=23
# division valor Floatante
# num1//num2  division entera
# num1%num2 === residuo
# exponencaicion: num1**num2 num2 valienfo 5 osea 2 a la 5
# resultado = 3**3 *(13/5-(2*4))
# 1. 2 *4
# 2.13/5
# 3. Resta
# 4
# 5.potencia 27
# 6.multiplicaicon 
# """suma=23333"""
# print(suma)
# operadores relacionales
#operador matematicos mayor prioridad que los relacionales

resultado =10 <20#true
resultado1 =10 == 20 # igualdad
print(resultado1)


#operadores logicos
#and or not
#pimreor not and y or de ultimo

#operadores de asigancion
a = 0 #declara variable y asignar
a +=5
a-=2
a*=3
a /=3
a**=2
a%=2

#str(3) '3'
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#salida de datos

nombre ='alejandro'
edad =23
print('hola',nombre,'tiendes',edad,'anos')
#format
print("hola{} tienes{} anos".format(nombre,edad))
print(f'hola {nombre} tienes{edad} anos')

#entrada de datos 
#input guarda nuro cadena

nombre=input('dogote su nombre')
print(f'hola {nombre}')
num=int(input('dogote su edad'))
print(f'hola {num}')
num=float(input('dogote su edad'))
# funcion str(34.5)
n= bin(10) # binario
n=hex(10) #hexamdecimal
#convertir binario a entero
n=int('oxa',16) #entero
n=int('ob1010',2)
n= abs()
n=round(5.6) #redondedar 6
a= float(input(f'digite la letra a:'))
b= float(input(f'digite la letra b:'))
c= float(input(f'digite la letra c:'))

resultado=(a**3 * (b**2 - 2*a*c))/2*b
print(f'resultad es {resultado}')
