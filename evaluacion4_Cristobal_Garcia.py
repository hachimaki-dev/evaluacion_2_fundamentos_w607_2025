lista_de_usuarios = []

def ingresar_usuarios(nombre_usuario, contraseña, sexo):
    usuario_existe = validar_usuario(nombre_usuario)
    if usuario_existe:
        print("no se puede agregar un usuario que ya existe")
    else:
        if sexo != "M" or sexo != "F":
            print("Usuario agregado correctamente")
        else:
            contraseña_es_correcta = validar_contraseña(contraseña)
            if contraseña_es_correcta:
                usuario = {
                    nombre_usuario : {
                        "sexo" : sexo,
                        "contraseña": contraseña
                    }
                }
                lista_de_usuarios.append(usuario)
            else:
                print("La contraseña no cumple con lo requerido")
        return

def buscar_usuario(usuario):
    return

def eliminar_usuarios(usuario):
    for usuario in lista_de_usuarios:
     if usuario in usuario:
        lista_de_usuarios.remove(usuario)
    return

def validar_contraseña(contraseña):
    if len (contraseña) < 8:
        print("la contraseña debe tener más de 8 caracteres")
        return False
    else:
        tiene_letras    = False
        tiene_numeros   = False
        tiene_espacios  = False
        for caracter in contraseña:
            print(caracter)
            if caracter.isalpha():
                tiene_letras = True
            if caracter.isdigit():
                tiene_numeros = True
            if caracter == " ":
                tiene_espacios = True
            if tiene_numeros and tiene_letras and not tiene_espacios:
                return True
            elif tiene_espacios:
                return False

def validar_usuario(nombre_usuario):
    for usuario in lista_de_usuarios:
        if nombre_usuario in usuario:
           print("El usuario existe")
           return True
        else:
           print("el usuario no existe")
           return False
    
while True:
        print("===Menu principal===")
        print("1.Ingresar usuario")
        print("2.Buscar usuario")
        print("3.Eliminar usuario")
        print("4.Salir del progarama")


        opcion = int(input("ingrese su opcion: "))


        if opcion == 1:
            usuario = input("Ingrese nombre del usuario: ")
            contraseña = input("Ingrese la contraseña del usuario: ")
            sexo = input("cual es el genero del usuario F para femenino y M para masculino: ")
            ingresar_usuarios(usuario, sexo, contraseña)

        elif opcion == 2:
            usuario = input("cual es el nombre del usuario que busca?")
            buscar_usuario(usuario)

        elif opcion == 3:
            usuario = input("ingrese el nombre del usuario que quiere eliminar: ")
            eliminar_usuarios(usuario)
                    

        elif opcion == 4:
            print("fin del programa que tenga buen dia o tarde adios")
            break



