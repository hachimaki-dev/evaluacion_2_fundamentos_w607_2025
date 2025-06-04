personas = 0
while True:
    try:
        personas = int(input("Ingrese la cantidad de personas a registrar: "))
        if personas > 0:
            break
        else:
            print("Debe ingresar un número entero positivo.")
    except ValueError:
        print("Debe ingresar  un número entero.")

for i in range(personas): 
    while True:
        try:
            dosis = int(input("Ingrese cantidad de dosis recibidas: "))
            if dosis > 0:
                break
            elif dosis <= 3:
                print("Esquema completo.")
            else:
                print("Esquema incompleto.")
        except ValueError:
            print("Debe ingresar un numero entero.")
        