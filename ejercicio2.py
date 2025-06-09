while True:
    try:
        total_personas = int(input("Ingrese la cantidad de personas a registrar: "))
        break
    except:
        print("debe ingresar un numero entero")

esquema_completo = 0
esquema_incompleto = 0

for i in range(total_personas):
    while True:
        try:
            dosis = int(input("Ingrese cantidad de dosis recibidas: "))
            break
        except:
            print("Debe ingresar un número entero.")
    
    if dosis >= 3:
        print("Esquema completo.")
        esquema_completo += 1
    else:
        print("Esquema incompleto.")
        esquema_incompleto += 1

print(f"\nSe registraron {esquema_completo} personas con esquema completo.")
print(f"Se registraron {esquema_incompleto} persona{'s' if esquema_incompleto != 1 else ''} con esquema incompleto.")