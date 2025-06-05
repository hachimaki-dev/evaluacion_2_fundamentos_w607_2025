esquema_completo = 0
esquema_incompleto = 0

while True:
    try:
        personas_registradas = int(input("Ingresa cuantas personas se van a vacunar (ingresa un numero entero) "))
        break
    except:
        print("Error debe ingresar un numero entero")
for el_container in range(personas_registradas):
    while True:
        try:
            dosis = int(input(f"Ingresa el numero de dosis {el_container + 1}: "))
            break
        except ValueError:
            print("Debe ingresar un numero entero")
    if dosis >= 3:
        print("Esquema completo")
        esquema_completo = el_container
    else:
        print ("esquema incompleto")
        esquema_incompleto = el_container

print(f"las personas con el esquema completo son: {esquema_completo - 1}")
print(f"las personas con el esquema incompleto son: {esquema_incompleto + 1}")