# Reto 2 : nivel - Medio
try:
    alumnos=[]
    lista_notas=[]
    for a in range(3):
        nuevo_alumno=input('Ingrese nuevo alumno: ')
        alumnos.append(nuevo_alumno)
        print(f'######## Alumno: {alumnos[a]} ########')
        # Reto 1 : nivel - Basico
        for x in range(5):
            print(f'Ingrese la nota {x + 1}')
            notas=int(input("Ingrese las notas:"))
            if  0 <= notas <= 20:
                print('Nota correcta')
            else:
                print('Ingresar una nota entre 00 al 20')
                notas=int(input("Ingrese la nota correcta: "))
            lista_notas.append(notas)
        lista_notas.sort()
        alumnos_tupla=tuple(alumnos)
        print(f'######## Sus notas son: ########')
        print(f'La mayor nota es: {lista_notas[-1]}')
        print(f'La menor nota es: {lista_notas[0]}')
        print(f'El promedio es: {sum(lista_notas)/len(lista_notas)}')
    print(type(alumnos_tupla))
except Exception as e:
    print( "La entrada es incorrecta: escribe un numero entero")




