#creamos una lista para los juegos almacenados
listaDeJuegos = []

def ingresarVideojuego(nombreVideojuego, categoria, codigo):
    if categoria != "A" and categoria != "I":
        print("Por favor, ingrese un género de videojuego correcto: (A o I)")
        print("Presione la tecla Enter para continuar")
        input()
    else:
        ingresarVideojuego(codigo)
        if ingresarVideojuego:
            videojuego = {
                nombreVideojuego : {
                    "categoria" : categoria,
                    "codigo" : codigo
                }
            }

            videojuegoExiste = validarCodigoVideojuego(nombreVideojuego)
            if videojuegoExiste:
                print("El videojuego ya existe")
                print("Presione la tecla Enter para continuar")
                input()
            else:
                listaDeJuegos.append(nombreVideojuego)
        else: 
            print("El código no cumple con los requisitos, intentalo de nuevo")
            print("Presione la tecla Enter para continuar")
            input()
    return

def buscarVideojuego(nombreVideojuego):
    for videojuegos in listaDeJuegos:
        if nombreVideojuego in videojuegos:
            print("El videojuego si existe")
            print("El videojuego", nombreVideojuego, "pertenece a la categoría", videojuegos[nombreVideojuego]["categoria"])
            print("El codigo del videojuego", nombreVideojuego, "es", videojuegos[nombreVideojuego]["codigo"])
            print("Presione la tecla Enter para continuar")
            input()

def eliminarVideojuego(nombreVideojuego):
    for videojuegos in listaDeJuegos:
        if nombreVideojuego in videojuegos:
            listaDeJuegos.remove(nombreVideojuego)
            return True
        
def validarCodigoVideojuego(codigo):
    if len(codigo) < 8:
        print("El código del juego debe tener almenos 8 carácteres de longitud")
        print("Presione la tecla Enter para continuar")
        input()

    else:
        tieneNumeros = False
        tieneLetras = False
        tieneEspacios = False

        for caracter in codigo:
            if caracter.isalpha():  #Letras
                tieneLetras = True
            elif caracter.isdigit():  #Números
                tieneNumeros = True
            elif caracter == " ":  #Espacios
                tieneEspacios = True
                if tieneNumeros and tieneLetras and tieneEspacios == False:
                    return True
                else:
                    return False
                



def validarCategoriaVideojuego(categoriaVideojuego):
    for categoria in listaDeJuegos:
        if listaDeJuegos in categoria:
            print("El videojuego", categoriaVideojuego, "si existe")
            return True
        return False 
    






def iniciarPrograma():
    while True:
        print("Bienvenido al menú, por favor ingrese una opción para continuar")
        print("1. Ingresar videojuego")
        print("2. Buscar videojuego")
        print("3. Eliminar videojuego")
        print("4. Salir")
        try:
            opcion = int(input("Seleccione la opción que desee: "))

            if opcion == 1:
                while True:
                    nombreVideojuego = input("Ingrese el nombre del videojuego: ")
                    break
                    
                while True:
                    categoria = input("Por favor, ingrese un género de videojuego correcto: (A o I): ")
                    break

                while True:
                    codigo = input("Ingrese el código del videojuego: ")
                    ingresarVideojuego(nombreVideojuego, categoria, codigo)
                    

            elif opcion == 2:
                nombreVideojuego = input("Por favor, ingrese el nombre del videojuego que desee buscar: ")
                buscarVideojuego(nombreVideojuego)
                
            
            elif opcion == 3:
                nombreVideojuego = input("Por favor, ingrese el nombre del videojuego que desee borrar: ")
                eliminarVideojuego(nombreVideojuego)
                
            
            elif opcion == 4:
                print("Saliendo...")
                break

            else:
                print("ERROR: Por favor, ingrese una opción válida")

        
        except ValueError:
            print("ERROR: Por favor, ingrese un caracter válido")

               
iniciarPrograma()


