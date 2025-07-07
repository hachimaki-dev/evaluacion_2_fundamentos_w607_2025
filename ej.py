usuarios = {}
def mostrar_menu():
    print("MENU PRINCIPAL")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")
    return


def ingresar_usuario(nombre_usuario):
    while True:
        nombre_usuario = input("Ingrese nombre de usuario: ")
        if nombre_usuario in usuarios:
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
    usuarios[nombre_usuario] = {"sexo" : sexo.upper(),"contraseña" : contraseña}
    print("Usuario ingresado con exito")


def buscar_usuario(nombre_usuario):
    nombre_usuario = input("Ingrese usuario a buscar: ")
    if nombre_usuario in usuarios:
        print(f"El sexo del usuario es: {usuarios[nombre_usuario]["sexo"]} y la contraseña es: {usuarios[nombre_usuario]["contraseña"]}")
    else:
        print("El usuario no se encuentra.")


def eliminar_usuario(nombre_usuario):
    nombre_usuario = input("Ingrese usuario a eliminar: ")
    if nombre_usuario in usuarios:
        usuarios.pop(nombre_usuario)
        print("Usuario eliminado con exito")
    else:
        print("No se pudo eliminar el usuario!")


def validar_contraseña(contraseña):
    if len(contraseña) < 8:        
        return False
    if " " in contraseña:        
        return False
    num = False
    letra = False
    for letra in contraseña:
        if letra.isdigit():            
            num = True
        if letra.isalpha():            
            letra = True
    return num and letra


def validar_sexo(sexo):
    if sexo.upper() == "M" or sexo.upper() == "F":        
        return True
    else:        
        return False


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