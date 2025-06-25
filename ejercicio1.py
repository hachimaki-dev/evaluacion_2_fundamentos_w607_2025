lista_deusuarios = []

def ingresar_usuario(nombre,sexo,contraseña):
  if sexo != "M" and  "F" :
    print("Opcion invalida debe escribir 'M' para masculino  o 'F' para femenino")
  else:
    
    
    usuario = {
        'nombre': nombre,
        'sexo': sexo,
        'contraseña': contraseña }
    
    lista_deusuarios.append(usuario)
    print("Usuario ingresado correctamente.")


def buscar_usuario(nombre_usuario):
 for usuario in lista_deusuarios:
    if usuario in lista_deusuarios:
     print ("el usuario existe")
    else:
       ("el usuario no existe")

    return

def eliminar_usuario():
    return

def validar_contraseña(contraseña):
   if len(contraseña) < 8 :
    print ("la contraseña debe tener 8 caracteres")
   else:
        tiene_letras = False
        tiene_numeros = False
        tiene_espacios = False
        for caracter in contraseña:
          if caracter .isalpha():
           tiene_letras = True
          elif caracter .isdigit():
             tiene_numeros = True
          elif caracter ==  "":
             tiene_espacios = True
        if tiene_numeros and tiene_letras and tiene_espacios == False:
           return True
        elif tiene_espacios:
           return False

def validar_sexo():
    return

def mostrar_menu():
    while True:
        print("---Bienvenido al sistema de usuarios---")
        print("1. Ingresar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

    if