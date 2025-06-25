usuarios = {}

def mostrar_el_menu():
    print(" ")
    print("═══════════════════════════════")
    print("═══════ MENU PRINCIPAL ════════")
    print("⋮ ➤  Seleccione una opción:   ⋮")
    print("═══════════════════════════════")
    print("⋮                              ⋮")
    print("⋮  1.- Ingresar usuario.       ⋮")
    print("⋮──────────────────────────────⋮")
    print("⋮  2.- Buscar usuario.         ⋮")
    print("⋮──────────────────────────────⋮")
    print("⋮  3.- Eliminar usuario.       ⋮")
    print("⋮──────────────────────────────⋮")
    print("⋮  4.- Salir.                  ⋮")
    print("⋮                              ⋮")
    print("═══════════════════════════════")
    print(" ")

def validar_contraseña(la_contraseña):
    if len(la_contraseña) < 8:
        return False
    if " " in la_contraseña:
        return False
    if not any(caracter.isdigit() for caracter in la_contraseña):
        return False
    if not any(caracter.isalpha() for caracter in la_contraseña):
        return False
    return True

def validar_sexo(sexo_del_usuario):
    return sexo_del_usuario in ["M", "F"]

def ingresar_usuario():
    global usuarios
    while True:
        print(" ")
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        if nombre_usuario in usuarios:
            print("⋮══════════════════════════════════════════════════════════════════════════⋮")
            print("⋮          El usuario ya existe. Ingrese un nombre diferente.              ⋮")
            print("⋮══════════════════════════════════════════════════════════════════════════⋮")
        else:
            break
    print(" ")
    sexo_del_usuario = input("Ingrese el sexo ( M / F ): ")
    print(" ")
    while not validar_sexo(sexo_del_usuario):
        print("⋮══════════════════════════════════════════════════════════════════════════⋮")
        print("⋮                   Sexo inválido. Debe ser 'M' o 'F'.                     ⋮")
        print("⋮══════════════════════════════════════════════════════════════════════════⋮")
        print(" ")
        sexo_del_usuario = input("Ingrese el sexo ( M / F ): ")
        print(" ")
    la_contraseña = input("Ingrese la contraseña: ")
    print(" ")
    while not validar_contraseña(la_contraseña):
        print("⋮════════════════════════════════════════════════════════════════════════════════════════⋮")
        print("⋮Contraseña inválida. Debe tener al menos 8 caracteres, 1 número, 1 letra y sin espacios.⋮")
        print("⋮════════════════════════════════════════════════════════════════════════════════════════⋮")
        print(" ")
        la_contraseña = input("Ingrese la contraseña: ")
        print(" ")
    usuarios[nombre_usuario] = {"sexo": sexo_del_usuario, "contraseña": la_contraseña}
    print("⋮═══════════════════════════════════════════════════════════════════════════════════════⋮")
    print(                     f"Usuario '{nombre_usuario}' ingresado exitosamente.                        ")
    print("⋮═══════════════════════════════════════════════════════════════════════════════════════⋮")

def buscar_usuario():
    global usuarios
    print(" ")
    nombre_usuario = input("Ingrese el nombre de usuario a buscar: ")
    print(" ")
    if nombre_usuario in usuarios:
        print("⋮════════════════════════════════════════════════════════════════════════════════════════════════════════════⋮")
        print(f"Usuario encontrado: {nombre_usuario}, Sexo: {usuarios[nombre_usuario]['sexo']}, Contraseña: {usuarios[nombre_usuario]['contraseña']}⋮")
        print("⋮═══════════════════════════════════════════════════════════════════════════════════════════════════════════ ⋮")
    else:
        print("═════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print("⋮                                         Usuario no encontrado.                                             ⋮")
        print("═════════════════════════════════════════════════════════════════════════════════════════════════════════════")

def eliminar_usuario():
    global usuarios
    print(" ")
    nombre_usuario = input("Ingrese el nombre de usuario a eliminar: ")
    print(" ")
    if nombre_usuario in usuarios:
        del usuarios[nombre_usuario]
        print("⋮══════════════════════════════════════════════════════════════════════════════⋮")
        print(                f"Usuario '{nombre_usuario}' eliminado exitosamente.                    ⋮")
        print("⋮══════════════════════════════════════════════════════════════════════════════⋮")
    else:
        print("⋮══════════════════════════════════════════════════════════════════════════════⋮")
        print("⋮                 Usuario no encontrado. No se puede eliminar.                 ⋮")
        print("⋮══════════════════════════════════════════════════════════════════════════════⋮")

def opciones_del_menu():
    while True:
        mostrar_el_menu()
        elegir_opcion = input("Ingrese una opción (1-4): ")
        if elegir_opcion == "1":
            ingresar_usuario()
        elif elegir_opcion == "2":
            buscar_usuario()
        elif elegir_opcion == "3":
            eliminar_usuario()
        elif elegir_opcion == "4":
            print("⋮═══════════════════════════════════════════════════════════════════════════════════════⋮")
            print("⋮                                 Saliendo del programa.                                ⋮")
            print("⋮═══════════════════════════════════════════════════════════════════════════════════════⋮")
            break
        else:
            print("⋮═══════════════════════════════════════════════════════════════════════════════════════⋮")
            print("⋮         Opción inválida. Por favor, ingrese una opción válida (1-4).                  ⋮")
            print("⋮═══════════════════════════════════════════════════════════════════════════════════════⋮")

def main():
    opciones_del_menu()

if __name__ == "__main__":
    main()