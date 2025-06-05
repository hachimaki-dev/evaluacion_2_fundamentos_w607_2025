# Ejercicio 1: Sistema de Verificación de Vacunación
lista = []

dosisCompletas = 0
dosisIncompletas = 0
numeroDePersonas = 0 

print("Bienvenido al verificador de vacunas, siga las instrucciones cuidadosamente")


### Paso 1: Solicitar el número de personas


while True:

    try:
        numeroDePersonas = int(input("Ingrese el número de personas a registrar: "))
        lista.append(numeroDePersonas)
        break

    except ValueError:
        print("Debe ingresar un número entero.")
        input("Presione la tecla Enter para reintentar")
        

### Paso 2: Registrar las dosis de cada persona
for i in range(numeroDePersonas):
    while True:
                
        try:
            dosisQuePosee = int(input("Ingrese la cantidad de dosis que posee: "))

            
            if dosisQuePosee >= 3:
                    dosisCompletas += 1
                    print("Esquema completo ")
                    lista.append(dosisCompletas)
                    break
            elif dosisQuePosee < 3:
                    dosisIncompletas += 1
                    print("Esquema incompleto")
                    lista.append(dosisCompletas)
                    break
            else:
                break 


        except ValueError:
            print("Debe ingresar un número entero.")
            input("Presione la tecla Enter para reintentar")

### Paso 3: Mostrar el resumen final
print(f"Se registraron:", dosisCompletas )
print(f"Se registraron:", dosisIncompletas )

