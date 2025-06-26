usuarios = {}

def mostrar_menu():
    print("Bienvenido al menú")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")
    return

def ingresar_usuario(nombre_user):
    while True:
        nombre_user = input("Ingrese nombre de usuario: ")
        if nombre_user in usuarios:
            print("Usuario ya existe. Intente otro. ")
            continue
        break
    while True:
        sexo = input("Ingrese sexo: ")
        if not validar_sexo(sexo):
            print("Debe ingresar M o F solamente. Intente de nuevo. ")
            continue
        else:
            sexo.upper()
            break
    while True:
        contraseña = input("Ingrese contraseña: ")
        if not validar_contraseña(contraseña):
            print("Contraseña no valida. Intente otra.")
            continue
        else:
            print("Contraseña valida.")
            break
    usuarios[nombre_user] = {"sexo" : sexo.upper(),
                             "contraseña" : contraseña}
    print("Usuario ingresado con exito")
            

def buscar_usuario(nombre_user):
    nombre_user = input("Ingrese usuario a buscar: ")
    if nombre_user in usuarios:
        print(f"El sexo del usuario es: {usuarios[nombre_user]["sexo"]} y la contraseña es: {usuarios[nombre_user]["contraseña"]}")
    else:
        print("El usuario no se encuentra.")

def eliminar_usuario(nombre_user):
    nombre_user = input("Ingrese usuario a eliminar: ")
    if nombre_user in usuarios:
        usuarios.pop(nombre_user)
        print("Usuario eliminado con exito")

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        print("#####1")
        return False
    if " " in contraseña:
        print("####2")
        return False
    num = False
    letra = False
    for letra in contraseña:
        if letra.isdigit():
            print("####1")
            num = True
        if letra.isalpha():
            print("####2")
            letra = True
    return num and letra

def validar_sexo(sexo):
    if sexo.upper() == "M" or sexo.upper() == "F":
        print("####V")
        return True
    else:
        print("####F")
        return False
    
def print_diccionario(usuarios):
    print(usuarios)
    
while True:
    mostrar_menu()
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Debe ingresar una opción valida")
        continue
    if opcion == 1:
        ingresar_usuario(usuarios)
    elif opcion == 2:
        buscar_usuario(usuarios)
    elif opcion == 3:
        eliminar_usuario(usuarios)
    elif opcion == 4:
        print("Saliendo del programa")
        break
    else:
        print("Debe ingresar una opción valida")