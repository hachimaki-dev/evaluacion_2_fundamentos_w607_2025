entero = False
dosis1 = False
completo = 0
incompleto = 0

while entero == False:
    try:
        personas = int(input("Ingrese la cantidad de personas a registrar\n"))
        entero = True
    except ValueError:
        print("Debe ingresar un número entero")
        entero = False


while dosis1 == False:
    try:
        for cantidad in range(personas):
            dosis = int(input("Ingrese cantidad de dosis recibidas"))
            dosis1 = True
            if dosis >= 3:
                print("Esquema completo")
                completo = completo +1
            else:
                print("Esquema incompleto")
                incompleto = incompleto +1
        
        print(f"Se reigstraron {completo} con esquema completo")
        print(f"Se registraron {incompleto} con esquema incompleto")

    except ValueError:
        print("Debe ingresar un número entero")
        dosis1 = False

    