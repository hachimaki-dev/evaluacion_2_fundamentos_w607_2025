esquema_completo = 0
esquema_incompleto = 0

def esquema_dosis():
    global esquema_completo, esquema_incompleto

    while True:
        try:
            dosis = int(input("Ingrese cuántas dósis ha recibido: "))
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    if dosis >= 3:
        print("Esquema completo.")
        esquema_completo +=1
    elif dosis < 3:
        print("Esquema incompleto.")
        esquema_incompleto +=1


while True:
    try: 
        n = int(input("Ingrese la cantidad de personas que se van a registrar: "))
        break

    except ValueError:
        print("Debe ingresar un número entero.")

for i in range(n):
    esquema_dosis()

print(f"Se registraron {esquema_completo} con esquema completo.")
print(f"Se registraron {esquema_incompleto} con esquema incompleto.")