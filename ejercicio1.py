lista_usuario = []
def mostrar_menu():
    while True:
        print("BIENVENIDO A TU MENU PRINCIPAL")
        print("Menu principal")
        print("1.- Ingresar usuario")
        print("2.- Buscar usuario")
        print("3.- Eliminar usuario")
        print("4.- Salir del programa")
        try:
            opcion_elegida = int(input("Ingrese el menu "))
        except:
            print("Por favor ingrese una opcion correcta")
            continue
        if opcion_elegida == 1:
            nombre = input("Por favor ingrese nombre de usuario")
            while True:
                sexo = input("Por favor F para femenino o M para masculino")
                if validar_sexo(sexo):
                    sexo = sexo.upper()
                    break
            contraseña=input("Por favor ingrese contraseña del usuario")
            ingresar_usuario(nombre, sexo, contraseña)
        elif opcion_elegida == 2:
            nombre = input("Por favor ingrese nombre de usuario")
            buscar_usuario(nombre)
        elif opcion_elegida == 3:
            nombre = input("Por favor ingrese nombre de usuario a eliminar")
            eliminar_usuario(nombre)
        elif opcion_elegida == 4:
            salir_programa()
            break
        else:
            print("intente de nuevo")

def ingresar_usuario(nombre, sexo, contraseña):
    if sexo != "M" and sexo != "F":
        print("'M' para masculino  o 'F' para femenino")
    else:
        usuario= {
            'nombre': nombre,
            'sexo': sexo,
            'contraseña': contraseña
        }
        lista_usuario.append(usuario)
        print("Usuario ingresado correctamente")
    return
    
def buscar_usuario(nombre_usuario):
    for usuario in lista_usuario:
        if usuario['nombre'] == nombre_usuario:
            print("El usuario que buscas sí existe")
            print("El password de", nombre_usuario, "es", usuario["contraseña"])
            print("El sexo de", nombre_usuario, "es", usuario["sexo"])
            return
    print("El usuario no existe")
    return

def eliminar_usuario(nombre_usuario):
    for usuario in lista_usuario:
        if usuario["nombre"] == nombre_usuario:
            lista_usuario.remove(usuario)
            print("El usuario ha sido eliminado exitosamente")
            print("Presione Enter para continuar")
            input()
            return
    print("El usuario no existe")
    input()

def validar_sexo(sexo):
    if sexo == 'M' or sexo == 'F' or sexo == 'm' or sexo == 'f':
        return True
    else:
        print("Debe ser 'M' para masculino o 'F' para femenino.")
        return False  

def validar_contraseña(contraseña):
    if len(contraseña)>= 8: 
        return True
    else:
        print("la contraseña debe tener al menos 8 caracteres")
        return False
    
def salir_programa():
    print("gracias por usar el programa ingrese pronto")
    return


mostrar_menu()
