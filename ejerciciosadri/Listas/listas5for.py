# c=['adriana lucia rincon forero rincon']
c =input('digite la cadena: ')
c1=c.split()
c1=list(map(str.upper,c1))
print(c1)
sinduplicado=set(c1)
print(sinduplicado)