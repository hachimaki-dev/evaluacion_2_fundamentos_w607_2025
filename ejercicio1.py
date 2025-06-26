#inicio
listaUsuarios = []

#creamos una funcion para la opción ingresar usuario
def ingresarUsuario(nombreDeUsuario, sexo, contraseña):

    while True:
        try:
            #si el sexo es diferente de "M" o "F", el usuario tendrá que volver a intentar ingresar una contraseña
            if sexo != "M" and sexo != "F":
                print("Por favor, ingrese -F- para femenino o -M- para masculino")
                print("La contraseña no cumple con los requisitos, por favor, intentelo de nuevo")

            else:
                contraseñaEsCorrecta = validarContraseña
                #aca creamos un diccionario para lo solicitado
                if contraseñaEsCorrecta:
                    usuario = {
                        nombreDeUsuario : {
                            "sexo" : sexo,
                            "contraseña" : contraseña
                        }
                    }

                    listaUsuarios.append(usuario)
                    print("¡Usuario agregado exitosamente!")
                    print("Presione Enter para continuar")
                    input()

                else: 
                    #si el usuario ya existe, le pedimos que vuelva a intentar ingresando otro 
                    usuarioExiste = usuario
                    usuarioExiste
                    print("El usuario que ingresó ya existe, por favor, intente con otro")
                    print("Presione Enter para continuar")
                    input()                    
                
            return
        except ValueError:
            print("Por favor, ingrese datos validos")
#funcion para buscar usuarios
def buscarUsuario(nombreDeUsuario):
    for usuario in listaUsuarios:
        if nombreDeUsuario in usuario:
            print("**************************************************")
            print("El usuario que buscas sí existe")
            print("La contraseña de", nombreDeUsuario, "es", usuario[nombreDeUsuario]["contraseña"])
            print("El sexo de", nombreDeUsuario, "es", usuario[nombreDeUsuario]["sexo"])
            return

#funcion para eliminar usuarios
def eliminarUsuario(nombreDeUsuario):
    for nombreDeUsuario in listaUsuarios:
        if nombreDeUsuario in listaUsuarios:
            print("El usuario ha sido eliminado exitosamente")
            listaUsuarios.remove(nombreDeUsuario)
            print("Presione Enter para continuar")
            input()

        else:
            print("El usuario que intentas eliminar, no existe")
#funcion para validar que la contraseña cumpla con lo solicitado
def validarContraseña(contraseña):
    #si la contraseña es menor que 8
    if len(contraseña) < 8:
        print("La contraseña debe tener más de 8 carácteres")
    #si es mayor a 8
    else:
        tieneLetras = False
        tieneNumeros = False
        tieneEspacios = False
        
        for caracter in contraseña:
            if caracter.isalpha(): #tiene letras?
                tieneLetras = True
            elif caracter.isdigit(): #tiene numeros?
                tieneNumeros = True
            elif caracter == " ": #tiene espacios?


                #si la contraseña cumple con estos requisitos, se valida
                if tieneNumeros and tieneLetras and tieneEspacios == False:
                    return True
                #si tiene espacios, no
                elif tieneEspacios:
                    return False
 #funcion para validar el sexo del usuario       
def validarSexo(nombreDeUsuario):
    for usuario in listaUsuarios:
        if nombreDeUsuario in usuario:
            print("El sexo del usuario", nombreDeUsuario, "es", usuario[nombreDeUsuario]["sexo"] )
#funcion para mostrar un menú del programa
def mostrarMenu():
    print("**************************************************")
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")
    print("**************************************************")

#funcion para que el programa inicie
def inicioMenu():
    print("****Bienvenido al menú principal****")
    #invoco la funcion del menú
    mostrarMenu()

    while True:
        try:
            
            opciónElegida = int(input("Por favor seleccione una opción: "))

            if opciónElegida == 1:
                nombreUsuario = (input("Por favor, ingrese su nombre de usuario: "))
                sexo = (input("Por favor, seleccione su sexo: "))
                contraseña = (input("Por favor, ingrese su contraseña: "))
                ingresarUsuario(nombreUsuario, sexo, contraseña)
                mostrarMenu()

            elif opciónElegida == 2:
                nombre = input("Por favor, ingrese el nombre del usuario que desea buscar: ")
                buscarUsuario(nombreUsuario)
                mostrarMenu()

            elif opciónElegida == 3:
                nombre = input("Ingrese el nombre del usuario que desea eliminar: ")
                print("¡Usuario eliminado exitosamente!")
                eliminarUsuario(nombre)
                mostrarMenu()
            
            elif opciónElegida == 4:
                print("Saliendo del programa... Gracias por utilizar este código :)")
                break

            else:
                print("ERROR: Por favor, seleccione una opción válida")
                mostrarMenu()

        except ValueError:
            print("ERROR: Algo salió mal... ")
            mostrarMenu()
#finalmente, invocamos todo el programa 
inicioMenu()