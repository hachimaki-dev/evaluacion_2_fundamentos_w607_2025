nombres = []

def op1(nombreusuario, sexo, contraseña):
    usuarios = {
        nombreusuario: {
            "sexo": sexo,
            "contraseña": contraseña
        }
    }
    nombres.append(usuarios)
    return

def verificacionusuario(nombreusuario):
    for usuario in nombres:
        if nombreusuario in usuario:
            print("Usuario ya existe. Intente otro")
    while True:
        nombreusuario = input("Ingrese nombre de usuario\n")
        break
    return

def verificacionsexo(sexo):
    while True:
        sexo = input("Ingrese sexo\n")
        if sexo != "F" and sexo != "M":
            print("Debe ingresar M o F solamente. Intente de nuevo")
        else:
            break
    return
def verificacioncontraseña(contraseña):
    while True:
        contraseña = input("Ingrese contraseña\n")
        if len(contraseña) > 8:
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
                break
            elif espacios == True:
                print("La contraseña no puede contener espacios. Intente de nuevo")
            else:
                print("La contraseña debe contener al menos 1 letra y 1 número. Intente de nuevo")
    return


while True:
    try:
        print("MENU PRINCIPAL")
        print("1.- Ingresar usuario")
        print("2.- Buscar usuario")
        print("3.- Eliminar usuario")
        print("4.- Salir")
        opcion = int(input("Ingrese opción: "))
        if opcion > 1 or opcion < 4:
            print("Por favor, ingrese una opción entre 1 y 4")
    except ValueError:
        print("Debe ingresar una opción válida")
        

    if opcion == 1:
        verificacionusuario()
        verificacionsexo()
        verificacioncontraseña()
        op1()

    elif opcion == 2:
        op1()
        buscar = input("Ingrese el nombre a buscar\n")
        for usuario in nombres: