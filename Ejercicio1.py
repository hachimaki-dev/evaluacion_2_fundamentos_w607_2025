esq_com = 0
esq_inc = 0
bucle = True
while bucle:
    try:
        personas = int(input("Cuantas personas se van a registrar? : \n"))
        bucle = False
    except ValueError:
        print("Ingrese un numero entero.")

for i in range(personas):
    bucle2 = True
    while bucle2:
        try:
            dosis = int(input("Cuantas dosis ha recibido? : \n"))
            bucle2 = False
        except ValueError:
            print("Ingrese un numero entero.")
    
    if dosis >= 3 :
        print("Esquema completo.")
        esq_com += 1
    elif dosis < 3:
        print("Esquema incompleto")
        esq_inc += 1

print("===RESUMEN===")
print(f"Pacientes con esquema completo : {esq_com}")
print(f"Pacientes con esquema incompleto : {esq_inc}")
    

