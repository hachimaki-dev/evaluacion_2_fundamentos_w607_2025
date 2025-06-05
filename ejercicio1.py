print("bienvenido al programa de vacunas")
try:
   numero_usuarios = int (input("¿cuantos usarios desea evaluar?"))
except ValueError:
    print("hubo un error ingrese un numero valido")
    DOSIS_NECESARIAS = 2 
completos = 0
incompletos = 0
while True:
    entrada = input("¿Cuántas personas desea registrar?")
    try:
        total_personas = int(entrada)
        break
    except ValueError:
        print("Por favor ingrese un número válido")
for persona in range(1, total_personas + 1):
    print(f"Registro de la persona número {persona}")
    while True:
        dato = input("Cantidad de dosis aplicadas:")
        try:
            dosis_recibidas = int(dato)
            break
        except ValueError:
            print("Ingrese un valor numérico")
    if dosis_recibidas >= DOSIS_NECESARIAS:
        print("Vacunación completa")
        completos += 1
    else:
        print("Vacunación incompleta")
        incompletos += 1
print(f"Total con esquema completo {completos}")
print(f"Total con esquema incompleto {incompletos}")
