lista_de_usuarios = []

def ingresar_usuario(nombre_usuario, sexo, password):
    if sexo != "M" and sexo != "F":
        print("Por favor, ingrese un valor correcto. F para Femenino, M para Masculino")
    else:
        password_es_correcta = validar_password(password)
        if password_es_correcta: 
            usuario = {
                nombre_usuario : {
                    "sexo" : sexo,
                    "password" : password
                }
            }
            usuario_existe = validar_usuario(nombre_usuario)
            if usuario_existe:
                print("El usuario ya existe")
            else:
                lista_de_usuarios.append(usuario)
        else:
            print("La password no cumple con los requisitos")
    return

def buscar_usuario(nombre_usuario):
    for usuario in lista_de_usuarios:
        if nombre_usuario in usuario:
            print("El usuario que buscas sí existe")
            print("El password de", nombre_usuario, "es", usuario[nombre_usuario]["password"])
            print("El sexo de", nombre_usuario, "es", usuario[nombre_usuario]["sexo"])
            return
    print("El usuario no existe")


def eliminar_usuario(nombre_usuario):
    for usuario in lista_de_usuarios:
        if nombre_usuario in usuario:
            lista_de_usuarios.remove(usuario)
            return True

def validar_password(password):
    if len(password) < 8:
        print("El password debe tener mas de 8 caracteres")
    else:
        tiene_letras    = False
        tiene_numeros   = False
        tiene_espacios  = False
        for caracter in password:
            if caracter.isalpha():
                tiene_letras = True
            elif caracter.isdigit():
                tiene_numeros = True
            elif caracter ==  " ":
                tiene_espacios = True
        if tiene_numeros and tiene_letras and tiene_espacios == False:
            return True
        elif tiene_espacios:
            return False

def validar_usuario(nombre_usuario):
    for usuario in lista_de_usuarios:
        if nombre_usuario in usuario:
            print("El usuario" , nombre_usuario, " si existe")
            return True
    return False

def iniciar_programa():
    print("1 - Ingresar usuario")
    print("2 - Buscar usuario")
    print("3 - Eliminar Usuario")
    print("4 - Salir")
    while True:
            try:
                opcion_elegida = int(input("Ingrese que desea hacer"))
            except:
                print("Por favor ingrese una opcion valida")
    while True:
        if opcion_elegida == 1:
            nombre = input("Por favor ingrese nombre de usuario")
            sexo = input("Por favor F para femenino / M para masculino")
            password = input("Por favor ingrese el password del usuario")
            ingresar_usuario(nombre, sexo, password)
            break
        elif opcion_elegida == 2:
            nombre = input("Por favor ingrese nombre de usuario a buscar")
            buscar_usuario(nombre)
            break
        elif opcion_elegida == 3:
            nombre = input("Por favor ingrese nombre de usuario a eliminar")
            eliminar_usuario(nombre)
            break
        elif opcion_elegida == 4:
            break
        
iniciar_programa()

# Estudiantes deben terminar el codigo