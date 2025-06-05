
while True:
    print("*** MENU PRINCIPAL ***")
    print("1.- Ingresar número.")
    print("2.- Mostrar mayor.")
    print("3.- Mostrar promedio.")
    print("4.- Salir.")
    eleccion_usuario = int(input())
    numero_entero = 0

    if eleccion_usuario == 1:
        while True:
            try:
                numero_entero = int(input("Ingresa un numero entero del 0 al 100 "))
                if 0 <= numero_entero <=100:
                    print("Ingreso exitoso")
                    
                    break        
                else:
                     print("ingresa un numero entre 0 y 100")
            except ValueError:
                print("debe de ingresar un un numero entero")





