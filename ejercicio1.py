esquema_completo = []
esquema_incompleto = []


while True:
    print("=== Bienvenido al programa de Vacunación ===")
    print("            ¿Qué deseas hacer?\n")
    print("1. Ingresar personas para vacunar")
    print("2. Preguntar por personas con esquema completo")
    print("3. Preguntar por personas con esquema incompleto")
    print("4. Salir\n")

    try:
        opcion = int(input("Selecciona una de las opciones: "))
    except ValueError:
        print("Debes seleccionar una opción válida, entre el 1 y 4")
        continue

    if opcion == 1:
        try:
            print("¿Cuantas personas se van a registrar para recibir una dosis de la vacuna?")
            vacunar_personas = int(input("Ingrese el número de personas para vacunar: "))
        except ValueError:
            print("Debes ingresar un número entero. Volviendo al menú...")
        



