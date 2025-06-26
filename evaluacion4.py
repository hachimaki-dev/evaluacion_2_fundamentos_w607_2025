usuarios = {
    "nombre_usuario": {
        "sexo": "F" or "M",
        "contraseña": "contraseña_usuario",
    }
}

def menu():
    while True:
        opciones = {
            "1": "Ingresar ususario",
            "2": "buscar usuario",
            "3": "Eliminar usuario",
            "4": "Salir"
        }
        for clave, opcion in opciones.items():
            print(f"{clave}. {opcion}")
        try:
            eleccion = input("¿Que desea hacer el dia de hoy?: ")
            if eleccion == "1":
                ingresar_usuario()
            elif eleccion == "2":
                buscar_usuario()
            elif eleccion == "3":
                eliminar_usuario()
            elif eleccion == "4":
                print("Hasta luego")
                break
            else:
                print("Esa opcion no existe, por favor intente de nuevo")
        except Exception as e:
            print(f"ocurrio un error: {e}")

def verificar_contraseña():
    while True:
        contraseña = input("Ingrese la contraseña del usuario: ")
        verificacion1 = False
        verificacion2 = False
        verificacion3 = False
        verificacion4 = False
        if len(contraseña) < 8:
            verificacion1 = True
        if not contraseña.isalnum():
            verificacion2 = True
        if not any(c.isalpha() for c in contraseña):
            verificacion3 = True
        if not any(c.isdigit() for c in contraseña):
            verificacion4 = True
        if verificacion1:
            print("La contraseña debe tener al menos 8 caracteres")
        if verificacion2:
            print("La contraseña debe ser alfanumerica y no contener espacios")
        if verificacion3:
            print("La contraseña debe contener al menos una letra")
        if verificacion4:
            print("La contraseña debe contener al menos un numero")
        if not verificacion1 and not verificacion2 and not verificacion3 and not verificacion4:
            print("Contraseña verificada correctamente")
            return contraseña

def sexo_verificacion():
    while True:
        sexo = input("ingrese el sexo del usuario F para femenino y M para masculino: ").upper().strip()
        if sexo not in ["F" , "M"]:
            print("sexo no valido favor ingresar F o M")
            continue
        return sexo

def ingresar_usuario():
    while True:
        try:
            nombre = input("ingrese el nombre de usuario: ")
            if nombre in usuarios:
                print("El nombre de usuario ya existe, por favor ingrese otro")
                continue
            sexo = sexo_verificacion()
            contraseña = verificar_contraseña()
            usuarios[nombre] = {
                "sexo": sexo,
                "contraseña": contraseña
            }
            print(f"Usuario {nombre} ingresado correctamente")
            input("Presione Enter para continuar...")
            break
        except Exception as e:
            print(f"Ocurrio un error: {e}")



def buscar_usuario():
    contador_error = 0 #puse este contador porque en el ejemplo al momento de equivocarce regresaba al menu pero eso me parece poco amigable y molesto
                    #pero si no ponia el break se quedaba en un bucle infinito hasta que ingresara un dato correctamente 
    while True:
        nombre = input("ingrese el nombre del usuario a buscar: ")
        if nombre in usuarios:
            print(f"usuario encontrado: {nombre}")
            print(f"Sexo: {usuarios[nombre]['sexo']}")
            print(f"Contraseña: {usuarios[nombre]['contraseña']}")
            input("Presione Enter para continuar...")
            break
        else:
            print("Usuario no encontrado, por favor intente de nuevo")
            contador_error = contador_error + 1
            if contador_error < 3:
                continue
            else:
                print("muchos intentos fallidos")
                input("Presione Enter para continuar...")
                break

def eliminar_usuario():
    contador_error = 0 
    while True:
        nombre = input("ingrese el nombre del ususario a elminar: ")
        if nombre in usuarios:
            del usuarios[nombre]
            print(f"Usuario {nombre} eliminado correctamente")
            input("Presione Enter para continuar...")
            break
        else:
            print("usuario no encontrado, por favor intente de nuevo")
            contador_error = contador_error +1
            if contador_error < 3:
                continue
            else:
                print("muchos intentos fallidos")
                input("Presione Enter para continuar...")
menu()