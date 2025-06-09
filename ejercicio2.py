#bucles/validar entradas/listas/mayor/promedio

num_list = []
while True:
    print("Bienvenido al menú principal.")
    print("1.-Ingresar número.")
    print("2.-Mostrar mayor.")
    print("3.-Mostrar promedio.")
    print("4.-Salir.")
    while True:
        try:
            option = int(input("Seleccione una opción: "))
            print(f"Se ha seleccionado la opción {option}")
            if option <= 0 or option > 4:
                print("Debe ingresar una opción válida.")
            else:
                break
        except ValueError:
            print("Debe ingresar una opción válida.")
    if option == 1:
        print("Ingrese un numero entero, puede ser del 0 hasta el 100")
        while True:
            try:
                num = int(input("Ingrese un número para agregar a la lista: "))
                if num < 0 or num > 100:
                    print("Debe ingresar una opción válida.")
                else:
                    num_list.append(num)
                    print(num_list)
                    break
            except ValueError:
                print("Debe ingresar una opción válida.")
    elif option == 2:
        print("Se mostrará el número más grande ingresado hasta el momento")
        print(max(num_list))
    elif option == 3:
        print("Se mostrará el promedio de los números ingresados")
        suma = sum(num_list)
        promedio = suma/(len(num_list))
        print(f"El promedio de la lista de numeros es {promedio}")
    elif option == 4:
        print("Fin del programa. Adiós.")
        break