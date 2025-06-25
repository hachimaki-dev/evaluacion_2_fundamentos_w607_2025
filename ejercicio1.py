lista_usuarios = {}

def menu():
    print("\nMENU PRINCIPAL")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")

def ingresar_usuario(nombre_usuario, sexo, contraseña):
    while True:
        nombre_usuario = input("Ingrese nombre de usuario: ")
        if not nombre_usuario:
            print("Nombre de usuario no valido, intente otra vez")
        elif nombre_usuario in lista_usuarios:
            print("Nombre de usuario existente, intente nuevamente.")
        else:
            break
    while True:
        sexo = input("Ingrese sexo: ")
        if not sexo:
            print("Ingreso no valido, vuelva a intentar.")
        elif sexo == "M" or sexo == "F":
            print("Ingreso valido.")
            break
        else:
            print("")
    while True:
        contraseña = input("Ingrese Contraseña: ")
        if validar_contra(contraseña):
            break
        else:
            print("Contraseña no valida. Debe tener minimo 8 caracteres\n Al menos 1 letra \n 1 numero y sin espacios.")

    lista_usuarios[nombre_usuario]={"sexo":sexo, "contraseña":contraseña}
    print("Usuario ingresado existosamente!")


def validar_contra(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(c.isalpha() for c in contraseña):
        return False
    if not any(c.isdigit() for c in contraseña):
        return False
    if " " in contraseña:
        return False
    return True

def buscar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario que desea buscar: ")   
    if nombre_usuario in lista_usuarios:
        print("Usuario encontrado:")
        print(f"Nombre: {nombre_usuario}")
        print(f"Género: {lista_usuarios[nombre_usuario]['sexo']}")
        print(f"Contraseña: {lista_usuarios[nombre_usuario]['contraseña']}")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario")


