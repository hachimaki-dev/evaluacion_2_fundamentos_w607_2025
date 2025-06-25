lista_usuarios = []
 
def menu():
    print("MENU PRINCIPAL")
    print("1. ingresar usuario")
    print("2. buscar usuario")
    print("3. eliminar usuario")
    print("4. salir")
    
def ingreso_usuario(nombre_usuario, sexo, contraseña):
    usuario = {
        nombre_usuario:{
            "sexo": sexo,
            "contraseña": contraseña
            
        }
    }
    return
    
def validar_contraseña(contraseña):
    numeros = False
    letras = False
    espacios = False
    for caracteres in contraseña:
        if caracteres.isdigit:
            numeros = True
            print("tiene numeros")
        if caracteres.isalpha:
            letras = True
            print("tiene letras")
        if caracteres == " ":
            print("tiene espacios")
            espacios = True
        
    if numeros and letras and espacios == False:
        print("contraseña ingresada correctamente")
        return True
 print(validar_contraseña("sdsdsds 21321314"))