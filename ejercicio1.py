listausuarios = {}
def inicio():
    try:
        while True:
            print("=== MENU PRINCIPAL ===\n"
                "1.- Ingresar usuario.\n"
                "2.- Buscar usuario.\n"
                "3.- Eliminar usuario.\n"
                "4.- Salir.")
            opcion = int(input("Ingresa una opcion: "))
            if opcion == 1:
                ingresar_usuario()
            elif opcion == 2:
                buscar_usuario()
            elif opcion == 3:
                eliminar_usuario()
            elif opcion == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción válida!\n")
    except ValueError:
        print("Opcion invalida. Intente nuevamente\n")
        inicio()

def validar_sexo():
    while True:
        sexo = input("Ingrese sexo (M/F): ").upper()
        if sexo in ["M","F"]:
            return sexo
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")

def validar_contraseña():
    while True:
        contraseña = input("Ingrese contraseña: ")
        if len(contraseña) < 8:
            print("Error: Debe tener al menos 8 caracteres. Intente otra.")
        elif not any(c.isalpha() for c in contraseña):
            print("Error: Debe tener al menos 1 letra. Intente otra.")
        elif not any(c.isdigit() for c in contraseña):
            print("Error: Debe tener al menos 1 numero. Intente otra.")
        elif " " in contraseña:
            print("Error: No puede tener espacios en blanco. Intente otra.")
        else:
            print("Contraseña válida.")
            return contraseña

def ingresar_usuario():
    while True:
        usuario = input("Ingrese nombre de usuario: ").strip()
        usuario_upper = usuario.upper()
        if any(c.upper() == usuario_upper for c in listausuarios):
            print("Usuario ya existe. Intente otro.")
        elif usuario == "":
            print("Usuario invalido. Intente otro.")
        else:
            break
    sexo = validar_sexo()
    contraseña = validar_contraseña()
    listausuarios[usuario] = {
        "sexo":sexo,
        "contraseña":contraseña}
    print("Usuario ingresado con éxito!\n")

def buscar_usuario():
    usuario = input("Ingrese usuario a buscar: ")
    if usuario in listausuarios:
        print("El sexo del usuario es:",listausuarios[usuario]["sexo"])
        print("La contraseña del usuario es:",listausuarios[usuario]["contraseña"],"\n")
    else:
        print("El usuario no se encuentra.\n")

def eliminar_usuario():
    usuario = input("Ingrese usuario a eliminar: ")
    if usuario in listausuarios:
        del listausuarios[usuario]
        print("Usuario eliminado con éxito!\n")
    else:
        print("No se pudo eliminar el usuario!\n")
inicio()