try:
    # Reto 3 : nivel - (Medio-Avanzado)
    cant_alumnos = int(input("Ingrese cantidad de alumnos: "))
    cant_notas = int(input("Ingrese cantidad de notas: "))
    # Reto 2 : nivel - Medio
    alumnos = []
    for a in range(cant_alumnos):
        nuevo_alumno = input('Ingrese nuevo alumno: ')
        #alumnos.append(nuevo_alumno)
        print(f'######## Alumno: {nuevo_alumno} ########')
        # Reto 1 : nivel - Basico
        lista_notas = []
        for x in range(cant_notas):
            while True:
                notas = int(input(f"Ingrese la nota {x + 1}:"))
                if  notas >= 0 and notas <= 20:
                    lista_notas.append(notas)
                    break
                else:
                    print('Ingresar una nota entre 00 al 20')
        
        alumnos.append({
            'alumno': nuevo_alumno,
            'notas': lista_notas
        })
    
    for v in alumnos:
        print("########################")
        print(f"Alumno : {v['alumno']}")
        print(f"Notas: {v['notas']}")
        print(f"Nota minima: {min(v['notas'])}")
        print(f"Nota maxima: {max(v['notas'])}")
        print(f"Nota promedio: {sum(v['notas'])/len(v['notas'])}")
        print(alumnos)
except KeyboardInterrupt as t:
    print("\nSe cerro la aplicacion")
#conversion = dict.fromkeys(alumnos_tupla,lista_notas[x])
'''print(alumnos_tupla)
print(lista_notas)
#print(conversion)
print(type(alumnos_tupla))
'''

