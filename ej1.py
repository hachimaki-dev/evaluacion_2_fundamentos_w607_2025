esque_comp = []
esque_incom = []
dosis = 0
dosis_necesarias = 3
print("Bienvenido al sistema de verificación de vacunas.\n")
print("Para empezar, ingrese la cantidad de personas a verificar: ")

while True:
    try:
        cant_pers = int(input(""))
        print(f"Perfecto, la cantidad de personas a verificar es {cant_pers}.")
        break
    except ValueError:
        print("Error: Debe ingresar un número entero. Inténtelo de nuevo: ")
        
        
# Cómo hacer lo de "por cada N de personas, preguntar con loop (paso 2)"