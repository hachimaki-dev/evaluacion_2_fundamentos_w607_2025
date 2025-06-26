lista_usuario = []

def ingresar_usuario(nombre_usuario,sexo,contraseña):
    if sexo != "M" and sexo != "F":
        print("Porfavor ingrese M o F")
        return
    
    if validar_usuario(nombre_usuario):
        print(f"El usuario {nombre_usuario} ya existe")
        return

    if not validar_contraseña(contraseña):
        print("la contraseña no cumple los requisitos")
        print("- Mínimo 8 caracteres de longitud")
        print("- Al menos 1 número")
        print("- Al menos 1 letra")
        print("- No puede contener espacios en blanco")
        return
    
    usuario = {
        "nombre": nombre_usuario,
        "sexo": sexo,
        "contraseña": contraseña
    }
    lista_usuario.append(nombre_usuario)
    print("Usuario ingresado correctamente:")

def validar_contraseña(contraseña):
    if len(contraseña) >= 8:
        numeros = False
        letras = False
        espacios = False
        for caracteres in contraseña:
            if caracteres.isdigit():
                numeros = True
            if caracteres.isalpha():
                letras = True
            if caracteres == " ":
                espacios = True

        if numeros and letras and not espacios:
            print("Contraseña ingresada correctamente")
            return True
        else:
            print("contraseña invalida")
            return False
    else:
        print("La contraseña debe tener al menos 8 caracteres")
        return False

def validar_usuario(nombre_usuario):
    for usuario in lista_usuario:
        if nombre_usuario in usuario:
            return True
    return False

def buscar_usuario(nombre_usuario):
    for usuario in lista_usuario:
        if nombre_usuario in usuario:
            print("Usuario existente")
            return True
    print("Usuario no encontrado")
    return False
       
       
def eliminar_usuario(nombre_usuario):
    for usuario in lista_usuario:
        if nombre_usuario in usuario:
            lista_usuario.remove(usuario)
            print("Usuario eliminado")
            return True
    print("Usuario no encontrado")
    return False

def menu():
    print("***MENU PRINCIPAL***")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Elimnar usuario")
    print("4.- Salir")

while True:
    menu()
    try:
        opcion = int(input("eliga una opcion: "))
    except:
        print("Escoja una opcion valida")
        continue

    if opcion == 1:
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        sexo = input("Ingrese su sexo (M/F): ")
        contraseña = input("Ingrese su contraseña: ")
        ingresar_usuario(nombre_usuario, sexo, contraseña)

    elif opcion == 2:
        nombre_usuario = input("Nombre a buscar: ")
        buscar_usuario(nombre_usuario)

    elif opcion == 3:
        nombre_usuario = input("Nombre a eliminar: ")
        eliminar_usuario(nombre_usuario)

    elif opcion ==4:
        print("Gracias por utilizar nuestro programa, hasta luego.")
        break

    else:
        print("Opcion invalida.")


#profe no entendi si tenia que hacerle print en algun lado al usuario para que se vea el nombre, sexo y contraseña. pero si funciona ya lo probe con un print(usuario)