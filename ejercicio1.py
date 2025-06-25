nombres = []

def op1(nombreusuario, sexo, contraseña):
    usuarios = {
        nombreusuario: {
            "sexo": sexo,
            "contraseña": contraseña
        }
    }
    nombres.append(usuarios)

def verificacionusuario():
    while True:
        nombreusuario = input("Ingrese nombre de usuario\n")
        if nombreusuario in nombres:
            print("Usuario ya existe. Intente otro")
        else:
            break

def verificacionsexo():
    while True:
        sexo = input("Ingrese sexo\n")
        if sexo != "F" and sexo != "M":
            print("Debe ingresar M o F solamente. Intente de nuevo")
        else:
            break

def verificacioncontraseña():
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