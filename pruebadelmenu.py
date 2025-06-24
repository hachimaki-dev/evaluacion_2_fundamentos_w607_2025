numeros= []
def menu():
    print("1.-ingresar n")
    print("2.-mostar mayor")
    print("3.-mostrar pedido")
    print("4.-salir")


while True:
    menu()
    try:
        opcion=int(input("ingrese una opcion: "))
    except ValueError:
        print("debe ingresar una opcion valida")
        continue

    if opcion==1:
        while True:
            try:
                numero=int(input("ingrese un numero: "))
                if 0 <= numero<=100:
                    numeros.append(numero)
                    print("numero agregado correctamente")
                    break
                else:
                    print("debe ingresar un numero entre 0 y 100")
            except ValueError:
                print ("debes ingresar un numero enteeeroo")

    elif opcion == 2:
        if numero:
            print("hasta ahora el mayor es: ", max(numeros))
        else:
            print("no se guardo n")

    elif opcion == 3:
        if numero:
            promedio = sum(numeros) / len(numeros)
            print (f"el promdio d los n ingresados es: {promedio:.2f}")
        else:
          print("no se han ingresado numeros")
    elif opcion ==4:
        print("fin del programa xaao")
        break
    else:
        print("debe elegir una opcion valida")