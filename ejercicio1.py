usuarios = {}

# Menú principal
def menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

# Validación de sexo
def validar_sexo():
    while True:
        sexo = input("Ingrese su sexo (M / F): ").upper() # Para poner el sexo, siempre pedira que sea mayuscula, pero si lo pone en minuscula, el upper se encargara de transformalo a mayuscula
        if sexo in ["M", "F"]: # En caso de poner una M o F, retornara bueno. En caso de poner una letra que no tenga nada que ver, irá al else que contiene el print
            return sexo
        else:
            print("Debes ingresar Masculino o Femenino. Vuelve a intentarlo!")

# Validar contraseña
def validar_contraseña():
    while True:
        contraseña = input("Ingresa tu contraseña: ") # Ingresar la contraseña que desea ponerle al usuario, tiene que ser si o si una contraseña con letras y digitos, funciones cuales se muestran abajo
        if (
            len(contraseña) >= 8 and # Con el len permite leer las letras de la contraseña, si es mayor o igual a 8, permite que sea una contraseña correcta. En caso de que sea menor a 8, dira que es una contraseña incorrecta
            any(c.isdigit() for c in contraseña) and # Permite que dentro de la contraseña hayan digitos como lo son numeros
            any(c.isalpha() for c in contraseña) and # Permite que dentro de la contraseña hayan letras
            ' ' not in contraseña # Esto permite que no hayan espacios dentro de la contraseña, en caso de haber un espacio, lo contara como una contraseña incorrecta, haciendo que el usuario vuelva a ingresar una contraseña que sea correcta
        ):
            print("Contraseña correcta!")
            return contraseña # En caso de tener una contraseña correcta, lo retornara bueno
        else:
            print("Contraseña incorrecta! Vuelve a intentarlo") # En caso de tener una contraseña incorrecta, lo llevara a este print

# Ingresar o registrar el nombre de los usuarios, individualmente
def ingresar_usuario():
    while True:
        usuario = input("Ingresa tu nombre de usuario: ") # Colocar el nombre de usuario
        if usuario in usuarios: # En caso de que el usuario ya este registrado dentro de la lista de las {}, dira el mensaje que se muestra en el print de abajo
            print("El usuario que ingresaste ya existe! Intenta con otro")
        else: # En caso de que el nombre sea registrado por primera vez, pasara como correcto y terminara la función de ingresar_usuario
            break

    sexo = validar_sexo()
    contraseña = validar_contraseña()

    usuarios[usuario] = { # Diccionario para los usuarios, donde se encuentra el nombre, sexo y contraseña. Utilizando la lógica de las {}, se puede obtener un resultado similar al que los [] ya que dentro de los corchetes, se guardan los usuarios que se vayan ingresando, junto también a su sexo y contraseña. Si se pudiera poner un ejemplo en la linea seria algo como usuarios[Pepe] = {"M": sexo, "1234asdf": contraseña} y así sucesivamente con cada usuario. No quiero ponerlo abajo ya que el codigo quedaria feo, en terminos de estructura xd
        "sexo": sexo,
        "contraseña": contraseña
    }
    print("Usuario ingresado con exito!")

# Buscar usuarios registrados, individualmente
def buscar_usuario():
    usuario = input("Ingresa el nombre de usuario que quieres buscar: ")
    if usuario in usuarios:
        print(f"El sexo del usuario es: {usuarios[usuario]['sexo']}") # Con esto se busca el genero del usuario, en base a la lista "usuarios", luego entrando en el "usuario" en concreto y por ultimo en el "sexo" del mismo. Todos estos datos ingresados por el mismo usuario
        print(f"La contraseña del usuario es: {usuarios[usuario]['contraseña']}") # Con esto se busca la contraseña ingresada por el usuario, utilizando el mismo método que el sexo. Empieza buscando en la lista "usuarios", luego pasa al "usuario" en concreto y por ultimo pasa a la "contraseña", revelando esta misma
    else:
        print("El usuario no se encuentra o no se ha registrado todavía")

# Eliminación de usuarios, individualmente
def eliminar_usuario():
    usuario = input("Ingresa el nombre del usuario que deseas eliminar: ")
    if usuarios.pop(usuario, None): # Con este if y la función "pop", permite eliminar al usuario deseado dentro de la lista, si el usuario ingresado es el correcto, se eliminara. En caso de ser incorrecto, utilizara el "None" para luego imprimir la linea que esta debajo del else
        print("El usuario se ha eliminado con exito") # Usuario encontrado
    else:
        print("No se ha podido eliminar el usuario") # Usuario no encontrado

# Selección de opciones de menú principal 
def main():
    while True:
        menu() # Llama a la función del menú que aparece en el principio
        try:
            opciones = int(input("Ingresa una opción entre el 1 - 4: "))
            if opciones == 1:
                ingresar_usuario()
            elif opciones == 2:
                buscar_usuario()
            elif opciones == 3:
                eliminar_usuario()
            elif opciones == 4:
                print("Finalizando programa...")
                print("Hasta luego!")
                break
        except ValueError: # En caso que ingrese un número  o letra que no se encuentre en las opciones
            print("Debes de ingresar un número! Entre el 1 y el 4")

main()
