lista_usuarios=[]
def ingresar_usuario (nombre_usuario, sexo, clave):
    if sexo != "m"and sexo !="f":
        print("porfavor, pon la opcion correcta, f de femenino y m d masculino")
    else:
        clave_correcta = validar_clave(clave)
        if clave_correcta:
            usuario={
                nombre_usuario: {
                    "sexo":sexo,
                    "clave":clave
                }
            } 
            usuario_existe=validar_clave  (nombre_usuario)
            if usuario_existe:
                print ("el usuario ya existe")
            else: lista_usuarios.append(usuario)
        else:
            print("la contraseña no comple con los requisitos")
            return
def buscar_usuario(nombre_usuario):
        for usuario in lista_usuarios:
            if nombre_usuario in usuario:
                print(usuario)
                print("el user q buscaste si esta disponible")
                print("clave:", usuario[nombre_usuario]["clave"])
                print("sexo:", usuario[nombre_usuario]["sexo"])
        return
        print("el usuario no esta disponible")
def eliminar_usuario(nombre_usuario):
       for usuario in lista_usuarios:
        if nombre_usuario in usuario:
            lista_usuarios.remove(usuario) 
            return True

def validar_clave (clave):
        if len(clave)< 8:
              print("la clave debe tener mas de ocho caracteres")
        else:
            tiene_letras =False
            tiene_numeros=False
            tiene_espacios=False
            for caracter in clave:
                if caracter.isalpha():
                    tiene_letras=True
                elif caracter.isdigit():
                 tiene_numeros=True
                elif caracter== " ":
                    tiene_espacios=True
            if tiene_numeros and tiene_letras and tiene_espacios== False:
                return True
            elif tiene_espacios:
                return False
def iniciar_programa():
    print("1. ingresar usuario")
    print("2.- buscar usuario")
    print("3.- eliminar usuario")
    print("4.-salir")
    while True:
        try:
            opcion_elegida= int(input("ingrese que desea hacer"))
        except:
            print("porfavor pon una opcion valida")
        while True:
            if opcion_elegida ==1:
                nombre= input("porfavor ponga en nombre de usuario")
                sexo= input("por favor f para femenino/ m para masculino")
                clave= input ("porfavor ingrese la clave de el usuario")
                ingresar_usuario(nombre, sexo, clave)
                break
            elif opcion_elegida == 2:
                nombre= input("porfavor ponga in nombre d usuario a buscar")
                buscar_usuario(nombre)
                break
            elif opcion_elegida==3:
                nombre= input ("porfavor escriba un nombre de usuaeio a eliminar")
                eliminar_usuario(nombre)
                break

    

ingresar_usuario("jvt.mimi","f","cnmroll23")
ingresar_usuario("salem","m","miau3033249")
ingresar_usuario("orquidea","f","9dejulio5008")
  
iniciar_programa()

#profe, en caso q este viendo mi tarea ahora mismo, vio el anterior? el donde le


