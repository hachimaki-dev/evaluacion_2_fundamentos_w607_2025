# Instrucciones del ejercicio N°1 ()


## Objetivo

Desarrollar un programa en **Python** que calcule los **beneficios económicos** otorgados a estudiantes de primer año según sus condiciones **académicas** y **socioeconómicas**.

---

## Requisitos del Programa

El programa debe recibir dos datos de entrada:

1. **Promedio final** con el que el estudiante egresó del colegio o liceo.
2. **Quintil socioeconómico** al que pertenece su grupo familiar.
   (El quintil debe estar entre 1 y 5, donde 1 representa mayor vulnerabilidad y 5, menor).

Con estos datos, el programa debe calcular:

* El **valor final del arancel** (sobre un valor base de **\$1.800.000**).
* El **valor final de la matrícula** (sobre un valor base de **\$90.000**).

---

## Tabla de Beneficios - Descuento en el Arancel

| Promedio                          | Quintil                          | Descuento en Arancel |
| --------------------------------- | -------------------------------- | -------------------- |
| Mayor a 6.0                       | Quintil 1 o 2                    | 20%                  |
| Mayor a 6.0                       | Quintil 3 o 4                    | 15%                  |
| Mayor a 5.0 y menor o igual a 6.0 | Quintil 1 o 2                    | 13%                  |
| Mayor a 5.0 y menor o igual a 6.0 | Quintil 3 o 4                    | 10%                  |
| Cualquier promedio                | Quintil 5 o promedio 5.0 o menos | 0%                   |

---

## Descuento en Matrícula

* Si el estudiante pertenece al **quintil 1, 2 o 3**, recibe automáticamente un **10% de descuento en la matrícula**.
* Si además tiene un **promedio mayor o igual a 5.5**, recibe un **5% adicional**, acumulando un total de **15% de descuento en matrícula**.

---

## Supuestos

* Valor **base del arancel**: `$1.800.000`
* Valor **base de la matrícula**: `$90.000`

---

## Ejemplo 1

```plaintext
Ingrese su promedio: 6.5  
Ingrese el quintil (1, 2, 3, 4 o 5): 1  

El valor del arancel es: $1.440.000  
El valor de la matrícula es: $76.500
```

**Explicación:**

* 20% de descuento en arancel → 1.800.000 x 0.80 = **1.440.000**
* 10% + 5% = 15% de descuento en matrícula → 90.000 x 0.85 = **76.500**

---

## Ejemplo 2

```plaintext
Ingrese su promedio: 4  
Ingrese el quintil (1, 2, 3, 4 o 5): 5  

El valor del arancel es: $1.800.000  
El valor de la matrícula es: $90.000
```

**Explicación:**

* No aplica descuento en arancel (promedio bajo y quintil 5)
* No aplica descuento en matrícula

---

## Recomendaciones

* Usa **condicionales (`if`, `elif`, `else`)** para determinar los beneficios.
* Aplica correctamente las **porcentajes de descuento**.
* Asegúrate de que el programa sea **claro y fácil de entender** para cualquier usuario.
