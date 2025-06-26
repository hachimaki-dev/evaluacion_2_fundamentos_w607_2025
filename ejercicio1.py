nombres = []

def verificacionusuario(nombreusuario):
    for usuario in nombres:
        if nombreusuario in usuario:
            return False
    return True

def verificacionsexo(sexo):
    if sexo != "F" and sexo != "M":
        return False
    return True

def verificacioncontraseña(contraseña):
    if len(contraseña) < 8:
        print("La contraseña debe contener al menos 8 carateres. Intente de nuevo")
    else:
        letras = False
        numeros = False
        espacios = False
        for caracter in contraseña:
            if caracter.isalpha():
                letras = True
            elif caracter.isdigit():
                numeros = True
            elif caracter == " ":
                espacios = True
        if (letras and numeros == True) and (espacios == False):
            print("Contraseña válida")
            return True
        elif espacios == True:
            print("La contraseña no puede contener espacios. Intente de nuevo")
            return False
        else:
            print("La contraseña debe contener al menos 1 letra y 1 número. Intente de nuevo")
            return False

def op2():
    buscar = input("Ingrese usuario a buscar: ")
    buscado = False
    if len(nombres) == 0:
        print("No se han ingresado usuarios")
    for usuario in nombres:
        if buscar in usuario:
            print(f"El sexo del usuario es: {usuario[buscar]["sexo"]}")
            print(f"La contraseña del usuario es: {usuario[buscar]["contraseña"]}")
            buscado = True
    if buscado == False:
        print("Usuario no se encuentra")

def op3():
    eliminar = input("Ingrese usuario a eliminar: ")
    buscado = False
    if len(nombres) == 0:
        print("No se han ingresado usuarios")
    for usuario in nombres:
        if eliminar in usuario:
            nombres.remove(usuario)
            print("Usuario eliminado con éxito")
            buscado = True
    if buscado == False:
        print("Usuario no encontrado")

while True:
    try:
        print("\nMENU PRINCIPAL")
        print("1.- Ingresar usuario")
        print("2.- Buscar usuario")
        print("3.- Eliminar usuario")
        print("4.- Salir")
        opcion = int(input("Ingrese opción: "))
    
        

        if opcion == 1:
            while True:
                nombreusuario = input("Ingrese nombre de usuario: ")
                if verificacionusuario(nombreusuario):
                    break
                print("Usuario ya existe. Intente otro")

            while True:
                sexo = input("Ingrese sexo: ")
                if verificacionsexo(sexo):
                    break
                print("Debe ingresar M o F solamente. Intente de nuevo")

            while True:
                contraseña = input("Ingrese contraseña: ")
                if verificacioncontraseña(contraseña):
                    break

            usuarios = {
            nombreusuario: {
                "sexo": sexo,
                "contraseña": contraseña
                }
            }
            nombres.append(usuarios)
            print("Usuario ingresado con éxito")

        elif opcion == 2:
            op2()

        elif opcion == 3:
            op3()

        elif opcion == 4:
            print("Programa terminado...")
            break

        else:
            print("Por favor, ingrese una opción entre 1 y 4")

    except ValueError:
        print("Debe ingresar una opción válida")
        
        