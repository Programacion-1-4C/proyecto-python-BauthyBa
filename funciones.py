import pickle


usuario = ['Pepe']
contrasenias = ['Pepe123']

salida = 0
siguiente_paso = 0
productos = []
stocks = []
nombres = []
padres = []
deudas = []


def linea():
    print('+' + '-' * 70 + '+')


def salto():
    print('\n'*20)


def opciones_iniciales():
    linea()
    opciones = ['Agregar alumno = 1', 'Mostrar Alumnos = 2', 'Gestionar Quiosco = 3']
    for i in range(len(opciones)):
        print(opciones[i])


def ingresar_nuevo_alumno():
    nuevo_alumno = input('Ingrese el nombre y apellido del alumno\n>>>')
    padre = input('Ingrese uno de sus padres\n>>>')
    deuda = input('Cuanta plata debe\n>>>')
    nombres.append(nuevo_alumno)
    padres.append(padre)
    deudas.append(deuda)
    pickle.dump(nombres, open('nombres.txt', 'wb'))
    pickle.dump(padres, open('padres.txt', 'wb'))
    pickle.dump(deudas, open('deudas.txt', 'wb'))


def sacar_alumno():
    alumno = input('Indique el nombre del alumno a sacar\n>>>')

    for i in range(len(nombres)):
        if nombres[i] == alumno:
            nombres.pop(i)
            padres.pop(i)
            deudas.pop(i)


def mostrar_alumnos():
    linea()
    print('|Nombre                   |Padre                    |Deuda             |')
    linea()
    lista_alumnos = pickle.load(open('nombres.txt', 'rb'))
    lista_padres = pickle.load(open('padres.txt', 'rb'))
    lista_deudas = pickle.load(open('deudas.txt', 'rb'))
    for i in range(len(lista_alumnos)):
        print('|{:<25}|{:<25}|{:<18}|'.format(lista_alumnos[i], lista_padres[i], lista_deudas[i]))


def gest_kiosko():
    limite = 0
    while salida == 0:
        if limite == 0:
            linea()
            limite = int(input('Establecer numero minimo de alerta\n>>>'))
            linea()
        operacion = input('| Que decea hacer? \nIngresar producto(ip)\nAgregar stock(ad)\nCambiar minimo de alerta(ma)\nOrdenare por Nombre(on)\nBuscar por Producto(bp)\nMostrar productos(mp)\nSalir(e)\n>>>')
        if operacion == 'ip':
            producto = input('Ingrese un producto\n>>>')
            productos.append(producto)
            stock = int(input('Ingrese el stock\n>>>'))
            if stock <= limite:
                print('Limite minimo de productos en este producto')
            stocks.append(stock)
        elif operacion == 'mp':
            indice = 0
            while indice < len(productos):
                producto = productos[indice]
                stock = stocks[indice]
                print("|{:<20}|{:>10.2f}|".format(producto, stock,))
                if stock <= limite:
                    print('Limite minimo de productos en este producto')
                print("+-------------------------------+")
                indice += 1
        elif operacion == 'ad':
            articulo_agregar = input('Que producto desea agregar cantidad?\n>>>')
            cantidad_agregar = int(input('Cuanto?\n>>>'))
            if articulo_agregar in productos:
                posision_producto = productos.index(articulo_agregar)
                valor_final = stocks[posision_producto] + cantidad_agregar
                stocks[posision_producto] = valor_final
            else:
                print("El artículo no existe")
        elif operacion == 'ma':
            limite = 0
        elif operacion == 'on':
            lugar_on = 0
            for producto in productos:
                lugar_producto = sorted(productos)
                elemento = lugar_producto[lugar_on]
                lugar_stock = productos.index(elemento)
                print("|{:<20}|{:>10.2f}|".format(lugar_producto[lugar_on], stocks[lugar_stock]))
                print("+-------------------------------+")
                lugar_on += 1
        elif operacion == 'bp':
            pos_producto = input('Que producto desea buscar: ')
            if pos_producto in productos:
                    print(f'Si hay: {pos_producto} y Tiene: {stock}')
            else:
                    print('No hay')
        elif operacion == 'e':
            print('Gracias por ejecutarme\nAdios')
            break
