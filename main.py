from functions import *


intento = 0
validacion_nombre = input('Ingrese su nombre de usuario\n>>>')
for i in nombres:
    if validacion_nombre == i:
        while intento < 3:
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


while True:
    if intento == 5:
        opciones_iniciales()
        decicion = int(input('>>>'))
        if decicion == 1:
            ingresar_nuevo_alumno()
        elif decicion == 2:
            sacar_alumno()
        elif decicion == 3:
            alumnosss = pickle.load(open('Alumnos.txt', 'rb'))
            print(alumnosss)
