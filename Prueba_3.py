while True:
    try:
        personas_registradas = int(input("Ingresa cuantas personas se van a vacunar (ingressa un numero entero) "))
        break
    except:
        print("Error debe ingresar un numero entero")
for el_container in range(personas_registradas):
    while True:
        try:
            dosis = int(input(f"Ingresa el numero de dosis {el_container + 1}: "))
            break
        except:
            print("Debe ingresar un numero entero")
if dosis >= 3:
    print("Esquema compoleto")
else:
    dosis < 3 
    print ("esquema incompleto")