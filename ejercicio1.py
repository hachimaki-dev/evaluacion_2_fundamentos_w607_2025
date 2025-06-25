usuarios = {}

def menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

def validar_sexo():
    while True:
        sexo = input("Ingrese su sexo (M / F): ").upper()
        if sexo in ["M", "F"]:
            return sexo
        else:
            print("Debes ingresar Masculino o Femenino. Vuelve a intentarlo!")
            continue

def validar_contraseña():
    while True:
        contraseña = input("Ingresa tu contraseña")
        if (
            len(contraseña) >= 8 and
            any(c.isdigit() for c in contraseña) and
            any(c.isalpha() for c in contraseña) and
            ' ' not in contraseña
        ):
            print("Contraseña correcta!")
            return contraseña
        else:
            print("Contraseña incorrecta! Vuelve a intentarlo")

def ingresar_usuario():
    while True:
        usuario = input("Ingresa tu nombre de usuario: ")
        if usuario in usuarios:
            print("El usuario que ingresaste ya existe! Intenta con otro")
        else:
            break

        sexo = validar_sexo()
        contraseña = validar_contraseña()

        usuarios[usuario] = {
            "sexo":sexo,
            "contraseña":contraseña
        }
        print("Usuario ingresado con exito!")

def buscar_usuario():
    usuario = input("Ingresa el nombre de usuario que quieres buscar: ")
    if usuario in usuarios:
        print(f"El sexo del usuario es: {usuarios[usuario['sexo']]}")
        print(f"La contraseña del usuario es: {usuarios[usuario['contraseña']]}")
    else:
        print("El usuario no se encuentra o no se ha registrado todavía")

def eliminar_usuario():
    usuario = input("Ingresa el nombre del usuario que deseas eliminar: ")
    if usuarios.pop(usuario, None):
        print("El usuario se ha eliminado con exito")
    else:
        print("No se ha podido eliminar el usuario")

def main():
    while True:
        menu()
        try:
            opciones = int(input("Ingresa una opción entre el 1 - 4: "))
            if opciones == "1":
                ingresar_usuario()
            elif