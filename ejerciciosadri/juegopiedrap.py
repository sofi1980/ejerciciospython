
j1=input(f'digite la jugada jugador 1: ')
# print(f'{j1}')


j2=input(f'digite la  jugador 2: ')
# print(f'{j2}')

if (j1=="piedra" and j2=="tijera"):
        print(f'gano jugador uno')
elif (j1=="tijera" and j2=="papel"):
    print(f'gano jugador uno')
elif (j1=="piedra" and j2=="tijera"):
    print(f'gano jugador dos')  
elif (j1=="piedra" and j2=="papel"):
    print(f'gano jugador dos') 
elif (j1=="piedra" and j2=="piedra"):
    print(f'vuelvan a jugar')  



    