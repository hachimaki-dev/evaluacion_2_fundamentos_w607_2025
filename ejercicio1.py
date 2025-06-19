# Definición de variables y sus valores iniciales que corresponden
esquema_completo = 0
esquema_incompleto = 0

# Bucle infinito del menú de usuario
while True:
    print("=== Bienvenido al programa de Vacunación ===")
    print("            ¿Qué deseas hacer?\n")
    print("1. Ingresar personas para vacunar")
    print("2. Preguntar por personas con esquema completo")
    print("3. Preguntar por personas con esquema incompleto")
    print("4. Salir\n")

# El programa solicita un número entero para escoger entre las opciones, las cuales serían del 1 hasta el 4, el try-except se asegura de que ea un número entero y no decimal o letras
    try:
        opcion = int(input("Selecciona una de las opciones: "))
    except ValueError:
        print("Debes seleccionar una opción válida, entre el 1 y 4")
        continue # Ayuda a continuar el bucle de selección de opciones

# Opción 1, la cual contiene el número de personas que se van a registrar para recibir las dosis de la vacuna y la cantidad de estas mismas dosis, junto a ello también se encuentra el contador de esquema completo e incompleto
    if opcion == 1:
        while True:
            try:
                print("¿Cuantas personas se van a registrar para recibir una dosis de la vacuna?")
                vacunar_personas = int(input("Ingrese el número de personas para vacunar: "))
                if vacunar_personas < 0: # En caso de que el usuario ingrese un número negativo o menor a 0, le dira que intente de nuevo, pero ingresando un número positivo
                    print("Debes ingresar un número positivo. Intenta de nuevo!")
                    continue # Omite el resto de las lineas dentro del while para que el usuario vuelva a ingresar el número de personas a vacunar 
                break # Rompe el bucle de personas para vacunar
            except ValueError:
                print("Debes ingresar un número entero. Intenta de nuevo!") # En caso de que el usuario ingrese un número decimal o letras

        for i in range(vacunar_personas): # Inicia un bucle que termina con el digito ingresado por el usuario, en caso de que el usuario ingrese 50 personas, el bucle terminara en la persona n° 50
            while True:
                try:
                    dosis = int(input("Ingrese la cantidad de dosis recibidas por la persona: ")) # Pide la cantidad de dosis recibidas por cada persona
                    break # Una vez terminada la cantidad de dosis recibidas, rompe el programa para pasar al resumen de los esquemas
                except ValueError:
                    print("Debes ingresar un número entero. Intenta de nuevo!")
                    
            # Contador que aumenta el digito inicial de cada esquema (0), por cada persona que recibe 3 vacunas, en caso de completo y si es menos de 3 en caso del incompleto
            if dosis == 3:
                print("Esquema completo")
                esquema_completo += 1
            else:
                print("Esquema incompleto")
                esquema_incompleto += 1

            # Resumen provisorio de los esquemas, esto facilita el no tener que volver al menu y seleccionar la opción 2 o 3
            print(f"Se registraron {esquema_completo} personas con el esquema completo\n")
            print(f"Se registraron {esquema_incompleto} personas con el esquema incompleto\n")

# Opción 2 - Esquema completo
    elif opcion == 2:
        print(f"Hay {esquema_completo} personas con el esquema completo")

# Opción 3 - Esquema incompleto
    elif opcion == 3:
        print(f"Hay {esquema_incompleto} personas con el esquema incompleto")

# Opción 4 - Finalizar programa
    elif opcion == 4:
        print("Finalizando programa...")
        print("Hasta luego!")
        break


