import time

lista_usuarios = []

def validar_contraseña(contraseña):
    tiene_letras = False
    tiene_numeros = False
    tiene_espacios = False
    if contraseña.isalpha():
        tiene_letras = True
    if contraseña.isdigit():
        tiene_numeros = True
    for caracter in contraseña:
        if caracter == " ":
            tiene_espacios = True
    if len(contraseña) < 8:
        print("La contraseña debe ser de mas de 8 caracteres")
        return False
    if tiene_letras and tiene_numeros and tiene_espacios == False:
        print("Contraseña ingresada con exito")
        return True
    
def validar_sexo(sexo):
    if sexo != "M" and sexo != "F":
        return False
    else:
        return True

def eliminar_usuario(nombre_usuario):
    lista_usuarios.remove(nombre_usuario)
    return

def buscar_usuario(nombre_usuario):
    for usuario in lista_usuarios:
        if nombre_usuario in usuario:
            print(f"El usuario {nombre_usuario} si se encuentra en el sistema")
        else:
            print("El usuario no se encuentra en el sistema")

def ingresar_usuario(nombre_usuario, sexo, contraseña):

    usuarios = {
        nombre_usuario : {
            "sexo": "M" or "F",
            "contraseña": "contraseña_del_usuario"
        }
    }

    if nombre_usuario in lista_usuarios:
        print("No puedes ingresar un usuario que ya esta en el sistema")
    else:
        lista_usuarios.append(nombre_usuario)
        print("Usuario agregado con exito")
        return
    
    if validar_sexo(sexo) == False:
        print("El sexo debe ser M o F")
        return False
    else:
        print("Sexo agregado con exito")
        return True
    
    if validar_contraseña(contraseña) == False:
        print("La contraseña no es valida")
    else:
        print("Contraseña ingresada con exito")
    
    



def menu():
    print("====MENU PRINCIPAL====")
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

def main():
    while True:
        menu()
        try:
            opcion = int(input("Ingrese opcion: \n"))
        except ValueError:
            print("Porfavor ingrese un numero valido")
        if opcion in (1, 2, 3, 4):
            if opcion == 4:
                print("Saliendo del programa...")
                time.sleep(1.5)
                break
            elif opcion == 1:
                nombre = input("Ingrese el nombre del usuario: \n")
                sexo = input("Ingrese el sexo del usuario: \n")
                contraseña = input("Ingrese contraseña del usuario: \n")
                ingresar_usuario(nombre, sexo, contraseña)
            elif opcion == 2:
                nombre == input("Ingrese usuario a buscar: \n")
                buscar_usuario(nombre)
            elif opcion == 3:
                nombre = input("Ingrese usuario a eliminar: \n")
                eliminar_usuario(nombre)
        else:
            print("Ingrese un numero del 1 al 4")

if __name__ == "__main__":
    main()