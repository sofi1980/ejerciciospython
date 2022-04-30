
edad=int(input(f'\n digite su edad:'))
peso=int(input(f'\n digite su peso:'))
tension=int(input(f'\n digite su tension:'))
plaquetas=float(input(f'\n digite su plaquetas:'))
genero=input(f'\n digite su genero:')

if edad>=18 and edad<65:
    if peso>50 :
        if tension>50 and tension<100:
            if genero=='masculino' and plaquetas>13.5:
                print(f'aplica para donar sangre')
            else:  print(f'OJO NO puede  donar sangre')    
            if genero=='femenino' and plaquetas>12.5:
                print(f'aplica para donar sangre')
            else:  print(f'OJO NO puede  donar sangre')    
        else:  print(f'OJO NO puede  donar sangre')    
                
else:
    print(f'OJO NO puede  donar sangre')