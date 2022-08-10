nombres = []
contrasenias = []
alumnos = []
mayusculas = 'QWERTYUIOPASDFGHJKLZXCVBNM'
contador_mayusculas = 0


def nuevo_usuario(continuacion):
    while continuacion:
        contador_mayusculas = 0
        nombre_usuario = input('Ingrese nombre de usuario\n>>>')
        contrasenia = input('Escriba una contranenia\n>>>')
        for caracter in contrasenia:
            if caracter in mayusculas:
                contador_mayusculas += 1
            else:
                pass
        if contador_mayusculas > 0:
            print('Contrasenia valida, ya puede iniciar secion')
            print('-' * 50)
            contrasenias.append(contrasenia)
            nombres.append(nombre_usuario)
            break
        elif contador_mayusculas == 0:
            print('Contrasenia facil, ingrese por lo menos una mayuscula')


def verificacion(continuacion):
    intento = 0
    if intento == 5:
        pass
    else:
        validacion_nombre = input('Ingrese su nombre de usuario\n>>>')
        for i in nombres:
            if validacion_nombre == i:
                while intento < 3 and continuacion:
                    validacion_contrasenia = input('Ingrese su contrasenia\n>>>')
                    for j in contrasenias:
                        if validacion_contrasenia == j:
                            print('Inicio de sesion correcto')
                            intento = 5
                        else:
                            print('Contrasenia incorrecta')
                            intento += 1
                            intento_restantes = 3 - intento
                            print(f'Te quedan {intento_restantes} intentos')
                        if intento == 3:
                            break
            else:
                print('Nombre de usuario no identificdo')


def menu_inicio():
    print('Bienvenido a el programa seleccione una opcion:')
    opciones = ['Iniciar sesion = 1', 'Registrarse = 2',]
    for i in range(len(opciones)):
        print(opciones[i])


def inicio_de_secion():
    continuacion = True
    menu_inicio()
    decicion = int(input('>>>'))
    if decicion == 1:
        verificacion(continuacion)
    elif decicion == 2:
        nuevo_usuario(continuacion)

def opciones_iniciales():
    print('Bienvenido a el programa seleccione una opcion:')
    opciones = ['Agregar un alumno = 1', 'Sacar un alumno = 2', ]
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
        nota = int(input(f'Ingrese la nota de la materia {materia}'))
        notas.append(materia)
        notas.append(nota)
    datos.append(nuevo_alumno)
    datos.append(padre)
    datos.append(notas)
    alumnos.append(datos)
    print(alumnos)
