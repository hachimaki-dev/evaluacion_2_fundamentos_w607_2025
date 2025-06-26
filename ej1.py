lista = []

def ingresar_user(nombre, sx, passw):
    print("Opción elegida: Ingresar usuario.")
    nombre = str(input("Ingrese nombre de usuario: "))
    sx  = str(input("Ingrese sexo del usuario (M/F): "))
    passw = str(input("Ingrese contraseñaS1: "))
    lista.append(nombre, sx, passw)
 
        
def eliminar_user(user):
    print("Opción elegida: Eliminar usuario.")
    lista.remove(user)
    return lista

def buscar_user():
    print("Opción elegida: Buscar usuario.")
    user = input("Ingrese el nombre del usuario a buscar: ")
    for i in lista:
        if user == i:
            print(f"El usuario {user} existe.")
            break
        else:
            print("No existe.")
            return False


while True:
    print("/---------------------------/")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir") 
    
    try:
        numopc = int(input("Ingrese una opción para ingresar al menú (1-4): "))
        if numopc == 1:
            ingresar_user(nombre, sx, passw)
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