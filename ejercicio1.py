usuarios = []


def mostrar_menu():
    # Menú con ciclo que maneja errores en el ingreso de opciones
    while True:

        print("MENU PRINCIPAL")
        print("1.- Ingresar usuario")
        print("2.- Buscar usuario")
        print("3.- Eliminar usuario")
        print("4.- Salir")

        try:
            n = int(input("Ingrese una opción: "))

            if n == 1:
                ingresar_usuario()

            elif n == 2:
                buscar_usuario()

            elif n == 3:
                eliminar_usuario()

            elif n == 4:
                print("Fin del programa.")
                break
            else:
                print("Ingrese una opción entre 1 y 4.\n")

        except ValueError:
            print("Ingrese un valor válido.\n")


def ingresar_usuario():
    print("\n-- Ingresar Usuario --")

    while True:
        nombre = input("Ingrese su nombre de usuario: ")
        # Se confima que el nombre no esté repetido a través de la función
        valido = validar_usuario(nombre)

        if valido:
            break

    while True:
        sexo = input("Ingrese su sexo (M o F): ").upper()
        # Se confirma el valor del sexo aceptando valores en minúscula
        sexo_valido = validar_sexo(sexo)

        if sexo_valido:
            break

    while True:
        contraseña = input("Ingrese su contraseña: ")

        contra_valida = validar_contraseña(contraseña)

        if contra_valida:
            break

    persona = {"nombre": nombre, "sexo": sexo, "contraseña": contraseña}
    usuarios.append(persona)
    print("Usuario creado correctamente.\n")


def validar_usuario(nombre):

    for persona in usuarios:
        # Ocupa la función lower para comparar correctamente
        if nombre.lower() == persona["nombre"].lower():
            print("El usuario está repetido.")
            return False

    return True


def validar_sexo(sexo):

    if sexo == "M" or sexo == "F":
        return True

    print("Error. Ingrese (M) de Masculino o (F) de Femenino.")
    return False


def validar_contraseña(contraseña): 

    tiene_letras = False
    tiene_numeros = False

    if len(contraseña) < 8:
        print("La contraseña debe tener mínimo 8 carácteres.")
        return False

    if " " in contraseña:
        print("La contraseña no puede tener espacios.")
        return False

    for letra in contraseña:
        if letra.isalpha():
            tiene_letras = True
        if letra.isdigit():
            tiene_numeros = True

    if not tiene_letras or not tiene_numeros:
        print("La contraseña debetener mínimo 1 letra o 1 número.")
        return False

    return True


def buscar_usuario():
    print("\n-- Buscar Usuario --")

    buscar = input("Ingrese el usuario que busca: ")

    for persona in usuarios:
        if buscar.lower() == persona["nombre"].lower():
            print(f"El usuario {persona["nombre"]} existe.")
            print(f"Sexo: {persona["sexo"]}")
            print(f"Contraseña: {persona["contraseña"]}\n")
            return

    print("El usuario que buscas no existe.\n")


def eliminar_usuario():
    print("\n-- Eliminar Usuario --")

    eliminar = input("Ingrese el usuario que desea eliminar: ")

    # Enumerate para evitar errores borrando en el mismo ciclo
    for i, persona in enumerate(usuarios):
        if eliminar.lower() == persona["nombre"].lower():
            print(f"El usuario {persona["nombre"]} ha sido eliminado.\n")
            del usuarios[i]
            # Elimina usando el índice obtenido
            return

    print("El usuario que buscas no existe.\n")

# Se ejecuta todo el código a través de la función que muestra el menú
mostrar_menu()

# git add .
# git commit -m "Avances clase miercoles 25"
# git push origin evaluacion4/paz_oyarzun