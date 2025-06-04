while True:

    esquema_completo = 0
    esquema_incompleto = 0   

    try:
        personas = int(input("Ingrese cantidad de personas a registrar: "))
        break
    except:
        print("Debe ingresar un número entero.")

while True:
    try:
        dosis = int(input("Ingrese cantidad de dosis recibida: "))
        if dosis >= 3:
            print("Esquema Completo")
            esquema_completo = esquema_completo + 1 
            personas = personas - 1
        else:
            print("Esquema Incompleto")
            esquema_incompleto = esquema_incompleto + 1
            personas = personas - 1
    except:
        print("Debe ingresar un número entero.")

    if personas == 0:
        break

print(f"Se registraron {esquema_completo} personas con esquema completo.")
print(f"Se registraron {esquema_incompleto} personas con esquema incompleto.")