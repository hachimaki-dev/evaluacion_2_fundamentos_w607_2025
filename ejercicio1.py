menu = True
lista_usuarios = []
def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre de usuario: ")
        existe = False
        for usuarios in lista_usuarios:
            if nombre in usuarios:
                existe = True
                break
        if existe:
            print("El usuario ya existe, intente otro")
        else:
            return nombre
def validar_genero():
    while True:
        genero = input('Ingrese el genero del usuario, "F" para femenino y "M" para masculino: ')
        if genero == "F" or genero == "M":
            return genero
        else:
            print('Debe ingresar "F" para femenino y "M" para masculino')
def validar_contraseña():
    while True:
        contraseña = input("Ingrese una contraseña: ")
        letras = False
        numeros = False
        espacios = False
        for c in contraseña:
            if c in "0123456789":
                numeros = True
            if c in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM":
                letras = True
            if c in " ":
                espacios = True
        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres")
        elif not numeros:
            print("Su contraseña debe contener numeros")
        elif not letras:
            print("Su contraseña debe contener letras")
        elif espacios:
            print("Su contraseña no debe tener espacios")
        else:
            print("Contraseña válida")
            return contraseña
def ingresar_usuario(nombre, genero, contraseña):
    usuarios = {
    nombre: {
        "sexo": genero,
        "contraseña": contraseña
        }
    }
    lista_usuarios.append(usuarios)
def buscar_usuario():
    nombre = input("Ingrese el usuario que desea buscar: ")
    for usuario in lista_usuarios:
        if nombre in usuario:
            print("El usuario que busca si existe.")
            print(f"Su sexo es: {usuario[nombre]["sexo"]}")
            print(f"Su contraseña es: {usuario[nombre]["contraseña"]}")
            return
    print("El usuario que desea buscar no se encuentra en la lista de usuarios")
def eliminar_usuario():
    nombre = input("Que usuario desea eliminar?: ")
    for usuario in lista_usuarios:
        if nombre in usuario:
            lista_usuarios.remove(usuario)
            print("Eliminando usuario...")
            return
    print("El usuario que quiere eliminar no existe")
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
            nombre = validar_nombre()
            genero = validar_genero()
            contraseña = validar_contraseña()
            ingresar_usuario(nombre, genero, contraseña)
            print("Usuario ingresado con exito!")
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