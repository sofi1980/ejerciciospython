#tienda milena
valorc=float(input('digite el valor de compra: '))
print(valorc)
if valorc>50000:
    balota=input('digite su color: ')
    print(balota)
    if balota =="roja":
        descuento=valorc*1
        valorfinal=valorc-descuento
        print('el descuento es:',descuento) 
        print('el valor a pagar  es:',valorfinal) 
    elif balota =="verde":
        descuento=valorc*0.5
        valorfinal=valorc-descuento
        print(f'el descuento es:{descuento}') 
        print(f'el valor a pagar es: {valorfinal}') 
    elif balota =="blanca":
        descuento=valorc*0.3
        valorfinal=valorc-descuento
        print(f'el descuento es:{descuento}') 
        print(f'el valor a pagar  es: {valorfinal}') 
    elif balota =="negra":
        descuento=valorc*0.2
        valorfinal=valorc-descuento
        print(f'el descuento es:{descuento}') 
        print(f'el valor a pagar  es: {valorfinal}') 
    elif balota =="amarilla":
        descuento=valorc*0.1
        valorfinal=valorc-descuento
        print(f'el descuento es:{descuento}') 
        print(f'el valor a pagar  es: {valorfinal}') 
        
else:
        print("no aplica nigun descuento , el valor de la compra es:",valorc)
            