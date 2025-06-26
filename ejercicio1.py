lista_usuarios=[]

def menu():
    while True:
        print("Menú principal")
        print("1.- Ingresar usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir.")
        opcion=filtro()
        if opcion==1:
            print("Para ingresar un nuevo usuario debe tener los siguientes criterios en cuenta")
            print("1. El nombre de usuario no tiene que existir en la base de datos.")
            print("2. Para seleccionar el sexo ocupe F para femenino y M para masculino.")
            print("3. La contraseña necesita un minimo de 8 caracteres, sin espacios y tanto letras como números.")
            ingresar_usuario()
        elif opcion==2:
            if len(lista_usuarios)>0:
                buscar_usuario(input("Ingrese el nombre de usuario que desea buscar: \n"))
            else:
                print("No hay datos")
                print("Volviendo al menu principal...")
        elif opcion==3:
            if len(lista_usuarios)>0:
                eliminar_usuario(input("Ingrese el nombre de usuario que desea eliminar: \n"))
            else:
                print("No hay datos")
                print("Volviendo al menu principal...")
        elif opcion==4:
            print("Cerrando el programa...")
            break

def filtro():
    while True:
        try:
            opcion=int(input("Ingrese una opción: \n"))
            if 1<=opcion<=4:
                return opcion
            else:
                print("Debe ingresar un número entero del 1 al 4.")
        except ValueError:
            print("Debe ingresar un número entero del 1 al 4.")

def ingresar_usuario():
    nuevo_usuario={
        validar_usuario():{
            "Sexo":validar_sexo(),
            "Contraseña":validar_contraseña()
        }
    }
    lista_usuarios.append(nuevo_usuario)
    print("El nuevo usuario ha sido ingresado correctamente.")

def buscar_usuario(nombre_usuario):
    for usuarios in lista_usuarios:
        for nombre in usuarios:
            if nombre_usuario.lower()==nombre.lower():
                print("Nombre de usuario encontrado.")
                print("Datos del usuario: ", usuarios[nombre])
                print("Volviendo al menu principal...")
                return
    print("Usuario no encontrado.")

def eliminar_usuario(nombre_usuario):
    for usuarios in lista_usuarios:
        for nombre in usuarios:
            if nombre_usuario.lower()==nombre.lower():
                print("Nombre de usuario encontrado.")
                print("Eliminando usuario...")
                lista_usuarios.remove(usuarios)
                print("Usuario eliminado correctamente. Volviendo al menú principal...")
                return
    print("Usuario no encontrado.")

def validar_usuario():
    while True:
        user=input("Ingrese el nombre de usuario: \n")
        existe=False
        for usuarios in lista_usuarios:
            if user in usuarios:
                existe=True
                break
        if existe:
            print("Nombre de usuaio invalido.")
        else:
            print("Nombre de usuario válido.")
            return user

def validar_sexo():
    while True:
        sexo=input("Ingrese el sexo del usuario, use F para femenino y M para masculino: \n")
        if sexo=="F" or sexo=="M":
            print("El sexo se ha ingresado correctamente.")
            return sexo
        else:
            print("Seleccione una opción valida, M o F solamente.")

def validar_contraseña():
    while True:
        contraseña=input("Ingrese una contraseña: \n")
        tiene_letras=False
        tiene_numeros=False
        tiene_espacios=False
        if len(contraseña)>=8:
            for caracter in contraseña:
                if caracter.isalpha():
                    tiene_letras=True
                if caracter.isdigit():
                    tiene_numeros=True
                if caracter.isspace():
                    tiene_espacios=True
            if tiene_letras and tiene_numeros and tiene_espacios==False:
                print("Contraseña valida.")
                return contraseña
            else:
                print("La contraseña no debe de tener espacios.")
        else:
            print("La contraseña no cumple con los requisitos. La contraseña necesita un minimo de 8 caracteres, sin espacios y tanto letras como números.")

print("###   Sistema de gestión de usuarios   ###")
menu()