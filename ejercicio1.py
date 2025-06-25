menu = True
lista_usuarios = []
def ingresar_nombre():
    nombre = input("Ingrese el nombre de usuario: ")
    for usuarios in lista_usuarios:
        if usuarios in lista_usuarios:
            print("No puede ingresar un usuario que ya existe: ")
        else:
            return nombre
def ingresar_genero():
    genero = input("Ingrese el genero de usuario: ")
    while True:
        if genero != "F" and genero != "M":
            print('Debe ingresar "F" para femenino o "M" para masculino')
        else:
            return genero
def ingresar_contraseña():
    contraseña = input("Ingrese una contraseña: ")
    return contraseña
def ingresar_usuario(nombre, genero, contraseña):
    usuarios = {
    nombre: {
        "sexo": genero,
        "contraseña": contraseña
        }
    }
    lista_usuarios.append(usuarios)
def buscar_usuario(usuarios):
    for usuarios in lista_usuarios:
        if usuarios in lista_usuarios:
            print("El usuario que busca si existe.")
        else:
            print("El usuario que busca no existe.")
def eliminar_usuario():
    for usuarios in lista_usuarios:
        if usuarios in lista_usuarios:
            lista_usuarios.remove(usuarios)
while menu:
    try:
        print("'''")
        print("MENU PRINCIPAL")
        print("1.- Ingresar usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir")
        print("'''")
        option = int(input("Seleccione una opción: "))
        print("''''")
        if option == 1:
            ingresar_usuario()
        elif option == 2:
            buscar_usuario()
        elif option == 3:
            eliminar_usuario()
        elif option == 4:
            menu = False
        else:
            print("Selección no válida.")
    except ValueError:
        print("Selección no válida.")