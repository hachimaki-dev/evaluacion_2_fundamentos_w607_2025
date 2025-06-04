
esquemas_completos = 0
esquemas_incompletos = 0

while True:
    try:
        num_de_personas = int(input("¿Cuántas personas deseas registrar?: "))
        break
    except:
        print("Debes ingresar un número entero")

for contador in range(num_de_personas):
    while True:
        try:
            cantidad_dosis = int(input(f"Ingrese cuantas dosis ha recibido la persona {contador + 1}: "))
            break
        except:
            print("Debe ingresar un numero entero.")
    
    if cantidad_dosis >= 3:
        print("Esquema completo.")
        esquemas_completos = (esquemas_completos + 1)
    else:
        print("Esquema incompleto.")
        esquemas_incompletos = (esquemas_incompletos + 1)
        
print(" ")
print("------ [Resumen Final] -----------")
print("Total de personas registradas:", num_de_personas)
print("Personas con esquema completo:", esquemas_completos)
print("Personas con esquema incompleto:", esquemas_incompletos)
print("----------------------------------")