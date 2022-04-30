import os
os.system("cls") 
print("Seleccine una opcion:")
print("1. suma")
print("2. resta")
print("3. producto")
print("4. cociente")
print("5. modulo")
print("6. potencia")

o =float(input("su opcion es :"))
a =float(input("ingrese un numero :"))

b =float(input("ingrese un numero dos :"))

if o==1: {
    print("la suma es",a+b)
}

if o==2: {
    print("la resta es",a-b)
}

if o==3: {
    print("la producto es",a*b)
}