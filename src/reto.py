# Reto 1 : nivel - Basico
try:
    lista_notas=[]
    for x in range(5):
        notas=int(input("Ingrese las notas:"))
        lista_notas.append(notas)
    
except Exception as e:
    print( "La entrada es incorrecta: escribe un numero entero")

lista_notas.sort()
print(f'La mayor nota es: {lista_notas[-1]}')
print(f'La menor nota es: {lista_notas[0]}')
print(f'El promedio es: {sum(lista_notas)/len(lista_notas)}')
