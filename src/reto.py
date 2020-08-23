try:
    # Reto 3 : nivel - (Medio-Avanzado)
    cant_alumnos= int(input("Ingrese cantidad de alumnos: "))
    cant_notas= int(input("Ingrese cantidad de notas: "))
    # Reto 2 : nivel - Medio
    alumnos=[]
    lista_notas=[]
    for a in range(cant_alumnos):
        nuevo_alumno=input('Ingrese nuevo alumno: ')
        alumnos.append(nuevo_alumno)
        print(f'######## Alumno: {alumnos[a]} ########')
        # Reto 1 : nivel - Basico
        for x in range(cant_notas):
            while True:
                print(f'Ingrese la nota {x + 1}')
                notas=int(input("Ingrese las notas:"))
                if  notas >= 0 and notas <= 20:
                    print('Nota correcta')
                    lista_notas.append(notas)
                    break
                else:
                    print('Ingresar una nota entre 00 al 20')
                    notas=int(input("Ingrese la nota correcta: "))  
        lista_notas.sort()
        alumnos_tupla=tuple(alumnos)
        print(f'######## Sus notas son: ########')
        print(f'La mayor de {alumnos[a]} nota es: {lista_notas[-1]}')
        print(f'La menor de {alumnos[a]} nota es: {lista_notas[0]}')
        print(f'El promedio de {alumnos[a]} es: {sum(lista_notas)/len(lista_notas)}')

except KeyboardInterrupt as t:
    print("\nSe cerro la aplicacion")
#conversion = dict.fromkeys(alumnos_tupla,lista_notas[x])
'''print(alumnos_tupla)
print(lista_notas)
#print(conversion)
print(type(alumnos_tupla))
'''

