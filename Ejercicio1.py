#SISTEMA GESTION DE USUARIOS

lista_usuarios = []

def ingresar_usuario(nombre_usuario, sexo, contrasena):
    if sexo != "M" and sexo != "F":
        print("Porfavor, ingrese un sexo valido M o F")
    else:
        contrasena_es_correcta = validar_contrasena(contrasena)
        if contrasena_es_correcta:
            print("La contraseña se ha guardado correctamente.")
            usuario = {
                nombre_usuario :{
                    "sexo": sexo,
                    "contrasena" : contrasena
                }
            }
            usuario_existe = validar_usuario(nombre_usuario)
            if usuario_existe:
                print("El usuario ya existe.")
            else:
                lista_usuarios.append(usuario)
        else:
            print("La contrasena no cumple con los requisitos.")
    return

def buscar_usuario(nombre_usuario):
    for usuario in lista_usuarios:
        if nombre_usuario in usuario:
            print("El usuario que buscas existe.")
            print("La contrasena de", nombre_usuario, "es", usuario[nombre_usuario]["contrasena"])
            print("El sexo de", nombre_usuario, "es", usuario[nombre_usuario]["sexo"])
            return
    print("El usuario no existe.")

def eliminar_usuario(nombre_usuario):
    for usuario in lista_usuarios:
        if nombre_usuario in usuario:
            lista_usuarios.remove(usuario)
            print("El usuario", nombre_usuario, "Se elimino.")
            return True
        
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        print("La contrasena debe tener minimo 8 caracteres.")
        return False
    else:
        tiene_letras = False
        tiene_numeros = False
        tiene_espacios = False
        for caracter in contrasena:
            if caracter.isalpha():
                tiene_letras = True
            elif caracter.isdigit():
                tiene_numeros = True
            elif caracter.isspace():
                tiene_espacios = True
        if tiene_espacios:
            print("La contrasena no debe tener espacios.")
            return False
        
        if not tiene_letras:
            print("La contrasena debe tener al menos una letra.")
            return False
        
        if not tiene_numeros:
            print("La contrasena debe tener al menos un numero.")

    return True

        
        
def validar_usuario(nombre_usuario):
    for usuario in lista_usuarios:
        if nombre_usuario in usuario:
            print("El usuario ya existe.")
            return True
    return False

def menu():
    print("Bienvenido al sistema de gestion de usuarios")
    while True:
        print("1. Ingresar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        try:
            opcion_elegida = int(input("Ingrese una opcion (1-4): "))
        except:
            print("Porfavor, ingrese un numero valido.")
            continue

        if opcion_elegida == 1:
            nombre = input("Ingrese nombre de usuario: ")
            sexo = input("Ingrese sexo (M/F): ").upper()
            contrasena = input("Ingrese una contrasena para su usuario: ")
            ingresar_usuario(nombre, sexo, contrasena)
        elif opcion_elegida == 2:
            nombre = input("Ingrese el nombre de usuario que desea buscar: ")
            buscar_usuario(nombre)
        elif opcion_elegida == 3:
            nombre = input("Ingrese el nombre de usuario que desea eliminar: ")
            eliminar_usuario(nombre)
        elif opcion_elegida == 4:
            print("saliendo del sistema...")
            break
        else:
            print("Porfavor, ingrese una opcion valida (1-4).")

menu()
        
