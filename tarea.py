milista=[1,2,3,4,5,6,7,8,9,10]
cont=0
i=0
j=0
h=0
print('Hola, yo soy una agenda amigable, soy capaz de guardar hasta 10 contactos.')
print('Por favor ingrece el nombre de sus amigos:')
for cont in range (0,10):
    print('Por favor ingrece el nombre ',cont+1,': ')
    nombre=input()
    for i in range (0,10):
        if milista[i] == nombre:
            rta=input('El nombre ingresado ya esta registrado,\n ¿desea incluirlo de todas formas? (si/no): ')
            if rta=='si':
                milista[cont]=nombre
            else:
                print('Por favor ingrece el nombre ',cont+1,': ')
                nombre=input()
        else:
            milista[cont]=nombre
for h in range (0,10):
    print('nombre ',h+1,': ',milista[h])
