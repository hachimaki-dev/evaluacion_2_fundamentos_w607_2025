numeros = []


def opcion_uno():
    while True:
        try:
            print("ingresa un numero entre 0 y 100")
            numero = int(input("Ingrese:"))
            if 0<= numero <= 100:
                numeros.append(numero)
                print("Ingreso exitoso")
                break
            else:
                print("Debe estar en el rango de 0 y 100")
                










while True:
    print("---MENU PRINCIPAL---")
    print("1. Ingresar un numero")
    print("2. Mostrar mayor")
    print("3. Mostrar promedio")
    print("4. salir")

    try:
        opcion_elegida = int(input("Elige una opcion"))
        if opcion_elegida == 1:
            opcion_uno()
        elif opcion_elegida == 2:
            opcion_dos()
        elif opcion_elegida == 3:
            opcion_tres()
        elif opcion_elegida == 4:
            print("##El progama termino##")
            break
    except ValueError:
        print("Debe ser entre la opcion 1 y 4")
