lista_usuario = []

def ingresar_usuario(usuario,nombre,sexo,contraseña):
    lista_usuario.append(usuario)

    nombre = input("Ingrese nombre de usuario:")
    sexo = input("Ingrese sexo:")
    contraseña = input("Ingrese contraseña:")

    usuarios= {
        "sexo": "M" or "F",
        "contraseña": "contraseña_del_usuario"
        }

def validar_sexo():
    print("")

def validar_contraseña(contraseña):
    if len(contraseña) >= 8:
        return
    else:
        print("Contraseña Muy Corta")

def buscar_usuario(buscar):
    for i in lista_usuario(buscar): 
       return
       
def eliminar_usuario(eliminar):
    lista_usuario in eliminar
    lista_usuario.remove(eliminar)
    return

def mostrar_menu(opcion,usuario):
    print("1.Ingresar usuario")
    print("2.Buscar usuario")
    print("3.Elimnar usuario")
    print("4.Salir")

    while True:
        opcion = input("Ingrese una opcion:")
    
        try:
            if opcion == "1":
                ingresar_usuario(usuario)

            elif opcion == "2":
                buscar_usuario(usuario)

            elif opcion == "3":
                eliminar_usuario(usuario)

            elif opcion == "4":
                print("Saliste del programa")
                break
            else:
                print("Debe ingresar una opción válida!")
        except ValueError:
            print("Caracteres Invalidos.")

mostrar_menu("","")



