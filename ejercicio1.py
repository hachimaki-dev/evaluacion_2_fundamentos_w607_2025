def verificacionVacunacion():
    # Solicitar numero de personas
    while True:
        try:
            personas = int(input("Ingresa el numero de personas a registrar: "))
            if personas > 0:
                break
            else:
                print("Ingresa un numero positivo")
        except ValueError:
            print("Debe ingresar un numero entero")

    esquema_completo = 0
    esquema_incompleto = 0
    dosis = 0
    # Registrar las dosis de cada persona
    for i in range(personas):
        try:
            dosis = int(input("¿Cuantas dosis a resivido esta persona?: "))
            if dosis >= 3:
                print("Esquema completo")
                esquema_completo += 1
            elif dosis < 3:
                print("Esquema incompleto")
                esquema_incompleto += 1
        except ValueError:
            print("Debe ingresar un numero entero")
            i += 1
    # Resumen Final
    print("Se registraron",esquema_completo,"personas con Esquema Completo\n" \
    "y", esquema_incompleto,"con Esquema Incompleto" )

verificacionVacunacion()