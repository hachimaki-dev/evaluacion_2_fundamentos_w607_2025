num_entero = False
while num_entero == False:
    try:
        personas = int(input("¿Cuantas personas se van a registrar? "))
        num_entero = True
    except ValueError:
        print("Debe ingresar un numero entero")

    doseados = 0
    no_doseados = 0

    try:
        for i in range(0,personas):

            dosis = int(input(f"¿Cuantas dosis ha recibido la persona {i + 1}? "))
            if dosis < 3:
                doseados = doseados + 1
            else:
                no_doseados = no_doseados +1

    except ValueError:
        print("Debe ingresar un numero entero")

    print(f"Se registaron {doseados} personas con esquema incompleto")
    print(f"Se registaron {no_doseados} personas con esquema completo")

    