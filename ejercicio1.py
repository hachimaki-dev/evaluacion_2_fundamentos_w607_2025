
contador_dosisCompletas = 0
contador_dosisIncompletas = 0
dosis = 0
while True:
    print("buenos dias \n¿cuantas personas se van a registrar el dia de hoy?")
    try:
        cantidad_personas = int(input("N° a registrar: "))
        if cantidad_personas < 0:
            print("Por favor ingrese un numero entero")
            continue
        elif cantidad_personas == 0:
            print("Por favor ingrese un numero mayor a 0")
            continue
        break
    except ValueError:
        print("Por favor, ingrese un numero entero")

while True:
    for i in range(1, cantidad_personas + 1):
        try:
            dosis = int(input("¿Cuantas dosis ha recibido?: "))
            if dosis < 0 :
                print("Por favor ingrese un numero entero POSITIVO")
            elif dosis == 3:
                contador_dosisIncompletas += 1
                print("Su esquema de vacunas esta completo")
            elif dosis < 3:
                contador_dosisIncompletas += 1
                print("Su esquema de vacunas esta incompleto")
        except ValueError:
            print("Por favor ingrese un numero entero")

print(f"el numero de personas con su esquema de vacunacion completo es: {contador_dosisCompletas}")
print(f"el numero de personas con su esquema de vacunacion incompleto es: {contador_dosisIncompletas} ")


            



