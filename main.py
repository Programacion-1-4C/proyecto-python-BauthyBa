from funciones import *


intento = 0
while intento != 5:
    for i in usuario:
        validacion_nombre = input('Ingrese su nombre de usuario\n>>>')
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


while intento == 5:
    opciones_iniciales()
    decision = int(input('>>>'))
    if decision == 1:
        ingresar_nuevo_alumno()
    elif decision == 2:
        sacar_alumno()
    elif decision == 3:
        pass
    elif decision == 4:
        mostrar_alumnos()
    elif decision == 5:
        agregar_deuda()
    elif decision == 6:
        pass


