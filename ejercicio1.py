lista_usuarios = []
import time
def ingresar_usuario(nombre_usuario, sexo, contraseña):
    validar_user=  validar_usuario(nombre_usuario)
    if validar_user:
        ("ERROR USUARIO EXISTENTE")
    else:
            validar_contra = validar_contraseña(contraseña)
            if validar_contra == False:
                print("ERROR")
            else:
                usuarios = {
                    nombre_usuario: {
                        "Sexo": sexo ,
                        "Contraseña" : contraseña
                    }
                }
                lista_usuarios.append(usuarios)
                print(lista_usuarios)

def buscar_usuario(nombre_usuario):
    for usuario in lista_usuarios:
        if nombre_usuario in usuario:
            print(f"USUARIO {nombre_usuario} DETECTADO")
            print("EL SEXO DEL USUARIO ES: ", usuario[nombre_usuario]["Sexo"])
            print("LA CONTRASEÑA ES: ", usuario[nombre_usuario]["Contraseña"])
        else:
            print("Usuario no encontrado")
    return

def eliminar_usuario(nombre_usuario):
        for usuario in lista_usuarios:
            if nombre_usuario in usuario:
                lista_usuarios.remove(usuario)
                print("usuario eliminado")
                print(lista_usuarios)
                return False
            else:
                print("USUARIO NO DETECTADO")
                return True
def validar_contraseña(contraseña):
    tiene_letras = False
    tiene_numeros = False
    tiene_espacios = False
    for iterar_contraseña in contraseña:
        if iterar_contraseña.isalpha():
            tiene_letras = True
        elif iterar_contraseña.isdigit():
            tiene_numeros = True
        elif iterar_contraseña == " ":
            tiene_espacios = True
    if tiene_numeros == True and tiene_letras == True and tiene_espacios == False:
        print("Usuario valido")
        return True
    else:
        print("CONTRASEÑA INVALIDA")
        return False

def validar_usuario(nombre_usuario):
    for usuario in lista_usuarios:
            if nombre_usuario in usuario:
                print("EL USUARIO EXISTE")
                return True
            elif nombre_usuario:
                print("USUARIO VALIDO")
                return False

def inicar_menu():
    while True:
        print("---BIENVENIDO---")
        print("1.-Ingresar usuario")
        print("2.-Buscar usuario")
        print("3.-Eliminar usuario")
        print("4.-Salir")
        try:
            opcion_user = int(input("\nINGRESE SU OPCION: "))
            if opcion_user == 1:
                nombre_usuario= input("Ingrese su nombre de usuario: ")
                sexo_usuario= input("Imgrese su sexo (F/M): ")
                if sexo_usuario != "F" and sexo_usuario != "f" and sexo_usuario != "M" and sexo_usuario != "m":
                    print("INGRESE UNA OPCION VALIDA")
                else:
                    contraseña_usuario = input("Ingrese su contraseña: ")
                    ingresar_usuario(nombre_usuario, sexo_usuario, contraseña_usuario)
            elif opcion_user == 2:
                nombre_usuario= input("INGRESE NOMBRE DE USUARIO A BUSCAR: ")
                buscar_usuario(nombre_usuario)
            elif opcion_user == 3:
                nombre_usuario = input("INGRESE NOMBRE DE USAURIO A ELIMINAR: ")
                eliminar_usuario(nombre_usuario)
            elif opcion_user > 4:
                ("INGRESE UNA OPCION VALIDA")
            else:
                print("Saliendo del programa...")
                time.sleep(1.4)
                return False
        except ValueError:
            print("INGRESE UNA OPCION VALIDA")



inicar_menu()