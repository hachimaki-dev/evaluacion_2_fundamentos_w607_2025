usuarios = {}

def mostrar_menu():
    print(" MENU PRINCIPAL ")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if " " in contraseña:
        return False

def validar_sexo():
    while True:
        sexo = input("Ingrese el sexo (M/F): ").upper()
        if sexo in ["M", "F"]:
            return sexo
        print("Debe ingresar su sexo, Masculino (M) o Femenino (F)")

def ingresar_usuario():
    while True:
        nombre_usuario = input("Ingrese nombre de usuario: ")
        if nombre_usuario in usuarios:
            print("El usuario ya existe, ingrese otro nombre")
        else:
            break
    sexo = validar_sexo()

    while True:
        contraseña = input("Ingrese una contraseña: ")
        if validar_contraseña(contraseña):
            break
        print("Contraseña inválida")
        print("Debe tener mínimo 8 caracteres")
        print("Incluir al menos una letra, un número y no contener espacios.")
    usuarios[nombre_usuario] = {"sexo": sexo, "contraseña": contraseña}
    print(f"Usuario '{nombre_usuario}' ingresado correctamente.")

def buscar_usuario():
    nombre = input("Ingrese el nombre de usuario a buscar: ")
    if nombre in usuarios:
        print(f"Sexo: {usuarios[nombre]['sexo']}")
        print(f"Contraseña: {usuarios[nombre]['contraseña']}")
    else:
        print("Error, usuario no encontrado")

def eliminar_usuario():
    nombre = input("Ingrese el nombre de usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario ", nombre, " eliminado correctamente.")
    else:
        print("Error, usuario no encontrado")

def menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ingresar_usuario()
        elif opcion == "2":
            buscar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Ingrese una opción válida")

menu()
