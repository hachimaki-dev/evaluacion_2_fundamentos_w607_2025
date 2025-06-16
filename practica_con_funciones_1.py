lista_de_usuarios = []

def ingresar_usuario(nombre_usuario):
    lista_de_usuarios.append(nombre_usuario)
    print(lista_de_usuarios)

def eliminar_usuario(nombre_usuario):
    lista_de_usuarios.remove(nombre_usuario)
    
def buscar_usuario(nombre_usuario):
    for i in lista_de_usuarios:
        if(i == nombre_usuario):
            break
        else:
            return False
    return True
    

ingresar_usuario("Juanito")
ingresar_usuario("Maria")
ingresar_usuario("Ana")
ingresar_usuario("Pepito")

eliminar_usuario("Ana")

ingresar_usuario("Raul")
buscar_usuario("Maria")

eliminar_usuario("Maria")
ingresar_usuario("Luigi")
buscar_usuario("Luigi")




