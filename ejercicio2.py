def mostrar_menu():
    print("MENU PRINCIPAL")
    print("1. ingresar numero")
    print("2. mostrar mayor")
    print("3. mostrar promedio")
    print("4. salir")

def dar_numero():
    while True:
        try:
            numero = int(input("ingrese un numero (0 - 100) "))
            if numero >= 0 and numero <= 100:
                print("numero ingresado correctamente.")
                return numero
            else: 
                print("el numero debe estar entre 0 y 100")
        except ValueError:
            print("el numero ingresado debe ser entero")

def inicio():
    mostrar_menu()
    numeros = []
    while True:        
        try:
            opcion = int(input("elija una opcion "))
            if opcion == 1:
                numero = dar_numero()
                numeros.append(numero)
    
            elif opcion == 2:
                if numeros:
                    print("el numero mayor es:" , max(numeros)) 
                else: print("no se han ingresado numeros")

          

            elif opcion == 4:
                print("programa finalizado")
                break
            else:
                print("escoja una opcion valida")    

                

        except ValueError:
            print("la opcion debe ser un entero")
inicio()