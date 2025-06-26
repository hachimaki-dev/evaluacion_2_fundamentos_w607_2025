lista_usuario = []

def ingresar_usuario(nombre_usuario, sexo, contraseña):
    if sexo != "M" and sexo != "F":
        print("ingrese un valor correcto, M para masculino y F para femenino")
    else:
        contraseña_correcta = validar_contraseñar(contraseña)
        if contraseña_correcta:
            usuario = {
                nombre_usuario : {
                    "sexo" : sexo,
                    "contraseña" : contraseña
                }
            }

            usuario_existe = validar_usuario(nombre_usuario)
            if usuario_existe:
                print("El usuario ya existe")
            else:
                lista_usuario.append(usuario)
        else:
            print("La contraseña no cumple con lo requerido")
    
    return

def buscar_usuario(nombre_usuario):
      for usuario in lista_usuario:
        if nombre_usuario in usuario:
            print("El usuario que buscas sí existe")
            print("la contraseña de", nombre_usuario, "es", usuario[nombre_usuario]["contraseña"])
            print("El sexo de", nombre_usuario, "es", usuario[nombre_usuario]["sexo"])
            return
        print("el usuario no existe")

def eliminar_usuario(nombre_usuario):
    for usuario in lista_usuario:
        if nombre_usuario in usuario:
            lista_usuario.remove(usuario)
        else:
            print("El usuario no existe ")
    return

def validar_contraseñar(contraseña):
     if len(contraseña) < 8:
        return False
     if " " in contraseña:
        return False
     if not any(caracter.isdigit() for caracter in contraseña):
        return False
     if not any(caracter.isalpha() for caracter in contraseña):
        return False
     return True

def validar_usuario(nombre_usuario):
    for usuario in lista_usuario:
        if nombre_usuario in usuario:
            print("El usuario" , nombre_usuario, " si existe")
            return True
    return False

def mostrar_menu():
    while True:
        print("MENU PRINCIPAL")
        print("1.- Ingresar usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir.")
        try:
            opcion_elegida = int(input("Ingresa que desea hacer"))
            if opcion_elegida >= 5:
                return
            break
        except:
            print("por favor ingrese una opcion valida ")
    while True:
        if opcion_elegida == 1:
            nombre = input("Ingrese el nombre de usuario")
            sexo = input("Ingrese el sexo del usuario ingresado (M/F)")
            contraseña = input("Ingrese la contraseña del usuario")
            ingresar_usuario(nombre, sexo, contraseña)
            return
        elif opcion_elegida == 2:
            nombre = input("Ingrese el nombre de usuario que desea buscar ")
            buscar_usuario(nombre)
        elif opcion_elegida == 3:
            nombre = input("Ingresa el usuario que desea eliminar ")
            eliminar_usuario(nombre)
            
            
        elif opcion_elegida == 4:
            print("Saliendo del menu")
            
            
        return

mostrar_menu()

ingresar_usuario("Deiner", "M", "DEINER123345")
buscar_usuario("deiner")




