completo = 0
incompleto = 0
    
while True:
    try:
        conteo_personas = int(input("¿a cuantas personas desea registrar? "))
        break
    except:
        print("el numero de personas debe ser entero.")
for persona in range(conteo_personas):
    while True:
        try:
            dosis = int(input("¿cuantas dosis a recibido? "))
            break
        except ValueError:
            print("el numero de dosis debe ser entero.")
  

    if dosis >= 3:
        print("esquema completo.")
        completo += 1
    else:
        print("esquema incompleto.")
        incompleto += 1
    
print("numero de personas registradas con esquema completo:" , completo)
print("numero de personas con esquema incompleto" , incompleto)