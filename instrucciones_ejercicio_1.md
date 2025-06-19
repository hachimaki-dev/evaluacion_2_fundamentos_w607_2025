# Sistema de Gestión de Usuarios

## Descripción General

Desarrolla un programa en Python que permita gestionar usuarios a través de un menú interactivo. El sistema debe permitir ingresar, buscar y eliminar usuarios con sus respectivas validaciones.

## Estructura de Datos Recomendada

Para este ejercicio, se recomienda utilizar un **diccionario** para almacenar los usuarios, ya que es más eficiente y fácil de manejar que múltiples listas. La estructura sugerida es:

```python
usuarios = {
    "nombre_usuario": {
        "sexo": "M" o "F",
        "contraseña": "contraseña_del_usuario"
    }
}
```

## Requisitos del Menú Principal

El programa debe mostrar un menú con las siguientes opciones:

```
MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
```

## Funcionalidades por Opción

### Opción 1: Ingresar Usuario

**Datos a solicitar:**
- Nombre de usuario
- Sexo
- Contraseña

**Validaciones obligatorias:**

1. **Nombre de usuario:** No debe estar repetido en el sistema
2. **Sexo:** Solo acepta "F" (femenino) o "M" (masculino)
3. **Contraseña:** Debe cumplir todos estos requisitos:
   - Mínimo 8 caracteres de longitud
   - Al menos 1 número
   - Al menos 1 letra
   - No puede contener espacios en blanco

**Comportamiento:**
- Si el usuario ya existe, solicitar un nuevo nombre de usuario
- Si el sexo no es válido, solicitar nuevamente hasta obtener "F" o "M"
- Si la contraseña no cumple los requisitos, solicitar una nueva contraseña
- Una vez que todos los datos sean válidos, confirmar el ingreso exitoso

### Opción 2: Buscar Usuario

**Funcionalidad:**
- Solicitar el nombre de usuario a buscar
- Si el usuario existe: mostrar sexo y contraseña
- Si el usuario no existe: mostrar mensaje informativo

### Opción 3: Eliminar Usuario

**Funcionalidad:**
- Solicitar el nombre de usuario a eliminar
- Si el usuario existe: eliminarlo y mostrar mensaje de confirmación
- Si el usuario no existe: mostrar mensaje de error

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
- `ingresar_usuario()`: Maneja toda la lógica de ingreso de usuarios
- `buscar_usuario()`: Maneja la búsqueda de usuarios
- `eliminar_usuario()`: Maneja la eliminación de usuarios
- `validar_contraseña()`: Valida si una contraseña cumple los requisitos
- `validar_sexo()`: Valida si el sexo ingresado es correcto

## Ejemplo de Ejecución

```
MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 1

Ingrese nombre de usuario: J.Rojas
Ingrese sexo: hombre
Debe ingresar M o F solamente. Intente de nuevo.
Ingrese sexo: M
Ingrese contraseña: 1234qwer
Contraseña válida.
Usuario ingresado con éxito!

MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 1

Ingrese nombre de usuario: J.Rojas
Usuario ya existe. Intente otro.
Ingrese nombre de usuario: L.Pereira
Ingrese sexo: F
Ingrese contraseña: 12as34 df
Contraseña no válida. Intente otra.
Ingrese contraseña: as1234yuioj
Contraseña válida.
Usuario ingresado con éxito!

MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 2

Ingrese usuario a buscar: L.Pereira
El sexo del usuario es: F y la contraseña es: as1234yuioj

MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 2

Ingrese usuario a buscar: S.Castro
El usuario no se encuentra.

MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 3

Ingrese usuario a eliminar: L.Rojas
No se pudo eliminar el usuario!

MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 3

Ingrese usuario a eliminar: L.Pereira
Usuario eliminado con éxito!

MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 5
Debe ingresar una opción válida!

MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
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
