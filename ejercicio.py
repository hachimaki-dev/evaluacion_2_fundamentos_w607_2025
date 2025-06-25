lista_de_usuarios = []

def ingresar_usuario(nombre_usuario , sexo , contraseña_del_usuario):
    usuarios = {
    nombre_usuario: {
    "sexo": sexo ,
        "contraseña": contraseña_del_usuario
    }}
    for i in range(lista_de_usuarios):
        if i == nombre_usuario:
            print("El usuario ya existe")
        else:
            lista_de_usuarios.append(usuarios)
            
     


def buscar_usuario():
    print()

def eliminar_usuario():
    print()








while True:
    print("MENU PRINCIPAL")
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

    opcion = int(input("Ingrese la opcion:\n"))
    if opcion == 1:
        print("Datos")
        print("El nombre no debe repetirse")
        nombre_usuario = input("Ingrese su usuario:\n")
        sexo = input("Ingrese sexo(M para masculino y F para femenino)\n")
        print("Debe cumplir con los siguientes requisitos")
        print("Minimo 8 caracteres de longitud")
        print("Al menos un numero y una letra")
        print("No debe contener espacios en blanco")
        contraseña_del_usuario = input("Registra tu contraseña:\n")
        ingresar_usuario(nombre_usuario , sexo , contraseña_del_usuario)
        print(lista_de_usuarios)
    elif opcion == 2:
        buscar_usuario()
    elif opcion == 3:
        eliminar_usuario()
    elif opcion == 4:
        break
    