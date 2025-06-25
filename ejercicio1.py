lista_usuarios=[]

def menu():
    return

def ingresar_usuario():
    return

def buscar_usuario():
    return

def eliminar_usuario():
    return

def validar_usuario(nombre_usuario):
    for usuarios in lista_usuarios:
        if nombre_usuario in usuarios:
            print("El usuario ha sido ingresado anteriormente")
            return False
    print("Nombre de usuario valido")    
    return True

def validar_sexo(sexo_usuario):
    if sexo_usuario=="F" or sexo_usuario=="M":
        print("El sexo se ha ingresado correctamente")
        return True
    print("Seleccione una opción valida, M o F solamente.")
    return False

def validar_contraseña(contraseña_usuario):
    tiene_letras=False
    tiene_numeros=False
    tiene_espacios=False
    if len(lista_usuarios)<8:
        print("No comple con los requisitos")
        return False
    else:
        for caracter in contraseña_usuario:
            if lista_usuarios.isalpha():
                tiene_letras=True
            if lista_usuarios.isdigit():
                tiene_numeros=True
            if caracter== " ":
                
    return

print("###   Sistema de gestión de usuarios   ###")
menu()