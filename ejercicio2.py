numeros=[]

while True:
    print("*** Menú Principal ***")
    print("1.- Ingresar número.")
    print("2.- Mostrar mayor")
    print("3.- Mostrar promedio")
    print("4.- Salir")
    while True:
            try:
                print("Ingrese una opción")
                opcion=int(input())
                break
            except ValueError:
                print("Debe ingresar un número entero")
    if opcion==1:
        while True:
            try:
                print("Ingrese un número:")
                num=int(input())
                if 0<=num<=100:
                    numeros.append(num)
                    print("Se han ingresado correctamente los datos")
                    break
                else:
                    print("El número ingresado tiene que estar entre el 0 y el 100")
            except ValueError:
                print("Debe ingresar un número entero")
    elif opcion==2:
        if len(numeros)>0:
            print("El numero mayor es: ", max(numeros))
        else:
            print("No hay datos")
    elif opcion==3:
        if len(numeros)>0:
            suma_de_numeros=0
            for d in numeros:
                ##suma_de_numeros+=numeros(d)
                suma_de_numeros=sum(numeros)
            promedio = suma_de_numeros/len(numeros)
            print("El promedio de los números ingresados es: ",promedio)
        else:
            print("No hay datos")
    elif opcion==4:
        print("Cerrando el programa ...")
        break
    else:
        print("Opción invalida")