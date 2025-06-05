entero = False
completo = 0
incompleto = 0

while entero == False:
    try:
        personas = int(input("Ingrese la cantidad de personas a registrar\n"))
        entero = True
    except ValueError:
        print("Debe ingresar un número entero")
        entero = False

for i in range(personas):
    dosis1 = False
    while dosis1 == False:
        try:
            dosis = int(input(f"Ingrese cantidad de dosis recibidas de la persona {i + 1}\n"))
            dosis1 = True
            if dosis >= 3:
                print("Esquema completo")
                completo = completo +1
            else:
                print("Esquema incompleto")
                incompleto = incompleto +1
        
        except ValueError:
            print("Debe ingresar un número entero")

print(f"Se reigstraron {completo} con esquema completo")
print(f"Se registraron {incompleto} con esquema incompleto")
