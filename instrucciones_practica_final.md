# Sistema de Gestión de Videojuegos

## Descripción General

Desarrolla un programa en Python que permita gestionar videojuegos a través de un menú interactivo. El sistema debe permitir ingresar, buscar y eliminar videojuegos con sus respectivas validaciones.

## Estructura de Datos Recomendada

Para este ejercicio, se recomienda utilizar un **diccionario** para almacenar los videojuegos, ya que es más eficiente y fácil de manejar que múltiples listas. La estructura sugerida es:

```python
videojuegos = {
    "nombre_videojuego": {
        "categoria": "A" o "I",
        "codigo": "codigo_del_videojuego"
    }
}
```

## Requisitos del Menú Principal

El programa debe mostrar un menú con las siguientes opciones:

```
MENU PRINCIPAL
1.- Ingresar videojuego.
2.- Buscar videojuego.
3.- Eliminar videojuego.
4.- Salir.
```

## Funcionalidades por Opción

### Opción 1: Ingresar Videojuego

**Datos a solicitar:**
- Nombre de videojuego
- Categoría
- Código

**Validaciones obligatorias:**

1. **Nombre de videojuego:** No debe estar repetido en el sistema
2. **Categoría:** Solo acepta "A" (triple A) o "I" (indie)
3. **Código:** Debe cumplir todos estos requisitos:
   - Mínimo 8 caracteres de longitud
   - Al menos 1 número
   - Al menos 1 letra
   - No puede contener espacios en blanco

**Comportamiento:**
- Si el videojuego ya existe, solicitar un nuevo nombre de videojuego
- Si la categoría no es válida, solicitar nuevamente hasta obtener "A" o "I"
- Si el código no cumple los requisitos, solicitar un nuevo código
- Una vez que todos los datos sean válidos, confirmar el ingreso exitoso

### Opción 2: Buscar Videojuego

**Funcionalidad:**
- Solicitar el nombre de videojuego a buscar
- Si el videojuego existe: mostrar categoría y código
- Si el videojuego no existe: mostrar mensaje informativo

### Opción 3: Eliminar Videojuego

**Funcionalidad:**
- Solicitar el nombre de videojuego a eliminar
- Si el videojuego existe: eliminarlo y mostrar mensaje de confirmación
- Si el videojuego no existe: mostrar mensaje de error

### Opción 4: Salir

**Funcionalidad:**
- Terminar la ejecución del programa

### Opción Inválida

**Funcionalidad:**
- Si se ingresa una opción que no está en el menú (1-4), mostrar mensaje de error y volver al menú

## Requisitos Técnicos

### Funciones Obligatorias

**Todas las opciones del menú deben estar implementadas mediante funciones separadas del código principal (main).**

**Funciones sugeridas:**
- `mostrar_menu()`: Muestra el menú principal
- `ingresar_videojuego()`: Maneja toda la lógica de ingreso de videojuegos
- `buscar_videojuego()`: Maneja la búsqueda de videojuegos
- `eliminar_videojuego()`: Maneja la eliminación de videojuegos
- `validar_codigo()`: Valida si un código cumple los requisitos
- `validar_categoria()`: Valida si la categoría ingresada es correcta

## Ejemplo de Ejecución

```
MENU PRINCIPAL
1.- Ingresar videojuego.
2.- Buscar videojuego.
3.- Eliminar videojuego.
4.- Salir.
Ingrese opción: 1

Ingrese nombre de videojuego: FIFA2023
Ingrese categoría: deportes
Debe ingresar A o I solamente. Intente de nuevo.
Ingrese categoría: A
Ingrese código: 1234qwer
Código válido.
Videojuego ingresado con éxito!

MENU PRINCIPAL
1.- Ingresar videojuego.
2.- Buscar videojuego.
3.- Eliminar videojuego.
4.- Salir.
Ingrese opción: 1

Ingrese nombre de videojuego: FIFA2023
Videojuego ya existe. Intente otro.
Ingrese nombre de videojuego: Minecraft
Ingrese categoría: I
Ingrese código: 12as34 df
Código no válido. Intente otro.
Ingrese código: as1234yuioj
Código válido.
Videojuego ingresado con éxito!

MENU PRINCIPAL
1.- Ingresar videojuego.
2.- Buscar videojuego.
3.- Eliminar videojuego.
4.- Salir.
Ingrese opción: 2

Ingrese videojuego a buscar: Minecraft
La categoría del videojuego es: I y el código es: as1234yuioj

MENU PRINCIPAL
1.- Ingresar videojuego.
2.- Buscar videojuego.
3.- Eliminar videojuego.
4.- Salir.
Ingrese opción: 2

Ingrese videojuego a buscar: CallOfDuty
El videojuego no se encuentra.

MENU PRINCIPAL
1.- Ingresar videojuego.
2.- Buscar videojuego.
3.- Eliminar videojuego.
4.- Salir.
Ingrese opción: 3

Ingrese videojuego a eliminar: Fortnite
No se pudo eliminar el videojuego!

MENU PRINCIPAL
1.- Ingresar videojuego.
2.- Buscar videojuego.
3.- Eliminar videojuego.
4.- Salir.
Ingrese opción: 3

Ingrese videojuego a eliminar: Minecraft
Videojuego eliminado con éxito!

MENU PRINCIPAL
1.- Ingresar videojuego.
2.- Buscar videojuego.
3.- Eliminar videojuego.
4.- Salir.
Ingrese opción: 5
Debe ingresar una opción válida!

MENU PRINCIPAL
1.- Ingresar videojuego.
2.- Buscar videojuego.
3.- Eliminar videojuego.
4.- Salir.
Ingrese opción: 4

Programa terminado...
```

## Consejos para la Implementación

1. **Usa un bucle principal** para mantener el menú activo hasta que el usuario elija salir
2. **Implementa validaciones robustas** para cada tipo de entrada
3. **Utiliza funciones auxiliares** para hacer el código más legible y mantenible
4. **Maneja los casos de error** de manera amigable para el usuario
5. **Prueba todas las funcionalidades** con diferentes casos de entrada