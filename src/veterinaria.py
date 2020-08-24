
cant_pacientes = int(input('Ingrese número de pacientes: '))

pacientes = []

for p in range(cant_pacientes):
    nuevo_paciente = input('Paciente nuevo: ')
    print(f'Paciente: {nuevo_paciente}')
    cant_mascotas = int(input(f'¿Cuantas mascotas tiene el paciente {nuevo_paciente}?: '))
    lista_mascotas = []
    for m in range(cant_mascotas):
        mascota = []
        nueva_mascota = input(f'Ingrese la {m + 1} mascota: ')
        altura = []
        nueva_altura = float(input(f'Altura de la {m + 1} mascota: '))
        peso = []
        peso_mascota = float(input(f'Peso de la {m + 1} mascota: '))

    pacientes.append({
        'paciente': nuevo_paciente,
        'mascota': {
        'nombre_mascota': nueva_mascota,
        'altura0': nueva_altura,
        'peso': peso_mascota
        }
    })

for v in pacientes:
    print("########################")
    print(f"Paciente : {v['paciente']}")
    print(f"Mascota: {v['mascota']}")
    print(pacientes)