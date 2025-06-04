esquema_completo = 0
esquema_incompleto = 0
#Debe tener: while/for/try-except/contadores/acumuladores
#PASO --> 1: Solicitar el número de personas
print("Bienvenid@ al sistema de verificación de vacunación.")
while True:
    try:
        cuantos = int(input("¿Cuantas personas se van a registar?: "))
        if cuantos < 0:
            print("Ingrese un número válido.")
        else:
            break
    except ValueError:
        print("ingrese un número válido.")

#PASO --> 2: Registrar las dosis de cada persona
for cuantos in range(cuantos, cuantos + 1):
    while True:
        try:
            dosis = int(input("Cuantas dosis ha recibido?: "))
            if dosis <0:
                print("Ingrese un número válido.")
            else:
                break
        except ValueError:
            print("Ingrese un número válido.")
#PASO --> 3: Mostrar el resumen final