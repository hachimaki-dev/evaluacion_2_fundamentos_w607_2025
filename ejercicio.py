lista_de_usuarios = []

def ingresar_usuario(nombre_usuario , sexo , contraseña_del_usuario):
    global lista_de_usuarios
    usuarios = {
        nombre_usuario: {
            "sexo": sexo ,
            "contraseña": contraseña_del_usuario
        }
    }
    
    
    for usuario in lista_de_usuarios:
        if nombre_usuario in usuario:
            print("El usuario existe")
            
        
    lista_de_usuarios.append(usuarios)
    print("Usuario ingresado con exito")
        
            
    
def validar_sexo(sexo):
    return sexo in ("F" , "M")




def buscar_usuario():
    nombre_usuario = input("Que usuario quiero buscar?:\n")
    for usuario in lista_de_usuarios:
        if nombre_usuario in usuario:
            print(f"sexo: {sexo} , contraseña: {contraseña_del_usuario}")
            return
    print("El usuario no se encuentra")

def eliminar_usuario():
    nombre_usuario = input("A que usuario quiere eliminar?:\n")
    for usuario in lista_de_usuarios:
        if nombre_usuario in usuario:
            lista_de_usuarios.remove(usuario)
            print("Usuario eliminado")
            return
    print("Error")
        

    



def validar_contraseña(contraseña_del_usuario):
    if len(contraseña_del_usuario) < 8:
        return False
    tiene_digito = False
    tiene_letra = False
    for caracter in contraseña_del_usuario:
        if caracter.isdigit():
            tiene_digito = True
        elif caracter.isalpha():
            tiene_letra = True
        if caracter.isspace():
            return False
    return tiene_digito and tiene_letra
        




while True:
    try:
        print("MENU PRINCIPAL")
        print("1. Ingresar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")

        opcion = int(input("Ingrese la opcion:\n"))
        if opcion == 1:
            print("Datos")
            print("El nombre no debe repetirse")
            nombre_usuario = input("Ingrese su usuario:\n")
            while True:
                sexo = input("Ingrese sexo(M O F)\n")
                if validar_sexo(sexo):
                    break
                else:
                    print("Debe ser M para masculino y F para femenino")

            print("Debe cumplir con los siguientes requisitos")
            print("Minimo 8 caracteres de longitud")
            print("Al menos un numero y una letra")
            print("No debe contener espacios en blanco")
            
            while True:
                contraseña_del_usuario = input("Ingrese su contraseña:\n")
                if validar_contraseña(contraseña_del_usuario):
                    break
                else:
                    print("Contraseña no valida")
            ingresar_usuario(nombre_usuario , sexo , contraseña_del_usuario)
            print(lista_de_usuarios)
        elif opcion == 2:
            buscar_usuario()
        elif opcion == 3:
            eliminar_usuario()
        elif opcion == 4:
            break
        else:
            print("Opcion no valida")
            continue
    except ValueError:
        print("Error")
        break
    