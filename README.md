# Simulación Evaluación Final Transversal

## Contexto del Problema

El concesionario **AutoUsados** se especializa en la venta de automóviles de segunda mano. Para gestionar su inventario, utilizan un sistema basado en dos diccionarios principales que contienen toda la información de los vehículos disponibles.

### Estructura de Datos

#### Diccionario "vehiculos"
Este diccionario almacena las características técnicas de cada automóvil, donde:
- **Clave**: Código único del vehículo (string)
- **Valor**: Lista con 7 elementos que representan las características del vehículo

| Índice | Campo | Descripción | Ejemplo |
|--------|-------|-------------|---------|
| 0 | Marca | Fabricante del vehículo | "Toyota", "Ford", "Chevrolet" |
| 1 | Año | Año de fabricación | 2018, 2020, 2015 |
| 2 | Kilometraje | Kilómetros recorridos | "45000km", "120000km" |
| 3 | Combustible | Tipo de combustible | "Gasolina", "Diesel", "Híbrido" |
| 4 | Transmisión | Tipo de transmisión | "Manual", "Automática" |
| 5 | Motor | Especificaciones del motor | "1.6L 4cil", "2.0L V6" |
| 6 | Color | Color del vehículo | "Blanco", "Negro", "Rojo" |

**Ejemplo del diccionario vehiculos:**
```python
vehiculos = {
    'TOY8475': ['Toyota', 2019, '65000km', 'Gasolina', 'Automática', '1.8L 4cil', 'Blanco'],
    'FOR2175': ['Ford', 2017, '85000km', 'Gasolina', 'Manual', '1.6L 4cil', 'Azul'],
    'CHE9834': ['Chevrolet', 2020, '25000km', 'Gasolina', 'Automática', '2.0L 4cil', 'Negro'],
    'NIS7654': ['Nissan', 2016, '95000km', 'Gasolina', 'Manual', '1.6L 4cil', 'Rojo'],
    'HYU4521': ['Hyundai', 2021, '15000km', 'Híbrido', 'Automática', '1.6L 4cil', 'Gris'],
    'KIA3456': ['Kia', 2018, '75000km', 'Diesel', 'Manual', '2.0L 4cil', 'Blanco'],
    'MAZ8901': ['Mazda', 2019, '55000km', 'Gasolina', 'Automática', '2.5L 4cil', 'Rojo'],
    'SUB2468': ['Subaru', 2020, '30000km', 'Gasolina', 'Manual', '2.0L 4cil', 'Verde'],
    # ... más vehículos
}
```

#### Diccionario "inventario"
Este diccionario almacena la información comercial de cada vehículo:
- **Clave**: Código único del vehículo (debe coincidir con "vehiculos")
- **Valor**: Lista con 2 elementos [precio, stock]

| Índice | Campo | Descripción | Ejemplo |
|--------|-------|-------------|---------|
| 0 | Precio | Precio de venta en pesos chilenos | 8500000, 12750000 |
| 1 | Stock | Cantidad disponible (0 = no disponible) | 1, 2, 0 |

**Ejemplo del diccionario inventario:**
```python
inventario = {
    'TOY8475': [8500000, 1], 
    'FOR2175': [6200000, 1], 
    'CHE9834': [12750000, 1],
    'NIS7654': [5400000, 2], 
    'HYU4521': [15200000, 1], 
    'KIA3456': [7800000, 1],
    'MAZ8901': [9200000, 1], 
    'SUB2468': [11500000, 0], 
    'HON1357': [6800000, 0],
    # ... más vehículos
}
```

---

## Requerimientos del Sistema

### Menú Principal
El programa debe mostrar un menú interactivo con las siguientes opciones:

```
*** MENU CONCESIONARIO AUTOUSADOS ***
1. Consultar inventario por marca.
2. Búsqueda por rango de precios.
3. Modificar precio de vehículo.
4. Salir del sistema.
```

### Funcionalidades Requeridas

#### 1. Consultar inventario por marca
- **Función**: `inventario_marca(marca)`
- **Parámetros**: 
  - `marca` (string): Nombre de la marca a consultar
- **Retorno**: No retorna valor (void)
- **Funcionalidad**:
  - Recibe una marca ingresada por el usuario
  - La búsqueda debe ser **insensible a mayúsculas/minúsculas**
  - Suma el stock total de todos los vehículos de esa marca
  - Muestra el resultado en pantalla
- **Validaciones**:
  - Si la marca no existe, mostrar stock 0
  - Considerar solo vehículos con stock > 0

**Formato de salida:**
```
El inventario de [MARCA] es: [TOTAL_STOCK]
```

#### 2. Búsqueda por rango de precios
- **Función**: `busqueda_precio(precio_min, precio_max)`
- **Parámetros**: 
  - `precio_min` (int): Precio mínimo del rango
  - `precio_max` (int): Precio máximo del rango
- **Retorno**: No retorna valor (void)
- **Funcionalidad**:
  - Busca todos los vehículos dentro del rango de precios especificado
  - Considera solo vehículos con stock > 0
  - Genera una lista de strings con formato "Marca--Código"
  - Ordena la lista alfabéticamente
  - Muestra la lista completa en pantalla

- **Validaciones obligatorias**:
  - Los precios deben ser números enteros
  - Si el usuario ingresa datos no numéricos, mostrar: "Debe ingresar valores enteros!!" y volver a preguntar
  - Usar manejo de excepciones (try-except)
  - Si no hay vehículos en el rango, mostrar: "No hay vehículos en ese rango de precios."
  - El precio mínimo debe ser menor o igual al precio máximo

