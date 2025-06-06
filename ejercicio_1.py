print("====Bienvenido al sistema de vacunaciones====")

def solicitar_entero(mensaje):
    while True:  
        entrada = input(mensaje)
        if entrada.strip() == "":
            print("No se ingresaron números. Intente de nuevo.")
            continue
        try:
            numero = int(entrada)
            if 1 <= numero <= 10:
                return numero
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Debe ingresar un número entero.")

# Solicitar el número de personas registradas
registrados = solicitar_entero("Cantidad de personas registradas: ")

# Contadores
esquema_completo = 0
esquema_incompleto = 0

# Registrar dosis de cada uno
for i in range(registrados):
    dosis = solicitar_entero(f"\n¿Cuántas dosis tiene la persona {i + 1}?: ")
    
    if dosis >= 3:
        esquema_completo += 1
    else:
        esquema_incompleto += 1

# Resultados finales
print(f"\nPersonas con el esquema completo: {esquema_completo}")
print(f"Personas con el esquema incompleto: {esquema_incompleto}")
