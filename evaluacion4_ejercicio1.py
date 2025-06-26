lista_usuarios = []
 
def menu():
    print("MENU PRINCIPAL")
    print("1. ingresar usuario")
    print("2. buscar usuario")
    print("3. eliminar usuario")
    print("4. salir")
    
def ingreso_usuario(nombre_usuario, sexo, contraseña):
    if sexo != "M" and sexo != "F":
        print("por favor ingrese un valor correcto(M. Masculino/ F. Femenino)")
    else:
        contraseña_correcta = validar_contraseña(contraseña)
        if contraseña_correcta:

            usuario = {
                nombre_usuario:{
                    "sexo": sexo,
                    "contraseña": contraseña
                    
                }
            }
            usuario_existente = validar_usuario(nombre_usuario)
            if usuario_existente:
                print("el usuario ya existe")
            else:
                lista_usuarios.append(usuario)
        else:
            print("la contraseña no cumple los requisitos para ser creada")
    return
def validar_contraseña(contraseña):
    if len(contraseña) <= 8:
        print("la contraseña debe tener al menos 8 caracteres")
    else:
        numeros = False
        letras = False
        espacios = False
        for caracteres in contraseña:
            if caracteres.isdigit:
                numeros = True
            if caracteres.isalpha:
                letras = True
            if caracteres == " ":
                espacios = True
            
        if numeros and letras and espacios == False:
            print("contraseña ingresada correctamente")
            return True
        elif espacios:
            return False

def validar_usuario(nombre_usuario):
    for usuario in lista_usuarios:
        if nombre_usuario in usuario:
            print(f"el usuario {nombre_usuario} existe")
    return False

def buscar_usuario(nombre_usuario):
    for usuario in lista_usuarios:
        if nombre_usuario in usuario:
            print("el usuario si existe")
            print("la contraseña de", nombre_usuario, "es", usuario[nombre_usuario]["contraseña"])
            print("el sexo de", nombre_usuario, "es", usuario[nombre_usuario]["sexo"])
            return
    print("el usuario no existe")

def elminar_usuario(nombre_usuario):
    for usuario in lista_usuarios:
        if nombre_usuario in usuario:
            lista_usuarios.remove(usuario)
            return True
        
def opciones():
    while True:
        try:
            menu()
            opcion = int(input("elije una opcion "))
        except:
            print("escoja una opcion valida")

        if opcion == 1:
            nombre_usuario = input("ingrese el nombre de usuario ")
            sexo = input("ingrese su sexo ")
            contraseña = input("ingrese su contraseña")
            ingreso_usuario(nombre_usuario, sexo, contraseña)
        
        elif opcion == 2:
            nombre_usuario = input("¿que nombre deseas buscar? ")
            buscar_usuario(nombre_usuario)

        elif opcion ==3:
            nombre_usuario =input("ingrese el nombre que desea eliminar ")
            elminar_usuario(nombre_usuario)

        elif opcion == 4:
            break
opciones()