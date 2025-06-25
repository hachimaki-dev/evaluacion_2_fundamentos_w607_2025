
usuarios = {
    "nombre de usuario": {
        "sexo": "M" or "F"
        "contraseña": "contraseña del usuario"
    }
}

while True:
    print("===Menu principal===")
    print("1.Ingresar usuario")
    print("2.Buscar usuario")
    print("3.Eliminar usuario")
    print("4.Salir del progarama")


    opcion = int(input("ingrese su opcion: "))


    if opcion == 1:
        usuarios = input("Ingrese nombre del usuario: ")
        contraseña = input("Ingrese la contraseña del usuario: ")
        sexo = input("cual es el sexo del usuario: ")

    elif opcion == 2:
        usuarios("cual es el nombre del usuario que busca?")

    elif opcion == 3:
        usuarios.remove = input("ingrese el nombre del usuario que quiere eliminar: ")
        print(usuarios)
        

    elif opcion == 4:
        print("fin del programa que tenga buen dia o tarde adios")
        break
    
print(usuarios)