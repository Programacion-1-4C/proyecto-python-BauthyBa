import pickle
nombres = ['Pepe']
contrasenias = ['Pepe123']
alumnos = [['Bauty', 'Barbero', ['Mate', 3, 'Lengua', 4] ]]
mayusculas = 'QWERTYUIOPASDFGHJKLZXCVBNM'
contador_mayusculas = 0




def opciones_iniciales():
    print('Bienvenido a el programa seleccione una opcion:')
    opciones = ['Agregar un alumno = 1', 'Sacar un alumno = 2', 'Gestionar Quiosco = 3' ]
    for i in range(len(opciones)):
        print(opciones[i])



def ingresar_nuevo_alumno():
    datos = []
    notas = []
    nuevo_alumno = input('Ingrese el nombre y apellido del alumno\n>>>')
    padre = input('Ingrese uno de sus padres\n>>>')
    decicion = int(input('Ingrese la cantidad de notas que quiere ingresar\n>>>'))
    for i in range(decicion):
        materia = input('Ingrese el nombre de la materia\n>>>')
        nota = int(input(f'Ingrese la nota de la materia {materia}\n>>>'))
        notas.append(materia)
        notas.append(nota)
    datos.append(nuevo_alumno)
    datos.append(padre)
    datos.append(notas)
    alumnos.append(datos)
    pickle.dump(alumnos, open('Alumnos.txt', 'wb'))

def sacar_alumno():
    cont = True
    indice = 0
    alumno = input('Ingrese el nombre y apellido del alumno\n>>>')
    while cont:
        if alumno in alumnos[indice][0]:
            alumnos.pop(indice)
            print(alumnos)
            break
        else:
            print('Pasando')
            indice += 1