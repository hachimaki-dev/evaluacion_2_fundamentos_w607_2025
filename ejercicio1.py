esquema_completo = 0
esquema_incompleto = 0
#Debe tener: while/for/try-except/contadores/acumuladores
#PASO --> 1: Solicitar el número de personas
print("Bienvenid@ al sistema de verificación de vacunación.")
while True:
    try:
        cuantos = int(input("¿Cuantas personas se van a registar?: "))
        print(f"Se registrarán {cuantos} persona/s")
        if cuantos < 0:
            print("Ingrese un número válido.")
        else:
            break
    except ValueError:
        print("ingrese un número válido.")

#PASO --> 2: Registrar las dosis de cada persona
for cuantos in range(1, cuantos + 1):
    while True:
        try:
            dosis = int(input("Cuantas dosis ha recibido?: "))
            if dosis <0:
                print("Ingrese un número válido.")
            elif 0 < dosis < 3:
                esquema_incompleto += 1
                print("Esquema incompleto")
                break
            elif dosis >= 3:
                esquema_completo += 1
                print("Esquema completo")
                break
        except ValueError:
            print("Ingrese un número válido.")
#PASO --> 3: Mostrar el resumen final
print("Ha finalizado el proceso de verificacion de vacunas")
print(f"Se registraron un total de {cuantos} persona/s")
print(f"Se han registrado {esquema_completo} persona/s con esquema completo")
print(f"Se han registrado {esquema_incompleto} persona/s con esquema incompleto")