**Formato de salida exitosa:**
```
Los vehículos en el rango de precios consultado son: ['Chevrolet--CHE9834', 'Ford--FOR2175', 'Toyota--TOY8475']
```

#### 3. Modificar precio de vehículo
- **Función**: `actualizar_precio(codigo, precio_nuevo)`
- **Parámetros**: 
  - `codigo` (string): Código del vehículo a actualizar
  - `precio_nuevo` (int): Nuevo precio del vehículo
- **Retorno**: 
  - `True`: Si la actualización fue exitosa
  - `False`: Si el código no existe
- **Funcionalidad**:
  - Actualiza el precio de un vehículo específico en el diccionario "inventario"
  - El programa principal debe manejar los mensajes según el valor retornado

- **Validaciones**:
  - Verificar que el código existe en el diccionario
  - El precio nuevo debe ser un número entero positivo

- **Flujo en el programa principal**:
  1. Solicitar código del vehículo
  2. Solicitar nuevo precio
  3. Llamar a la función `actualizar_precio()`
  4. Según el retorno:
     - `True`: Mostrar "Precio actualizado exitosamente!!"
     - `False`: Mostrar "El código del vehículo no existe!!"
  5. Preguntar: "¿Desea actualizar otro precio (s/n)?"
     - Si responde "s": Repetir el proceso
     - Si responde "n": Volver al menú principal

#### 4. Salir del sistema
- Mostrar mensaje: "Sistema finalizado correctamente."
- Terminar la ejecución del programa

### Validaciones Generales del Menú

- Si el usuario ingresa una opción inválida en el menú principal:
  - Mostrar: "Debe seleccionar una opción válida!!"
  - Volver a mostrar el menú

---

## Ejemplo de Ejecución Completa

```
*** MENU CONCESIONARIO AUTOUSADOS ***
1. Consultar inventario por marca.
2. Búsqueda por rango de precios.
3. Modificar precio de vehículo.
4. Salir del sistema.
Ingrese opción: 1

Ingrese marca a consultar: Toyota
El inventario de Toyota es: 1

*** MENU CONCESIONARIO AUTOUSADOS ***
1. Consultar inventario por marca.
2. Búsqueda por rango de precios.
3. Modificar precio de vehículo.
4. Salir del sistema.
Ingrese opción: 1

Ingrese marca a consultar: bmw
El inventario de BMW es: 0

*** MENU CONCESIONARIO AUTOUSADOS ***
1. Consultar inventario por marca.
2. Búsqueda por rango de precios.
3. Modificar precio de vehículo.
4. Salir del sistema.
Ingrese opción: 2

Ingrese precio mínimo: 6000000
Ingrese precio máximo: 9000000
Los vehículos en el rango de precios consultado son: ['Ford--FOR2175', 'Kia--KIA3456', 'Toyota--TOY8475']

*** MENU CONCESIONARIO AUTOUSADOS ***
1. Consultar inventario por marca.
2. Búsqueda por rango de precios.
3. Modificar precio de vehículo.
4. Salir del sistema.
Ingrese opción: 2

Ingrese precio mínimo: hola
Debe ingresar valores enteros!!
Ingrese precio mínimo: 20000000
Ingrese precio máximo: 25000000
No hay vehículos en ese rango de precios.

*** MENU CONCESIONARIO AUTOUSADOS ***
1. Consultar inventario por marca.
2. Búsqueda por rango de precios.
3. Modificar precio de vehículo.
4. Salir del sistema.
Ingrese opción: 3

Ingrese código del vehículo a actualizar: TOY8475
Ingrese precio nuevo: 9200000
Precio actualizado exitosamente!!
¿Desea actualizar otro precio (s/n)?: s

Ingrese código del vehículo a actualizar: BMW123
Ingrese precio nuevo: 15000000
El código del vehículo no existe!!
¿Desea actualizar otro precio (s/n)?: n

*** MENU CONCESIONARIO AUTOUSADOS ***
1. Consultar inventario por marca.
2. Búsqueda por rango de precios.
3. Modificar precio de vehículo.
4. Salir del sistema.
Ingrese opción: 8

Debe seleccionar una opción válida!!

*** MENU CONCESIONARIO AUTOUSADOS ***
1. Consultar inventario por marca.
2. Búsqueda por rango de precios.
3. Modificar precio de vehículo.
4. Salir del sistema.
Ingrese opción: 4

Sistema finalizado correctamente.
```

---

## Notas Importantes para la Implementación

### Manejo de Excepciones
- Implementar try-except para la validación de entrada de números enteros
- Capturar `ValueError` cuando el usuario ingrese texto en lugar de números

### Estructura del Código
- El programa debe estar estructurado con funciones claramente definidas
- Cada función debe cumplir con su responsabilidad específica
- El código principal (main) debe manejar el flujo del menú y las interacciones con el usuario

### Consideraciones Técnicas
- Los datos de entrada del usuario aparecen en **negrita** en los ejemplos
- Todas las comparaciones de strings deben ser insensibles a mayúsculas/minúsculas
- El ordenamiento debe ser alfabético ascendente
- Los diccionarios pueden contener más datos de los mostrados en los ejemplos (indicado por "...")

### Criterios de Evaluación
- Correcta implementación de las funciones requeridas
- Manejo adecuado de excepciones y validaciones
- Funcionalidad completa del menú interactivo
- Formato correcto de salida según los ejemplos proporcionados
- Eficiencia y claridad del código