

usuarios = {
    "nombre_usuario" : "",
    "sexo":"",
    "contraseña":"",
}

def agregar_usu(usuarios):
     print(usuarios)


def elimi(usuarios):
      print(usuarios)
      return
      

while True:
    while True:
          try:
            print("---MENU---")
            print("1-ingresar usuario")
            print("2-buscar usuario")
            print("3-eliminar usuario")
            print("4-salir")
            opcion = int(input(print("ingrese una opcion")))
            break
          except:
               print("ingrese un numero entero")



    if opcion == 1:
        usuarios["nombre_usuario"] = input("ingrese nombre de usuario:")
        usuarios["sexo"]=input("ingrese sexo:")
        usuarios["contraseña"]=input("ingrese contraseña:")
        agregar_usu(usuarios)

 
    if opcion == 2:
                buscar = input("ingrese usuario a buscar:")
                if buscar == usuarios["nombre_usuario"]:
                    print("el sexo del usuario es",usuarios["sexo"], "y la contraseña es",usuarios["contraseña"])    
                else:
                    print("el usuario no se encuentra")
                    

    if opcion == 3:
        eliminar = input(print("ingrese usuario a eliminar:"))
        if eliminar == usuarios["nombre_usuario"]:
            del eliminar,usuarios["nombre_usuario"]
            print("usuario eliminado con exito")
        else:
            print("no se pudo eliminar el usuario!")

    if opcion == 4:
           break
      

      
      


