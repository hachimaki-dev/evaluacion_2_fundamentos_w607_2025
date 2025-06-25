usuarios = []
#Usando de base el codigo que hicimos con esto mismo pero con listas en vez de diccionarios
def mostrar_menu():
    print("Bienvenido al menú")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")
    return

def ingresar_usuario(nombre_usuario):
    print(nombre_usuario)
    usuarios.append(nombre_usuario)
    return usuarios

def buscar_usuario(nombre_usuario):
    if nombre_usuario in usuarios:
        print("Si esta")
    else:
        print("No esta")
    return

def eliminar_usuario(nombre_usuario):
    usuarios.remove(nombre_usuario)
    return

def validar_contraseña():
    return

def validar_sexo():
    return

print(ingresar_usuario("Diego"))
print(buscar_usuario("Hola"))
