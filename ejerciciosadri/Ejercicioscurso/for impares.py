#contar  los numeros impares segun un limite establecido y generar
#la suma de dichos numeros-- utilizar el ciclo FOR
suma=0   
impar=0
limite=int(input("digite el limite: "))
if limite>0:
    for i in  range(0,limite):

         if i%2 !=0:
            impar+=1
            suma+=i
    print(f'la cantidad de nros impares es:{impar}')
    print(f'la suma de los nro impares es:{suma}')
else:
        print('digite un numero postitivo')
  



