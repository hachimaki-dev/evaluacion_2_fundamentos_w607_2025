import os

# Control parea guardar los numeros ingresados
numeros_guardados = []

# Bandera para controlar el menu principal
menu_activo = True

while menu_activo:
    # Limpiar pantalla (opcional)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Mostrar menu principal
    print("====MENU PRINCIPAL====")
    print("1. Ingresar un numero")
    print("2. Mostrar numero mayor")
    print("3. Mostrar promedio")
    print("4. Salir del programa")
    print("======================")

 # Opciónes del usuario
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        try:
            numero = int(input("\nIngrese un número: "))
            numeros_guardados.append(numero)
            print("Número guardado con éxito.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")
        input("\nPresiona ENTER para volver al menú...")

    elif opcion == "2":
        if numeros_guardados:
            print(f"\nEl número más grande es: {max(numeros_guardados)}")
        else:
            print("\nAún no se han ingresado números.")
        input("\nPresiona ENTER para volver al menú...")

    elif opcion == "3":
        if numeros_guardados:
            promedio = sum(numeros_guardados) / len(numeros_guardados)
            print(f"\nEl promedio de los números ingresados es: {promedio:.2f}")
        else:
            print("\nAún no se han ingresado números.")
        input("\nPresiona ENTER para volver al menú...")

    if opcion == "4":
        print("\n¡Fin del programa! ¡Adiós!")
        menu_activo = False  # Cambiar bandera para salir del bucle

    else:
        input("Presiona ENTER para continuar...")

# Mensaje final fuera del bucle
print("Gracias por usar el programa chao!.")
