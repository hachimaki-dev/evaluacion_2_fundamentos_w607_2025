lista_usuarios = {}

def menu():
    print("\nMENU PRINCIPAL")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")

def ingresar_usuario():
    while True:
        nombre_usuario = input("Ingrese nombre de usuario: ")
        if not nombre_usuario:
            print("Nombre de usuario no válido, intente otra vez.")
        elif nombre_usuario in lista_usuarios:
            print("Usuario ya existe. Intente nuevamente.")
        else:
            break
    while True:
        sexo = input("Ingrese sexo: ").upper()
        if not sexo:
            print("Ingreso no válido, vuelva a intentar.")
        elif sexo == "M" or sexo == "F":
            print("Ingreso válido.")
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")
    while True:
        contraseña = input("Ingrese Contraseña: ")
        if validar_contra(contraseña):
            print("Contraseña válida.")
            break
        else:
            print("Contraseña no válida. Intente otra.")

    lista_usuarios[nombre_usuario]={"sexo":sexo, "contraseña":contraseña}
    print("Usuario ingresado con éxito!")


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
    nombre_usuario = input("Ingrese usuario a buscar: ")   
    if nombre_usuario in lista_usuarios:
        print(f"El sexo del usuario es: {lista_usuarios[nombre_usuario['sexo']]} y la contraseña es: {lista_usuarios[nombre_usuario]['contraseña']}")
    else:
        print("El usuario no se encuentra.")

def eliminar_usuario():
    nombre_usuario = input("Ingrese usuario a eliminar: ")
    if nombre_usuario in lista_usuarios:
        del lista_usuarios[nombre_usuario]
        print("Usuario eliminado con éxito.")
    else:
        print("No se pudo eliminar el usuario!")

while True:
    menu()
    try:
        opcion = input("Ingrese opción: ")
    except ValueError:
        print("Debe ingresar un numero válido.")
        continue
    if opcion == "1":
        ingresar_usuario()
    elif opcion == "2":
        buscar_usuario()
    elif opcion == "3":
        eliminar_usuario()
    elif opcion == "4":
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opcin valida")


