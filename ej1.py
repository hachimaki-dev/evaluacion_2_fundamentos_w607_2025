
esque_completo = 0
esque_incompleto = 0
print("Bienvenido al sistema de verificación de vacunas.\n")
print("Para empezar, ingrese la cantidad de personas a verificar: ")

while True:
    try:
        cant_pers = int(input(""))
        print(f"Perfecto, la cantidad de personas a verificar es {cant_pers}.")
        break
    except ValueError:
        print("Error: Debe ingresar un número entero. Inténtelo de nuevo: ")
        
        
for i in range(cant_pers):
    while True:
        try:
            dosis = int(input("Cuántas vacunas recibió la persona? Indique la cantidad: "))
            if dosis >= 3:
                print("La persona recibió sus dosis necesarias. Esquema completo.")
                esque_completo += 1
            else:
                print("La persona no recibió sus dosis necesarias. Esquema incompleto.")
                esque_incompleto += 1
            break
        except ValueError:
            print("Error: El número que ingresó es entero. Intente de nuevo.")

print("\n")
print("Validaciones hechas. Calculando esquemas...\n")
print(f"Hay {esque_completo} personas con esquema completo.")
print(f"Hay {esque_incompleto} personas con esquema incompleto.")
print("\n")


