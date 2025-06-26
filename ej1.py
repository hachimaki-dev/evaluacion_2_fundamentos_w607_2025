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
    if tiene_espacios:
        print("La contraseña no debe tener espacios")
        return False
    if len(contraseña) < 8:
        print("La contraseña debe ser de mas de 8 caracteres")
        return False
    if not (tiene_letras and tiene_numeros):
        print("La contraseña debe tener letras y numeros")
        return False
    return True
    
def validar_sexo(sexo):
    if sexo.upper() not in ("M", "F"):
        print("El sexo debe ser M o F")
        return False
    return True

def eliminar_usuario(nombre_usuario):
    nombre_usuario = nombre_usuario.lower()
    for usuario in lista_usuarios:
        if usuario["clave"] == nombre_usuario:
            lista_usuarios.remove(usuario)
            print(f"Usuario {usuario['nombre_original']} eliminado exitosamente")
            return 
    print("El usuario no se encuentra en el sistema")

def buscar_usuario(nombre_usuario):
    nombre_usuario = nombre_usuario.lower()
    for usuario in lista_usuarios:
        if usuario["clave"] == nombre_usuario:
            print("Usuario encontrado:")
            print(f"Nombre: {usuario['nombre_original']}")
            print(f"Sexo: {usuario['sexo']}")
            print(f"Contraseña: {usuario['contraseña']}")
            return
    print("El usuario no se encuentra en el sistema")

def ingresar_usuario(nombre_usuario, sexo, contraseña):
    clave_usuario = nombre_usuario.lower()

    for usuario in lista_usuarios:
            if usuario["clave"] == clave_usuario:
                print("No puedes ingresar un usuario que ya esta en el sistema")
                return
    
    if not validar_sexo(sexo) and not validar_contraseña(contraseña):
        print("Datos invalidos, el usuario no se ha podido ingresar")
        return

    usuarios = {
        "clave": clave_usuario,
        "nombre_original": nombre_usuario,
        "sexo": sexo.upper(),
        "contraseña": contraseña
    }
    lista_usuarios.append(usuarios)
    print("Usuario ingresado con exito")
    
    
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
            continue
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
            nombre = input("Ingrese usuario a buscar: \n")
            buscar_usuario(nombre)
        elif opcion == 3:
            nombre = input("Ingrese usuario a eliminar: \n")
            eliminar_usuario(nombre)
        else:
            print("Ingrese un numero del 1 al 4")

if __name__ == "__main__":
    main()