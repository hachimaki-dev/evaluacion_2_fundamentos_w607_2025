esquema_completo= 0
esquema_incompleto= 0

while True:
    try:
        cantidad_personas= int(input("INGRESE CANTIDAD DE PERSONAS\n:"))
        break
    except ValueError:
        print("DEBE INGRESAR UN NUMERO ENTERO VALIDO!")

for i in range(cantidad_personas):
    while True:
        try:
            cantidad_dosis= int(input("INGRESE CANTIDAD DE VACUNAS: "))
            if cantidad_dosis >= 3:
                print("---ESQUEMA DE VACUNACION COMPLETO---")
                esquema_completo = esquema_completo + 1
                break
            elif cantidad_dosis <= 3:
                print("---ESQUEMA DE VACUNACION INCOMPLETO---")
                esquema_incompleto = esquema_incompleto + 1
                break
        except ValueError:
            print("INGRESE UN NUMERO ENTERO VALIDO!")

            
print("\n---RESUMEN---")
print(f"SE REGISTRARON {esquema_completo} PERSONAS CON ESQEUMA COMPLETO ")
print(f"SE REGISTRARON {esquema_incompleto} PERSONAS CON ESQUEMA INCOMPLETO")

