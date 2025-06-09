numero_rango =0
numero_rango =100
while True:
    print("MENU PRINCIPAL")
    print("1. ingresar el rango")
    print("2. mostrar numero mayor")
    print("3. mostrar promedio")
    seleccion = input("seleccione una opcion: ")
    if seleccion == "1":
        while True:
            try:
                numero = int(input("Ingrese número: "))
                if 0 <= numero <= 100:
                    numero_rango = numero
                    print(f"numero ingresado {numero_rango}")
                    break
                else:
                    print("su numero debe estar entre 0 y 100 intente de nuevo")
            except ValueError:
                print("Por favor ingrese un número válido")
    elif seleccion == "2":
        print(f"el numero mayor es {numero_rango}")
    elif seleccion == "3":
        if numero_rango > 0:
            promedio = numero_rango / 2
            print(f"el promedio es {promedio}")
        else:
            print("numero no valido para calcular el promedio")
    else:
        print("intente de nuevo")
        print("gracias por usar el programa")
        break



            
