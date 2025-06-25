users = []

user = ""

passw = int

usuarios = {
    "nombre_usuario": user {
        "sexo": "M" or "F",
        "contraseña": passw
    }
}

def ingresar_user():
    print("Opción elegida: Ingresar usuario.")
    user = str(input("Ingrese nombre de usuario: "))
    for i in users:
        if user == i:
            print(f"El usuario {user} existe, Ingrese de nuevo a la opción del menú para intentar nuevamente.")
        else:
            print("No existe.")
    users.append(user)

def eliminar_user(user):
    print("Opción elegida: Eliminar usuario.")
    users.remove(user)
    return users

def buscar_user():
    print("Opción elegida: Buscar usuario.")
    user = input("Ingrese el nombre del usuario a buscar: ")
    for i in users:
        if user == i:
            print(f"El usuario {user} existe.")
            break
        else:
            print("No existe.")
    return


while True:
    print("/---------------------------/")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir") 
    
    try:
        numopc = int(input("Ingrese una opción para ingresar al menú (1-4): "))
        if numopc == 1:
            ingresar_user()
        elif numopc == 2:
            buscar_user()
        elif numopc == 3:
            eliminar_user()
        elif numopc == 4:
            print("Opción elegida: Salir.")
            print("Programa terminado...")
            exit()
        else:
            print("Opción no válida. Por favor ingrese una opción del 1 al 4.")
    except ValueError:
        print("Ingrese un número entero (1-4), y no texto.")