## Ejercicio 1: Sistema de Verificación de Vacunación

## Descripción del Problema

#Necesitas crear un programa en Python que funcione como un sistema simple para verificar si las personas han completado su esquema de vacunación.

## Objetivos de Aprendizaje

# Usar bucles `while` y `for`
# Manejar excepciones con `try-except`
# Trabajar con contadores y acumuladores
# Validar entrada de datos del usuario

## Instrucciones Paso a Paso

### Paso 1: Solicitar el número de personas
#1. El programa debe preguntar cuántas personas se van a registrar
#2. Este número debe ser **entero** (no decimales)
#3. Si el usuario ingresa algo que no sea un número entero, mostrar el mensaje: `"Debe ingresar un número entero."`
#4.Repetir la pregunta hasta que ingrese un número válido

### Paso 2: Registrar las dosis de cada persona
#Para cada una de las N personas:
#Preguntar cuántas dosis ha recibido
#El número de dosis también debe ser **entero**
#Si ingresa algo inválido, mostrar `"Debe ingresar un número entero."` y volver a preguntar
#Una vez que ingrese un número válido:
#Si tiene **3 o más dosis**: mostrar `"Esquema completo."`
#Si tiene **menos de 3 dosis**: mostrar `"Esquema incompleto."`

### Paso 3: Mostrar el resumen final
#Al final del programa, mostrar:
#Cuántas personas tienen esquema completo
 #Cuántas personas tienen esquema incompleto


def vacunas(personas):
    completo = 0
    incompleto = 0
    for i in range(personas):
        while True:
            try:
                input_value = input(f"Dosis recibidas por persona {i + 1}: ")
                dosis = int(input_value)
                if dosis >= 0:
                    break
                else:
                    print("Debe ingresar un numero entero positivo.")
            except ValueError:
                print("Debe ingresar un numero entero.")
        if dosis >= 3:
            completo += 1
        else:
            incompleto += 1
    return completo, incompleto
def main():
    while True:
        try:
            personas = int(input("Ingrese el número de personas que se van a registrar: "))
            if personas > 0:
                break
            else:
                print("Debe ingresar un número entero positivo.")
        except ValueError:
            print("Debe ingresar un número entero.")
    completo, incompleto = vacunas(personas)
    print(f"Esquema completo: {completo}")
    print(f"Esquema incompleto: {incompleto}")

if __name__ == "__main__":
    main()

                

