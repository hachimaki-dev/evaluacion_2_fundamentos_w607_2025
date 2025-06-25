#inicio
listaUsuarios = []


def ingresarUsuario(nombreDeUsuario, sexo, contraseña):
    while True:
        try:
            if sexo != "M" and sexo != "F":
                print("Por favor, ingrese -F- para femenino o -M- para masculino")
                contraseñaEsCorrecta = validarContraseña
                #aca creamos un diccionario para lo solicitado
                if contraseñaEsCorrecta:
                    usuario = {
                        nombreDeUsuario : {
                            "sexo" : sexo,
                            "contraseña" : contraseña
                        }
                    }

            return
        except ValueError:
            print("Por favor, ingrese datos validos")

            






def buscarUsuario(nombreDeUsuario):
    while True:
        try:
            for usuario in listaUsuarios:
                print("El usuario que buscas sí existe")
                print("La contraseña de", nombreDeUsuario, "es", usuario[nombreDeUsuario]["contraseña"])
                print("El sexo de", nombreDeUsuario, "es", usuario[nombreDeUsuario]["contraseña"])
                print("Presione Enter para continuar")
                input()
        except ValueError:
            print("El usuario ingresado no existe")
            print("Presione Enter para continuar")
            input()



def eliminarUsuario(nombreDeUsuario):
    for usuario in listaUsuarios:
        print("El usuario ha sido eliminado exitosamente")
        listaUsuarios.remove(nombreDeUsuario)
        print("Presione Enter para continuar")
        input()




def validarContraseña(contraseña):
    if len(contraseña )< 8:
        print("La contraseña debe tener más de 8 carácteres")
    else:
        tieneLetras = False
        tieneNumeros = False
        tieneEspacios = False
        
        for caracter in contraseña:
            if caracter.isalpha(): #tiene letras?
                tieneLetras = True
            elif caracter.isdigit(): #tiene numeros?
                tieneNumeros = True
            elif caracter == " ": #tiene espacios?



                if tieneNumeros and tieneLetras and tieneEspacios == False:
                    return True
                elif tieneEspacios:
                    return False
        
def validarSexo(sexo):
    print("")





def inicioMenu():
    print("****Bienvenido al menú principal****")

    while True:
        try:
            print("")
        
        except ValueError:
            print("ERROR")


        




def mostrarMenu():
    while True:
        try:

            opción = int(input("Por favor seleccione una opción: "))

            print("1. Ingresar usuario")
            print("2. Buscar usuario")
            print("3. Eliminar usuario")
            print("4. Salir")

        except ValueError:
            print("Por favor, seleccione una opción válida")
            print("Presione Enter para continuar")
            input()



