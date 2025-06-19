lista_users = []

def insertar_user(nombre_user):
    print(nombre_user)
    lista_users.append(nombre_user)
    return lista_users

def eliminar_user(nombre_usuario):
    lista_users.remove(nombre_usuario)
    return lista_users

def buscar(nombre_usuario):
    
    for i in lista_users:
        if i == nombre_usuario:
            print("el usuario ", nombre_usuario, "si existe" ) 
            break
        else:
            print("usuario no encontrado")
    return


def iniciar_programa(opcion, usuario):
    while True:
        if opcion == 1:
            insertar_user(usuario)
            break
        if opcion == 2:
            buscar(usuario)
            break
        if opcion == 3:
            eliminar_user(usuario)
            break

opcion = int(input("Ingrese opcion"))
usuario= input("ingrese usuario")

while True:
    iniciar_programa(opcion, usuario)
    

