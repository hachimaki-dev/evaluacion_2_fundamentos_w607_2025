personas = int(input("cuántas personas se van a registrar: "))
while personas < 1:
    try:
        personas = int(input("ingrese una cantidad de personas valido: "))

    except ValueError:
        
        print("solo puede ingresar numeros")



i= 0
for i in range (personas):
    
    dosis = int(input("cuántas dosis ha recibido"))
    while dosis < 1:
        try:
            dosis = int(input("ingrse dosis validas recibidas"))

        except ValueError:
            print("solo puede ingresar numeros")


    if dosis >= 3:
        print("Esquema ompleto")
    elif dosis < 3:
        print("Esquema incompleto")
    else:
        print("error")


print("personas con esquema completo")
print("personas con esquema incompleto")
