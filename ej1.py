while True:
    try:
        cantidad_personas = int(input("Ingrese la cantidad de personas a registrar: "))
        break
    except:
        print("Debe ingresar un número entero")

esquema_completo = 0
esquema_incompleto = 0

for i in range(cantidad_personas):
    while True:
        try:
            dosis = int(input("Ingrese cantidad de dosis recibidas: "))
            break
        except:
            print("Debe ingresar un número entero")    
    if dosis >= 3:
        print("Esquema completo")
        esquema_completo = esquema_completo + 1
    else:
        print("Esquema incompleto")
        esquema_incompleto = esquema_incompleto + 1

print("resultados")
print(f"Se registraron {esquema_completo} personas con esquema completo")
print(f"Se registraron {esquema_incompleto} personas con esquema incompleto")