# Instrucciones del ejercicio N°2

## Objetivo

Desarrollar un programa en **Python** que permita:

1. **Generar un número aleatorio** dentro de un rango definido por el usuario.
2. Simular un **juego de adivinanza** con hasta **3 intentos**.

---

## Requisitos del Programa

El programa debe hacer lo siguiente:

1. Solicitar al usuario **dos números enteros** que representen el **límite inferior y superior** de un rango numérico.

   * El primer número ingresado (límite inferior) debe ser **menor** que el segundo (límite superior).

2. Usar la función `randint()` para **generar un número aleatorio** dentro del rango indicado.

---

## Sugerencia para generar el número aleatorio

```python
from random import randint  # Importa la función randint
numero = randint(num1, num2)  # Genera un número aleatorio entre num1 y num2 (incluyéndolos)
```

**Ejemplo:**
`randint(1, 10)` genera un número aleatorio entre 1 y 10, incluyendo ambos extremos.

---

## Reglas del Juego de Adivinanza

* El usuario tiene **3 intentos** para adivinar el número secreto.
* En el **primer intento**, si no acierta, el programa debe indicar si el número a adivinar es **mayor o menor**.
* En el **segundo intento**, si tampoco acierta:

  * Nuevamente se debe decir si el número es **mayor o menor**.
  * Además, se debe entregar una **pista**, indicando cuál de los dos números ingresados anteriormente está **más cerca del número secreto**.
* En el **tercer intento**, si aún no adivina, el programa debe mostrar el mensaje **“Perdiste”** y revelar el número correcto.
* Si el usuario adivina el número en **cualquier intento**, el juego debe terminar con el mensaje:
  **“Felicitaciones, adivinaste.”**

---

## Ejemplos

### Ejemplo 1

```plaintext
Ingrese límite inferior: 0  
Ingrese límite superior: 10  

Intente adivinar: 2  
El número es mayor.  

Intente de nuevo: 8  
El número es mayor.  
Te daré una pista:  
El número que buscas está más cerca de 8 que de 2  

Intente la última vez: 9  
Perdiste.  
El número era: 10
```

---

### Ejemplo 2

```plaintext
Ingrese límite inferior: 1  
Ingrese límite superior: 15  

Intente adivinar: 8  
Felicitaciones, adivinaste en el primer intento.
```

---

### Ejemplo 3

```plaintext
Ingrese límite inferior: 0  
Ingrese límite superior: 8  

Intente adivinar: 3  
El número es mayor.  

Intente de nuevo: 4  
Felicitaciones, adivinaste en su segundo intento.
```

---

### Ejemplo 4

```plaintext
Ingrese límite inferior: 5  
Ingrese límite superior: 20  

Intente adivinar: 10  
El número es menor.  

Intente de nuevo: 5  
El número es mayor.  
Te daré una pista:  
El número que buscas está más cerca de 5 que de 10  

Intente la última vez: 6  
Perdiste  
El número era: 7
```

---

## Recomendaciones

* Usa `int(input())` para obtener los valores ingresados por el usuario.
* Asegúrate de validar que el primer número sea **menor que** el segundo.
* Usa estructuras condicionales (`if`, `elif`, `else`) y funciones matemáticas como `abs()` para calcular cuál número está más cerca del secreto.
* El programa debe ser claro y amigable para el usuario.
