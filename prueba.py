lista_de_usuario = []

def ingresar_usuario(nombre_usuario,sexo,contraseña):
    usuario_exite =   validar_usuario(nombre_usuario)
    if usuario_exite:
        print("no es posible agregar un usuario que ya existe")
    else:
            if sexo != "F" and sexo != "M":
                print("por favor ingrese un valor correcto, F para femenino, M para masculino")
            else:
                contraseña_es_correcto = validar_contraseña(contraseña)
                if contraseña_es_correcto:
                    usuario = {
                        nombre_usuario  : {
                            "sexo" : sexo,
                            "contraseña" : contraseña

                        }

                    }
                    lista_de_usuario.append(usuario)
                    print("usuario agregado con exito")
                else:
                    print("la contraseña no cumple los requisitos")
        
    return
 
def eliminar_usuario(nombre_usuario):
    try:
        print("recorriendo lista de usuarios")
        for usuario in lista_de_usuario:
            if nombre_usuario in usuario:
                lista_de_usuario.remove(usuario)
                print(lista_de_usuario)
                return True
    except: 
        print("usuario no existe, escoga un usuario existente ")

def buscar_usuario(nombre_usuario):
    for usuario in lista_de_usuario:
        if nombre_usuario in usuario:
            print("el usuario que estas buscando si exite ")
            print("el sexo de ",nombre_usuario, " es: ",usuario[nombre_usuario]["sexo"])    
            print("la contraseña de ",nombre_usuario," es: ",usuario[nombre_usuario]["contraseña"])
        else:
            print("usuario",nombre_usuario,"no existe, por favor digite un usuario existente")

def validar_contraseña(contraseña):
    if len (contraseña) < 8:
        print("la contraseña debe tener mas de 8 caracteres")
    else:
        try:
            tiene_letras   = False
            tiene_numeros  = False
            tiene_espacios = False
            for caracter in contraseña:
                if caracter.isalpha():
                    tiene_letras = True
                elif caracter.isdigit():
                    tiene_numeros = True
                elif caracter == " ":
                    tiene_espacios = True
            if tiene_numeros and tiene_letras and tiene_espacios == False:
                return True
            elif tiene_espacios:                  
                return False
        except:
            print("contraseña valida")
    return

def validar_usuario(nombre_usuario):
    for usuario in lista_de_usuario:
        if nombre_usuario in usuario:
                print("el usuario",nombre_usuario,"si existe ")
                return True
        else:
            print("el usuario", nombre_usuario,"no existe ")
            print("el usuario,",nombre_usuario,"se ingreso correctamente")
            return False
        
def iniciar_programa():
    while True:
        
            print("1. ingresar usuario")
            print("2. buscar usuario")
            print("3. eliminar usuario")
            print("4. salir ")
        
            opcion_elegida = int(input("eliga una opcion "))
            while True:
            
                if opcion_elegida == 1:    
                    nombre_usuario = input("por favor ingrese el nombre del usuario: ")
                    sexo = input("por favor ingrese el sexo del usuario(F si es femenino o M para masculino): ")
                    contraseña = input("por favor ingrese la contraseña del usuario: ")
                    ingresar_usuario(nombre_usuario,sexo,contraseña)
                    break
                elif opcion_elegida == 2:
                    nombre_usuario = input("por favor ingrese el nombre de usuario que desea buscar: ")
                    buscar_usuario(nombre_usuario)
                    break
                elif opcion_elegida == 3:
                    nombre_usuario = input("por favor ingrese el nombre del usuario que desea eliminar: ")
                    eliminar_usuario(nombre_usuario)
                    break
                elif opcion_elegida == 4:
                    break
                break
        
          
        


iniciar_programa()
