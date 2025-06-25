lista_usuarios = []

def ingresar_usuario(nombre_usuario, sexo, contraseña):
    usuarios = {
        nombre_usuario: {
            "Sexo": sexo ,
            "Contraseña" : contraseña
        }
    }
    validar_usuario(nombre_usuario)
    lista_usuarios.append(usuarios)
    return

def buscar_usuario():
    return

def eliminar_usuario(nombre_usuario):
        for usuario in lista_usuarios:
            if nombre_usuario in usuario:
                lista_usuarios.remove(usuario)
                print("usuario eliminado")
                print(lista_usuarios)
                break
            else:
                print("USUARIO NO DETECTADO")

def validar_contraseña(contraseña):
    tiene_letras = False
    tiene_numeros = False
    tiene_espacios = False
    for iterar_contraseña in contraseña:
        print(iterar_contraseña)
        if iterar_contraseña.isalpha():
            tiene_letras = True
        elif iterar_contraseña.isdigit():
            tiene_numeros = True
        elif iterar_contraseña == " ":
            tiene_espacios = True
    if tiene_numeros == True and tiene_letras == True and tiene_espacios == False:
        print("Contraseña valida")
    else:
        print("CONTRASEÑA INVALIDA")
    return

def validar_usuario(nombre_usuario):
    for iterar_usuario in lista_usuarios:
            if nombre_usuario in iterar_usuario:
                print("EL USUARIO EXISTE")
                print(iterar_usuario)
            else: 
                print("USUARIO VALIDO")
                print(iterar_usuario)
    return

def inicar_menu():
    return


ingresar_usuario("pepe", "M", "HOLA1234")
ingresar_usuario("benja", "M", "HOLA1234")
ingresar_usuario("juaco", "M", "HOLA1234")

eliminar_usuario("benja")
