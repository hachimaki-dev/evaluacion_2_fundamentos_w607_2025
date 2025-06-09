# Ejercicio 2: Sistema de Menú con Manejo de Números

## Descripción del Problema

Debes crear un programa en Python que muestre un menú interactivo que permita al usuario ingresar números, ver el mayor número ingresado y calcular el promedio de todos los números ingresados.

## Objetivos de Aprendizaje

- Crear menús interactivos con bucles
- Validar entrada de while True:
    try:
        numero = int(input("Ingrese número: "))
        if 0 <= numero <= 100:
            # Número válido
            break
        else:
            print("Debe ingresar un número entre 0 y 100!!")
    except:
        print("Debe ingresar un número entero!!")datos con rangos específicos
- Manejar listas o variables para almacenar múltiples valores
- Calcular estadísticas básicas (mayor, promedio)
- Controlar el flujo del programa con estructuras condicionales

## Funcionalidades del Menú

El programa debe mostrar el siguiente menú:

```
*** MENU PRINCIPAL ***
1.- Ingresar número.
2.- Mostrar mayor.
3.- Mostrar promedio.
4.- Salir.
```

### Opción 1: Ingresar número

**Requisitos:**
- Debe permitir ingresar un número entero entre 0 y 100 (inclusive)
- Debe validar que sea un número entero (no decimal, no texto)
- Debe validar que esté en el rango [0, 100]

**Validaciones y mensajes:**
- Si no es un número entero: `"Debe ingresar un número entero!!"`
- Si está fuera del rango: `"Debe ingresar un número entre 0 y 100!!"`
- Si es válido: `"Ingreso exitoso"`

**Comportamiento:**
- Si el usuario ingresa algo inválido, debe volver a pedir el número
- Solo cuando el número sea válido, debe guardarse y volver al menú principal

### Opción 2: Mostrar mayor

**Función:**
- Mostrar el número más grande que se ha ingresado hasta el momento
- Mensaje: `"El número mayor hasta el momento es: X"`

**Caso especial:**
- Si no se han ingresado números: `"No se han ingresado números."`

### Opción 3: Mostrar promedio

**Función:**
- Calcular y mostrar el promedio de todos los números ingresados
- Mensaje: `"El promedio de los números ingresados es: X.XX"`
- El promedio debe mostrarse con 2 decimales

**Caso especial:**
- Si no se han ingresado números: `"No se han ingresado números."`

### Opción 4: Salir

**Función:**
- Terminar el programa
- Mensaje: `"Fin del programa. Adiós."`

### Validación del menú

**Comportamiento:**
- Si el usuario ingresa una opción que no existe (diferente de 1, 2, 3, 4)
- Mostrar: `"Debe ingresar una opción válida."`
- Volver a mostrar el menú

## Conceptos Técnicos Importantes

### Estructura del Programa

Tu programa necesitará:

1. **Bucle principal** que mantenga el menú activo hasta que el usuario elija salir
2. **Lista o variables** para almacenar los números ingresados
3. **Funciones de validación** para verificar entrada de datos
4. **Estructuras condicionales** para manejar cada opción del menú

### Almacenamiento de Datos

Tienes dos opciones para guardar los números:
- **Lista**: Para guardar todos los números y calcular estadísticas
- **Variables separadas**: Una para el mayor, otra para la suma y otra para el contador

### Validación de Números

```python
# Ejemplo de validación

```

### Cálculo del Promedio

Para calcular el promedio necesitas:
- La suma de todos los números
- La cantidad de números ingresados
- Promedio = suma / cantidad

## Estructura Recomendada

1. **Inicialización**: Crear variables o listas para almacenar datos
2. **Bucle principal**: Mostrar menú y procesar opciones
3. **Función de ingreso**: Validar y almacenar números
4. **Funciones de cálculo**: Mayor y promedio
5. **Control de salida**: Terminar cuando se elija la opción 4

## Criterios de Evaluación

1. **Menú funcional**: El menú se muestra correctamente y responde a todas las opciones
2. **Validación robusta**: Maneja correctamente entradas inválidas
3. **Rangos correctos**: Valida que los números estén entre 0 y 100
4. **Cálculos precisos**: Mayor y promedio se calculan correctamente
5. **Mensajes exactos**: Los mensajes coinciden exactamente con lo especificado
6. **Casos especiales**: Maneja correctamente cuando no hay números ingresados
7. **Flujo del programa**: El programa continúa hasta que el usuario elija salir

## Consejos para el Desarrollo

1. **Planifica la estructura**: Piensa en qué datos necesitas guardar antes de empezar
2. **Desarrolla por partes**: Primero el menú básico, luego cada funcionalidad
3. **Prueba cada opción**: Verifica que cada opción del menú funcione correctamente
4. **Valida exhaustivamente**: Prueba con números válidos, inválidos, decimales, texto
5. **Revisa los mensajes**: Asegúrate de que coincidan exactamente con lo solicitado
6. **Prueba casos extremos**: Qué pasa si intentas ver el mayor sin haber ingresado números

## Ejemplo de Flujo de Datos

```
Inicio → Mostrar menú → Leer opción
    ↓
Opción 1: Validar número → Guardar → Volver al menú
Opción 2: Verificar si hay números → Mostrar mayor → Volver al menú  
Opción 3: Verificar si hay números → Calcular promedio → Volver al menú
Opción 4: Mostrar despedida → Terminar programa
Otra opción: Mostrar error → Volver al menú
```

## Consideraciones Especiales

- El programa debe funcionar indefinidamente hasta que se elija la opción 4
- Puedes ingresar múltiples números y el programa debe recordar todos
- Los cálculos deben actualizarse cada vez que se ingresa un nuevo número
- La validación debe ser robusta para manejar cualquier tipo de entrada del usuario