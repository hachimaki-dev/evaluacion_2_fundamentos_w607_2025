# Ejercicio 1: Sistema de Verificación de Vacunación
**Valor: 3 puntos**

## Descripción del Problema

Necesitas crear un programa en Python que funcione como un sistema simple para verificar si las personas han completado su esquema de vacunación.

## Objetivos de Aprendizaje

- Usar bucles `while` y `for`
- Manejar excepciones con `try-except`
- Trabajar con contadores y acumuladores
- Validar entrada de datos del usuario

## Instrucciones Paso a Paso

### Paso 1: Solicitar el número de personas
1. El programa debe preguntar cuántas personas se van a registrar
2. Este número debe ser **entero** (no decimales)
3. Si el usuario ingresa algo que no sea un número entero, mostrar el mensaje: `"Debe ingresar un número entero."`
4. Repetir la pregunta hasta que ingrese un número válido

### Paso 2: Registrar las dosis de cada persona
Para cada una de las N personas:
1. Preguntar cuántas dosis ha recibido
2. El número de dosis también debe ser **entero**
3. Si ingresa algo inválido, mostrar `"Debe ingresar un número entero."` y volver a preguntar
4. Una vez que ingrese un número válido:
   - Si tiene **3 o más dosis**: mostrar `"Esquema completo."`
   - Si tiene **menos de 3 dosis**: mostrar `"Esquema incompleto."`

### Paso 3: Mostrar el resumen final
Al final del programa, mostrar:
- Cuántas personas tienen esquema completo
- Cuántas personas tienen esquema incompleto

## Conceptos Importantes

### Manejo de Excepciones
Debes usar la estructura `try-except` para capturar errores cuando el usuario ingrese datos no válidos:

```python
try:
    numero = int(input("Ingrese un número: "))
    # Si llegamos aquí, el número es válido
except:
    print("Debe ingresar un número entero.")
    # Continuar pidiendo el número
```

### Bucles de Validación
Para asegurar que el usuario ingrese datos válidos, usa un bucle `while True` que solo se rompa cuando el dato sea correcto:

```python
while True:
    try:
        dato = int(input("Mensaje: "))
        break  # Sale del bucle si no hay error
    except:
        print("Error, intente de nuevo")
```

### Contadores
Necesitarás variables para contar:
- Personas con esquema completo
- Personas con esquema incompleto

## Criterios de Evaluación

1. **Validación de entrada**: El programa debe manejar correctamente entradas inválidas
2. **Lógica correcta**: Debe determinar correctamente si el esquema está completo (3+ dosis)
3. **Conteo preciso**: Debe contar correctamente las personas en cada categoría
4. **Mensajes apropiados**: Debe mostrar los mensajes exactos especificados
5. **Estructura del código**: Uso adecuado de bucles y estructuras de control

## Ejemplo de Ejecución

```
Ingrese la cantidad de personas a registrar: 2.5
Debe ingresar un número entero.
Ingrese la cantidad de personas a registrar: 3

Ingrese cantidad de dosis recibidas: 3
Esquema completo.
Ingrese cantidad de dosis recibidas: 1.7
Debe ingresar un número entero.
Ingrese cantidad de dosis recibidas: dos
Debe ingresar un número entero.
Ingrese cantidad de dosis recibidas: 2
Esquema incompleto.
Ingrese cantidad de dosis recibidas: 3
Esquema completo.

Se registraron 2 personas con esquema completo.
Se registraron 1 persona con esquema incompleto.
```

## Consejos para Resolver el Ejercicio

1. **Planifica antes de programar**: Piensa en los pasos que debe seguir tu programa
2. **Usa variables descriptivas**: Como `esquema_completo`, `esquema_incompleto`
3. **Define constantes**: El número de dosis necesarias (3) puede ser una variable
4. **Prueba tu código**: Intenta ingresar datos inválidos para verificar que funcione
5. **Revisa los mensajes**: Asegúrate de que coincidan exactamente con lo solicitado