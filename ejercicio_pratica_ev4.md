# Sistema de Reservas - Zapatillas Strike

## Descripción del Proyecto

Debes crear un programa en Python que simule un tótem de autoatención para reservas de zapatillas en la tienda "Zapatillas Strike". El programa debe permitir a los usuarios reservar zapatillas, buscar reservas existentes y consultar el stock disponible.

## Objetivos de Aprendizaje

- Implementar un menú interactivo usando estructuras de control
- Utilizar funciones para organizar el código
- Manejar listas para almacenar información
- Aplicar validaciones de entrada con try-except
- Implementar lógica de negocio con condiciones

## Especificaciones del Sistema

### Menú Principal

El programa debe mostrar el siguiente menú de forma repetitiva hasta que el usuario elija salir:

```
TOTEM AUTOATENCIÓN RESERVA STRIKE
1.- Reservar zapatillas
2.- Buscar zapatillas reservadas
3.- Ver stock de reservas
4.- Salir
```

### Estructura de Datos

Utiliza las siguientes listas para almacenar la información:
- `nombres_compradores`: lista para almacenar los nombres de los compradores
- `pares_reservados`: lista para almacenar la cantidad de pares por comprador (1 para estándar, 2 para VIP)
- `tipos_reserva`: lista para almacenar el tipo de reserva ("estándar" o "VIP")

### Funcionalidades Requeridas

#### 1. Reservar Zapatillas

**Función:** `reservar_zapatillas()`

**Validaciones obligatorias:**
- El nombre del comprador no debe estar vacío
- El nombre no debe estar repetido en el sistema
- El comprador debe ingresar exactamente la frase secreta: `"EstoyEnListaDeReserva"` (respetando mayúsculas y minúsculas)
- Verificar que no se haya alcanzado el límite máximo de 20 reservas totales
- Solo se permite una reserva por comprador inicialmente

**Proceso:**
1. Solicitar nombre del comprador
2. Validar que el nombre no esté vacío y no esté repetido
3. Solicitar la frase secreta
4. Validar la frase secreta exacta
5. Verificar disponibilidad de stock
6. Registrar la reserva como estándar (1 par)

#### 2. Buscar Zapatillas Reservadas

**Función:** `buscar_reserva()`

**Proceso:**
1. Solicitar nombre del comprador a buscar
2. Buscar en la lista de nombres
3. Si existe la reserva:
   - Mostrar información actual (nombre, cantidad de pares, tipo)
   - Preguntar si desea upgradar a VIP
   - Si acepta upgradar: cambiar a 2 pares y tipo "VIP"
4. Si no existe: mostrar mensaje de error

#### 3. Ver Stock de Reservas

**Función:** `ver_stock()`

**Proceso:**
1. Calcular total de pares reservados (sumar todos los elementos de `pares_reservados`)
2. Calcular pares disponibles (20 - total reservado)
3. Mostrar la información

#### 4. Salir

**Función:** `salir_programa()`

Mostrar mensaje: "Programa terminado..." y terminar la ejecución.

### Validaciones y Manejo de Errores

#### Entrada del Menú
- Usar `try-except` para capturar entradas no numéricas
- Validar que la opción esté entre 1 y 4
- Mostrar "Debe ingresar una opción válida!!" para opciones incorrectas

#### Validación de Nombres
- Verificar que el nombre no esté vacío (usar `.strip()`)
- Verificar que el nombre no esté ya registrado

#### Validación de Frase Secreta
- Debe ser exactamente: `"EstoyEnListaDeReserva"`
- Mostrar "Error: palabra clave incorrecta. Reserva no realizada." si es incorrecta

#### Validación de Stock
- Verificar que no se exceda el límite de 20 reservas totales
- Considerar que las reservas VIP ocupan 2 espacios

## Estructura del Código

```python
# Variables globales (listas)
nombres_compradores = []
pares_reservados = []
tipos_reserva = []

def mostrar_menu():
    # Código para mostrar el menú

def reservar_zapatillas():
    # Implementar funcionalidad de reserva

def buscar_reserva():
    # Implementar búsqueda de reservas

def ver_stock():
    # Implementar visualización de stock

def salir_programa():
    # Implementar salida del programa

def main():
    # Función principal con el bucle del menú
    
if __name__ == "__main__":
    main()
```

## Ejemplos de Ejecución

### Reserva Exitosa
```
-- Reservar Zapatillas --
Nombre del comprador: Juan Perez
Digite la palabra secreta para confirmar la reserva: EstoyEnListaDeReserva
Reserva realizada exitosamente para Juan Perez.
```

### Error en Frase Secreta
```
-- Reservar Zapatillas --
Nombre del comprador: Maria Lopez
Digite la palabra secreta para confirmar la reserva: EstoyEnListaDeReservas
Error: palabra clave incorrecta. Reserva no realizada.
```

### Upgrade a VIP
```
-- Buscar Zapatillas Reservadas --
Nombre del comprador a buscar: Juan Perez
Reserva encontrada: Juan Perez - 1 par(es) (estándar).
¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): s
Reserva actualizada a VIP. Ahora Juan Perez tiene 2 pares reservados.
```

## Criterios de Evaluación

- **Funcionalidad completa:** Todas las opciones del menú funcionan correctamente
- **Validaciones:** Manejo adecuado de errores con try-except
- **Estructura:** Uso correcto de funciones separadas
- **Lógica:** Implementación correcta de las reglas de negocio
- **Interfaz:** Mensajes claros y formato consistente

## Consejos de Implementación

1. Comienza implementando el menú principal y la estructura básica
2. Implementa una función a la vez y pruébala antes de continuar
3. Usa comentarios para explicar la lógica compleja
4. Prueba todos los casos de error posibles
5. Verifica que las listas se mantengan sincronizadas (mismo índice para el mismo comprador en todas las listas)

## Entrega

Entrega un archivo `.py` con el código completo y funcional. El programa debe ejecutarse sin errores y cumplir con todas las especificaciones mencionadas.