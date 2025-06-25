lista_de_usuarios = []



name=[]

def agregar_usu(name, sexo, contraseña):
        usuarios = {
        name: {
                "sexo": sexo,
                "contraseña": contraseña
            }
        }
        lista_de_usuarios.append(usuarios)
        print(usuarios)
        return

def elimi(eliminar):
      print(eliminar)
      lista_de_usuarios.remove(eliminar)
      return
      

while True:
    print("---MENU---")
    print("1-ingresar usuario")
    print("2-buscar usuario")
    print("3-eliminar usuario")
    print("4-salir")
    opcion = int(input(print("ingrese una opcion")))



    if opcion == 1:
        name = input("ingrese nombre de usuario:")
        agregar_usu(name)


    if opcion == 2:
            if lista_de_usuarios:
                for i in lista_de_usuarios:
                    print(lista_de_usuarios)

    if opcion == 3:
        eliminar = input(print("ingrese usuario a eliminar"))
        elimi(eliminar)

    if opcion == 4:
           break
      

      
      


