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
        except ValueError:
            print("No puede ser decimal ni letras, solo numeros")
                

def opcion_dos():
    if numeros:
        max(numeros)
        print(f"El numero más grande es {max(numeros)} ")
    else:
        print("No se han ingresado numeros")



def opcion_tres():
    if numeros:
        promedio = sum(numeros)/len(numeros)
        print(f"El promedio es {promedio}")
    else:
        print("No se han ingresado numeros")
        




while True:
    print("---MENU PRINCIPAL---")
    print("1. Ingresar un numero")
    print("2. Mostrar mayor")
    print("3. Mostrar promedio")
    print("4. salir")

    try:
        opcion_elegida = int(input("Elige una opcion:"))
        if opcion_elegida == 1:
            opcion_uno()
        elif opcion_elegida == 2:
            opcion_dos()
        elif opcion_elegida == 3:
            opcion_tres()
        elif opcion_elegida == 4:
            print("###---FIN DEL PROGRAMA---###")
            break
        else:
            print("ingrese una opcion valida")
            continue
    except ValueError:
        print("Debe ingresar una opcion valida")
        continue
