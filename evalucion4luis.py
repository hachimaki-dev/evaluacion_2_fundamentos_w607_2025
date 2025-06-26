usuarios = {}

def validar_contraseña(contraseña):
    return (
        len(contraseña) >= 8 and
        " " not in contraseña and
        any(l.isalpha() for l in contraseña) and
        any(n.isdigit() for n in contraseña)
    )

def ingresar_usuario(nombre, sexo):
    try:
        if nombre in usuarios:
            print("Nombre existente.")
            return
        if sexo not in ("M", "F"):
            print("Sexo inválido.")
            return

       
        while True:
            contraseña = input("Ingrese su contraseña: ").strip()
            if validar_contraseña(contraseña):
                break
            print("Contraseña inválida. Debe tener al menos 8 caracteres, una letra, un número y sin espacios.")

        usuarios[nombre] = {"sexo": sexo, "contraseña": contraseña}
        print("Usuario añadido con éxito.")
    except:
        print("Error al ingresar usuario.")

def buscar_usuario(nombre):
    try:
        if nombre in usuarios:
            datos = usuarios[nombre]
            print(f"Usuario encontrado - Sexo: {datos['sexo']}, Contraseña: {datos['contraseña']}")
        else:
            print("Usuario no encontrado.")
    except:
        print("Error al buscar usuario.")

def eliminar_usuario(nombre):
    try:
        if nombre in usuarios:
            del usuarios[nombre]
            print("Usuario eliminado con éxito.")
        else:
            print("Usuario no encontrado.")
    except:
        print("Error al eliminar usuario.")

def menu():
    while True:
        try:
            print("\n*** Menú ***")
            print("1. Ingresar usuario")
            print("2. Buscar usuario")
            print("3. Eliminar usuario")
            print("4. Salir")
            opcion = input("Opción: ").strip()

            if opcion == "1":
                nombre = input("Ingrese su nombre: ").strip()
                sexo = input("Ingrese su sexo (M/F): ").strip().upper()
                ingresar_usuario(nombre, sexo)

            elif opcion == "2":
                nombre = input("Ingrese el nombre a buscar: ").strip()
                buscar_usuario(nombre)

            elif opcion == "3":
                nombre = input("Ingrese el nombre a eliminar: ").strip()
                eliminar_usuario(nombre)

            elif opcion == "4":
                print("Saliste del programa.")
                break

            else:
                print("Opción inválida.")
        except:
            print("Error en el menú.")

menu()

        
             
