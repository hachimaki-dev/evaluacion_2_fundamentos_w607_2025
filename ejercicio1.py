lista_de_usuario = []

def menu():
    op = 0
    while op != 4:
        try:
            print("MENU PRINCIPAL")
            print("1. Ingresar Usuario")
            print("2. Buscar Usuario")
            print("3. Eliminar Usuario")
            print("4. Salir")
            op = int(input("Porfavor Ingresa una Opcion del Menu: "))

            while op < 1 or op > 4:
                try:
                    op = int(input("Porfavor Ingresa una Opcion del Menu: "))
                except ValueError:
                    print("Error 400: Solo puedes ingresar numeros")
                
            if op == 1:
                nombre = input("Porfavor ingrese un nombre de usuario: ").strip()
                while nombre == "" or validar_usuario(nombre):
                    nombre = input("Porfavor ingrese un nombre de usuario: ").strip()

                sexo = input("Porfavor ingrese sexo (F/f) para femenino / (M/m) para masculino: ").strip().lower()
                while (sexo == "") or (sexo != "f")  and (sexo != "m"):
                    sexo = input("Porfavor ingrese sexo (F/f) para femenino / (M/m) para masculino: ").strip().lower()
                        
                password = input("Porfavor ingrese contraseña: ").strip()
                while True:
                    if len(password) < 8:
                        print("la contraseña debe tener minimo 8 caracteres")
                    elif " " in password:
                        print("la contraseña no debe contener espacios")
                    else:
                        tiene_letra = False
                        tiene_numero = False

                        for c in password:
                            if c.isalpha():
                                tiene_letra = True
                            elif c.isdigit():
                                tiene_numero = True
                        
                        if not tiene_letra:
                            print("La contraseña debe tener al menos un caracter")
                        elif not tiene_numero:
                            print("La contraseña debe tener al menos un numero")
                        else:
                            print("contraseña ingresada")
                            break

                    password = input("Ingrese contrraseña (minimo 8 caracteres minimo una letra y un numero): ").strip()
                ingresar_usuario(nombre,sexo,password)
            
            elif op == 2:
                nombre = input("Porfavor ingrese usuario a buscar: ")
                buscar_usuario(nombre)

            elif op == 3:
                nombre = input("Porfavor ingrese usuario a eliminar: ")
                eliminar(nombre)
            elif op == 4:
                print("Gracias por usuar el programa :).")
            else:
                print("Porfavor ingresa una opcion valida.")

        except ValueError:
            print("Error 400: Solo puedes ingresar numeros")

def validar_usuario(nombre):
    for usuario in lista_de_usuario:
        if nombre in usuario:
            print("Este nombre de usuario ya a sido ingresado")
            return True
    return False

def ingresar_usuario(nombre_usuario,sexo,password):
    usuario = {
        nombre_usuario: {
            "sexo": sexo,
            "password": password            
        }
    }
    lista_de_usuario.append(usuario)
    print("usuario ingresado correctamente")
    
def buscar_usuario(nombre_usuario):
    for usuario in lista_de_usuario:
        if nombre_usuario in usuario:
            print("el usuario que busca si existe")
            print("Usuario: ",nombre_usuario,usuario[nombre_usuario])
            return
    print("El usuario que busca no existe")

def eliminar(nombre_usuario):
    for usuario in lista_de_usuario:
        if nombre_usuario in usuario:
            lista_de_usuario.remove(usuario)
            print("El usuario a sido eliminado.")
            return True
    print("El usuario que busca no existe")
    
menu()