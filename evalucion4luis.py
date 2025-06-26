usuarios = {}

def validar_constraseña(contraseña):
    return len(contraseña) >=8 and""not in contraseña and any(l.ishalpha() for l in contraseña) and any(n.isdigit for n in contraseña)


def ingresar_usuario():
    try:
        while True:
            nombre = input("Ingrese su nombre").strip()
            if nombre in usuarios:
                print("nombre existente")
                continue
            
            sexo = input("Ingrese su sexo (M/F)").strip().upper()
            if sexo not in ("M","F"):
                print("sexo invalido")


            while True:
                contraseña = input("Ingrese su contraseña").strip()
                if validar_constraseña(contraseña):
                    break
                print("Contraseña invalida ingrese una que tenga 8 caracteres y que contenga 1 latra y un numero")

                contraseña[usuarios] = {"contraseña":contraseña,"sexo":sexo,}
                print("usuario añadido con exito")
                break
    except ValueError:
        print("")
     

      


def buscar_usuario(u):
    nombre = input("Ingrese el nombre a buscar").strip()
    if usuarios in nombre:

   
    print("usuario ingresado con exito")
        break



def eliminar_usuario():
    nombre = input("Ingrese el nombre a eliminar").strip()
    if nombre in usuarios:
        del usuarios[nombre]
        print("")



def menu(usuario):
    while True:
            print("***Menu***")
            opcion = input("Ingrese una opcion del 1 al 4")
            if opcion == "1":
                ingresar_usuario(usuario)
            elif opcion =="2":
                buscar_usuario(usuario)
            elif opcion =="3":
                eliminar_usuario(usuario)
            elif opcion =="4":
                print("Saliste del programa")
            else:
                print("Elija una opcion valida")
        
                


    


    

        
    


        
             
