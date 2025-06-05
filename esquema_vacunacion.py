personas = 0
while True:
    try:
        personas = int(input("Ingrese la cantidad de personas a registrar: "))
        if personas > 0:
            break
        else:
            print("Debe ingresar un número entero positivo.")
    except ValueError:
        print("Debe ingresar  un número entero.")
vacunados = 0
no_vacunados = 0
for i in range(personas): 
    while True:
        try:
            dosis = int(input("Ingrese cantidad de dosis recibidas: "))
            if dosis == 0:
                print("Ingresa un numero positivo.")
            else:
                if dosis == 3:
                    print("Esquema completo.")
                    vacunados += 1
                else:
                    print("Esquema incompleto")
                    no_vacunados += 1
                break
        except ValueError:
            print("Ingresa un número entero.")

print(f"Se registraron {vacunados} personas con esquema completo.")
print(f"Se registraron {no_vacunados} personas con esquema incompleto.")