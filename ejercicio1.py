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
                while nombre == "":
                    nombre = input("Porfavor ingrese un nombre de usuario: ").strip()

                sexo = input("Porfavor ingrese sexo (F/f) para femenino / (M/m) para masculino: ").strip().lower()
                while (sexo == "") or (sexo != "f")  and (sexo != "m"):
                    sexo = input("Porfavor ingrese sexo (F/f) para femenino / (M/m) para masculino: ").strip().lower()

                print("bien echo")

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
                            print("")
            
            elif op == 2:
                print("en proceso")

            elif op == 3:
                print("en proceso")
            elif op == 4:
                print("en proceso")
            else:
                print("a")

        except ValueError:
            print("Error 400: Solo puedes ingresar numeros")


menu()