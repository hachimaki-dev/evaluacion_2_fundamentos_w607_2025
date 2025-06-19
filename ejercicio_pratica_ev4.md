# Sistema de Reservas Blockbuster - Videojuegos

## Descripción del Proyecto

Debes crear un programa en Python que simule un sistema de reservas de videojuegos para Blockbuster. El programa debe permitir agregar reservas, buscar reservas existentes, eliminar reservas y mostrar todas las reservas registradas.

## Objetivos de Aprendizaje

- Implementar un menú interactivo usando while
- Utilizar funciones para organizar el código
- Manejar listas para almacenar información
- Aplicar operaciones básicas: agregar, buscar, eliminar elementos
- Implementar validaciones básicas de entrada

## Menú del Sistema

El programa debe mostrar el siguiente menú de forma repetitiva hasta que el usuario elija salir:

```
=== SISTEMA DE RESERVAS BLOCKBUSTER ===
1. Ingresar reserva
2. Buscar reserva
3. Eliminar reserva
4. Mostrar todas las reservas
5. Salir
```

## Estructura de Datos

Utiliza una lista simple para almacenar los nombres de los clientes que han reservado videojuegos:

```python
lista_reservas = []
```

## Funcionalidades Requeridas

### 1. Ingresar Reserva

**Función:** `ingresar_reserva(nombre_cliente)`

**Validaciones:**
- El nombre no debe estar vacío (después de aplicar `.strip()`)
- El nombre no debe estar duplicado en la lista
- Si el nombre ya existe, mostrar mensaje de error
- Si es válido, agregar a la lista y mostrar confirmación

**Mensajes:**
- Éxito: `"Reserva registrada exitosamente para [nombre]"`
- Error duplicado: `"El cliente [nombre] ya tiene una reserva registrada"`
- Error vacío: `"El nombre no puede estar vacío"`

### 2. Buscar Reserva

**Función:** `buscar_reserva(nombre_cliente)`

**Proceso:**
- Buscar el nombre en la lista usando un bucle for
- Si encuentra el nombre: `"El cliente [nombre] tiene una reserva registrada"`
- Si no lo encuentra: `"No se encontró reserva para [nombre]"`

### 3. Eliminar Reserva

**Función:** `eliminar_reserva(nombre_cliente)`

**Proceso:**
- Verificar si el nombre existe en la lista
- Si existe: eliminarlo y mostrar confirmación
- Si no existe: mostrar mensaje de error

**Mensajes:**
- Éxito: `"Reserva eliminada exitosamente para [nombre]"`
- Error: `"No se encontró reserva para [nombre]"`

### 4. Mostrar Todas las Reservas

**Función:** `mostrar_reservas()`

**Proceso:**
- Si la lista está vacía: `"No hay reservas registradas"`
- Si tiene elementos: mostrar todas las reservas numeradas

**Formato de salida:**
```
=== RESERVAS REGISTRADAS ===
1. Juan Pérez
2. María González
3. Carlos López
Total de reservas: 3
```

### 5. Salir

- Mostrar mensaje: `"Programa terminado. Gracias por usar el sistema de Blockbuster"`
- Terminar la ejecución del programa

## Validaciones Requeridas

### Validación del Menú
```python
try:
    opcion = int(input("Seleccione una opción (1-5): "))
    if opcion < 1 or opcion > 5:
        print("Opción inválida. Ingrese un número entre 1 y 5")
except ValueError:
    print("Error: Debe ingresar un número válido")
```

### Validación de Nombres
- Usar `.strip()` para eliminar espacios en blanco
- Verificar que no esté vacío después del strip
- Convertir a formato título para consistencia: `.title()`

## Estructura del Código

```python
# Lista global para almacenar las reservas
lista_reservas = []

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n=== SISTEMA DE RESERVAS BLOCKBUSTER ===")
    print("1. Ingresar reserva")
    print("2. Buscar reserva")
    print("3. Eliminar reserva")
    print("4. Mostrar todas las reservas")
    print("5. Salir")

def ingresar_reserva(nombre_cliente):
    """Agrega una nueva reserva a la lista"""
    # Implementar aquí

def buscar_reserva(nombre_cliente):
    """Busca una reserva en la lista"""
    # Implementar aquí

def eliminar_reserva(nombre_cliente):
    """Elimina una reserva de la lista"""
    # Implementar aquí

def mostrar_reservas():
    """Muestra todas las reservas registradas"""
    # Implementar aquí

def main():
    """Función principal que ejecuta el programa"""
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            
            if opcion == 1:
                nombre = input("Ingrese el nombre del cliente: ").strip().title()
                ingresar_reserva(nombre)
            elif opcion == 2:
                nombre = input("Ingrese el nombre a buscar: ").strip().title()
                buscar_reserva(nombre)
            elif opcion == 3:
                nombre = input("Ingrese el nombre a eliminar: ").strip().title()
                eliminar_reserva(nombre)
            elif opcion == 4:
                mostrar_reservas()
            elif opcion == 5:
                print("Programa terminado. Gracias por usar el sistema de Blockbuster")
                break
            else:
                print("Opción inválida. Ingrese un número entre 1 y 5")
        except ValueError:
            print("Error: Debe ingresar un número válido")

if __name__ == "__main__":
    main()
```

## Ejemplo de Ejecución

```
=== SISTEMA DE RESERVAS BLOCKBUSTER ===
1. Ingresar reserva
2. Buscar reserva
3. Eliminar reserva
4. Mostrar todas las reservas
5. Salir
Seleccione una opción (1-5): 1
Ingrese el nombre del cliente: juan perez
Reserva registrada exitosamente para Juan Perez

=== SISTEMA DE RESERVAS BLOCKBUSTER ===
1. Ingresar reserva
2. Buscar reserva
3. Eliminar reserva
4. Mostrar todas las reservas
5. Salir
Seleccione una opción (1-5): 2
Ingrese el nombre a buscar: Juan Perez
El cliente Juan Perez tiene una reserva registrada

=== SISTEMA DE RESERVAS BLOCKBUSTER ===
1. Ingresar reserva
2. Buscar reserva
3. Eliminar reserva
4. Mostrar todas las reservas
5. Salir
Seleccione una opción (1-5): 4
=== RESERVAS REGISTRADAS ===
1. Juan Perez
Total de reservas: 1

=== SISTEMA DE RESERVAS BLOCKBUSTER ===
1. Ingresar reserva
2. Buscar reserva
3. Eliminar reserva
4. Mostrar todas las reservas
5. Salir
Seleccione una opción (1-5): 5
Programa terminado. Gracias por usar el sistema de Blockbuster
```

## Consejos de Implementación

1. **Comienza con la estructura básica**: implementa el menú y el bucle principal primero
2. **Una función a la vez**: implementa y prueba cada función por separado
3. **Usa .strip() y .title()**: para mantener consistencia en los nombres
4. **Prueba todos los casos**: nombres vacíos, duplicados, nombres que no existen
5. **Mantén el código simple**: usa las estructuras básicas que ya conoces

## Entrega

Entrega un archivo `.py` con el código completo y funcional. El programa debe:
- Ejecutarse sin errores
- Implementar todas las funciones requeridas
- Manejar las validaciones básicas
- Mostrar mensajes claros al usuario
- Permitir salir solo con la opción 5