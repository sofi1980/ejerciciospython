# Escriba un programa en Python que compute el futuro valor de una cantidad de dinero,
# a partir del capital inicial, el tipo de interés y el número de años (solución).
# Entrada: capital=10000; interés=3.5; años=7
# 62 Capítulo 3. Tipos de datos
# Aprende Python
# Salida: 12722.792627665729

capital=10000
i=(3.5)/100
a=7
vf=capital*(1+i)**a
print('el vf es:',vf)