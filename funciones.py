import pickle

usuario = ['Pepe']
contrasenias = ['Pepe123']

nombres = []
padres = []
notas = []
kiosko = []

arch_nombres = open('nombres.txt', 'w')
arch_padres = open('padres.txt', 'w')
arch_notas = open('notas.txt', 'w')
arch_kiosko = open('kiosko.txt', 'w')


def linea():
    print('+' + '-' * 60 + '+')


def opciones_iniciales():
    linea()
    print('|       Bienvenido a el programa seleccione una opcion       |')
    linea()
    opciones = ['Agregar alumno = 1', 'Sacar alumno = 2', 'Gestionar Quiosco = 3', 'Mostrar Alumnos = 4']
    for i in range(len(opciones)):
        print(opciones[i])


def ingresar_nuevo_alumno():
    nuevo_alumno = input('| Ingrese el nombre y apellido del alumno\n|>>>')
    padre = input('| Ingrese uno de sus padres\n|>>>')
    cant_notas = int(input('| Ingrese la cantidad de notas que quiere ingresar\n|>>>'))
    for i in range(cant_notas):
        materia = input('| Ingrese el nombre de la materia\n|>>>')
        nota = int(input(f'| Ingrese la nota de la materia {materia}\n|>>>'))
        notas.append(materia)
        notas.append(nota)
    nombres.append(nuevo_alumno)
    padres.append(padre)
    kiosko.append(0)


def sacar_alumno():
    alumno = input('Indique el nombre del alumno a sacar\n>>>')
    for i in range(len(nombres) - 1, -1, -1):
        aux = i + 1
        if nombres[i] == alumno:
            nombres.pop(i)
            padres.pop(i)
            notas.pop(i)
            notas.pop(aux)
            kiosko.pop(i)


def mostrar_alumnos():
    linea()
    print('|Nombre         |Padre          |Deuda |')
    for i in range(len(nombres)):
        print('|{:<15}|{:<15}|{:<6}|'.format(nombres[i], padres[i], 0))


def agregar_deuda():
    pass


def guardar_alumnos():
    for t in range(len(nombres)):
        arch_nombres.write(nombres[t] + ',')
        arch_padres.write(padres[t] + ',')
        arch_notas.write(notas[t] + ',')
        arch_kiosko.write(kiosko[t] + ',')

    arch_nombres.close()
    arch_padres.close()
    arch_notas.close()
    arch_kiosko.close()