lista_deusuarios = []

def ingresar_usuario(nombre, sexo, contraseña):
    if sexo != "M" and sexo != "F":
        print("Ha ocurrido un error al ingresar el sexo")
        print("Debe escribir 'M' para masculino o 'F' para femenino. Intente de nuevo.")
        return

    contraseña_es_valida = validar_contraseña(contraseña)
    if contraseña_es_valida == False:
        print("La contraseña no es válida. Debe tener al menos 8 caracteres, contener letras y números, y no tener espacios.")
        return

    usuario_existe = validar_usuario(nombre)
    if usuario_existe:
        print("El usuario ingresado ya existe")
        return

    usuario = {
        "nombre": nombre,
        "sexo": sexo,
        "contraseña": contraseña
    }
    lista_deusuarios.append(usuario)
    print("Usuario fue ingresado correctamente.")

def buscar_usuario(nombre_usuario):
    for usuario in lista_deusuarios:
        if nombre_usuario == usuario["nombre"]:
            print("El usuario que estás buscando existe")
            print("Contraseña:", usuario["contraseña"])
            print("Sexo:", usuario["sexo"])
            return
    print("El usuario no existe.")

def eliminar_usuario(nombre_usuario):
    for usuario in lista_deusuarios:
        if usuario["nombre"] == nombre_usuario:
            lista_deusuarios.remove(usuario)
            print("El usuario fue eliminado correctamente")
            return
    print("No se pudo eliminar el usuario, el usuario no existe")   

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    tiene_letras = False
    tiene_numeros = False
    tiene_espacios = False
    for caracter in contraseña:
        if caracter.isalpha():
            tiene_letras = True
        elif caracter.isdigit():
            tiene_numeros = True
        elif caracter == " ":
            tiene_espacios = True
    if tiene_espacios:
        print("La contraseña no debe contener espacios.")
        return False
    if tiene_letras and tiene_numeros:
        print("Contraseña válida.")
        return True
    return False

def validar_usuario(nombre_usuario):
    for usuario in lista_deusuarios:
        if usuario["nombre"] == nombre_usuario:
            return True
    return False

def mostrar_menu():
    while True:
        print("--- Menú Principal ---")
        print("1 - Ingresar usuario")
        print("2 - Buscar usuario")
        print("3 - Eliminar usuario")
        print("4 - Salir")

        try:
            opcion = input("Seleccione una opción: ")
        except ValueError:
            print("Debe ingresar una opción válida")
            continue

        if opcion == "1":
            nombre = input("Ingrese nombre de usuario: ")
            sexo = input("Ingrese su sexo ('F' para Femenino, 'M' para Masculino): ")
            contraseña = input("Ingrese contraseña: ")
            ingresar_usuario(nombre, sexo, contraseña)

        elif opcion == "2":
            nombre = input("Ingrese el nombre de usuario que quiere buscar: ")
            buscar_usuario(nombre)

        elif opcion == "3":
            nombre = input("Ingrese el nombre de usuario que desea eliminar: ")
            eliminar_usuario(nombre)

        elif opcion == "4":
            print("Programa finalizado. Has salido del sistema.......")
            break

        else:
            print("Debe escribir una opción entre el 1 y el 4")


mostrar_menu()