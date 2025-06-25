usuarios = []
while True:
      try:

        print("---MENU---")
        print("1-ingresar usuario")
        print("2-buscar usuario")
        print("3-eliminar usuario")
        print("4-salir")
        opcion = int(input(print("ingrese una opcion")))



        if opcion == 1:
                def agregar_usu(usu_agregar):
                    name = input("ingrese nombre de usuario:")
                    usuarios.append(name)
                    print(usuarios)

        if opcion == 2:
                if usuarios:
                    for i in usuarios:
                        print(usuarios)