# Evaluación 2 – Fundamentos de Programación – Sección W607 – Año 2025

## 🧠 Instrucciones

1. Este repositorio contiene dos ejercicios.
2. Debes resolverlos individualmente.
3. Lee las instrucciones específicas en:
   - `Instrucciones_ejercicio_n1.md`
   - `Instrucciones_ejercicio_n2.md`
4. Crea un archivo `.py` para cada ejercicio:
   - `ejercicio1.py`
   - `ejercicio2.py`
5. Súbelos al mismo repositorio, pero **en una rama nueva con tu nombre** (ver abajo).

---

## 🧪 ¿Cómo parto?

### 1. Clona este repositorio

```bash
git clone https://github.com/hachimaki-dev/evaluacion_2_fundamentos_w607_2025.git
cd evaluacion_2_fundamentos_w607_2025
````

---

### 2. Crea tu rama

Usa tu nombre completo, todo en minúsculas y sin tildes:

```bash
git checkout -b evaluacion/nombre_apellido1_apellido2
```

Ejemplo:

```bash
git checkout -b evaluacion/camila_rodriguez_torres
```

---

### 3. Crea los archivos y resuelve los ejercicios

```bash
touch ejercicio1.py
touch ejercicio2.py
```

Edita cada archivo según lo que piden los `.md` del repo.

---

### 4. Guarda y sube tus cambios

```bash
git add ejercicio1.py ejercicio2.py
git commit -m "Evaluación completa"
git push origin evaluacion/nombre_apellido1_apellido2
```

---

## ❌ ¡No modificar la rama `main`!

Trabaja **solo en tu propia rama**.
No intentes subir nada a `main`. Esa rama es del profesor.

---

## 📬 ¿Dudas?

Consulta directamente al profesor.
La pauta de evaluación ya fue enviada por correo y está en el ambiente de aprendizaje.

---

## ✅ Checklist rápida

* [ ] Leí ambas instrucciones (`Instrucciones_ejercicio_n1.md` y `n2.md`)
* [ ] Cloné el repositorio correctamente
* [ ] Creé mi propia rama con mi nombre
* [ ] Resolví el `ejercicio1.py`
* [ ] Resolví el `ejercicio2.py`
* [ ] Subí los dos archivos en mi rama
* [ ] No toqué la rama `main`



---

## Evaluación: Puntajes y Escala de Notas

### Puntaje por indicador

| Indicador | Descripción breve           | Ponderación | 100% | 80%  | 60%  | 30%  | 0   |
| --------- | -------------------------- | ----------- | ---- | ---- | ---- | ---- | --- |
| IE 2.1.1  | Inicializa variables        | 5%          | 5.0  | 4.0  | 3.0  | 1.5  | 0   |
| IE 2.1.2  | Actualiza variables         | 10%         | 10.0 | 8.0  | 6.0  | 3.0  | 0   |
| IE 2.1.3  | Entrada/salida              | 15%         | 15.0 | 12.0 | 9.0  | 4.5  | 0   |
| IE 2.2.1  | Operaciones aritméticas     | 15%         | 15.0 | 12.0 | 9.0  | 4.5  | 0   |
| IE 2.2.2  | Manipula strings/lógicas    | 15%         | 15.0 | 12.0 | 9.0  | 4.5  | 0   |
| IE 2.3.1  | Sintaxis condicionales      | 15%         | 15.0 | 12.0 | 9.0  | 4.5  | 0   |
| IE 2.3.2  | Lógica condicionales        | 25%         | 25.0 | 20.0 | 15.0 | 7.5  | 0   |

🔢 **Puntaje total máximo:** 100 puntos  
📉 **Puntaje mínimo para aprobar (60%):** 60 puntos  

---

### Escala de notas al 60% de exigencia

| Puntaje (%) | Nota | Desempeño                             |
| ----------- | ---- | ----------------------------------- |
| 0           | 1.0  | Desempeño no logrado       |
| 30          | 2.5  | Desempeño incipiente                 |
| 45          | 3.5  | Desempeño insuficiente               |
| 59          | 3.9  | Casi aprueba                        |
| 60          | 4.0  | Desempeño aceptable (mínimo aprobado) |
| 70          | 4.75 | Buen desempeño                      |
| 80          | 5.5  | Alto desempeño                     |
| 90          | 6.25 | Muy buen desempeño                  |
| 100         | 7.0  | Desempeño destacado (perfecto)     |

---

### Nota mínima para aprobar: 4.0 (equivale a 60% o 60 puntos)

---

### Cómo calcular tu nota desde el puntaje (%)

Se usa la siguiente fórmula lineal para transformar el puntaje en nota:

```excel
=SI(Puntaje<60, 1 + (Puntaje/60)*3, 4 + ((Puntaje-60)/40)*3)
````

* `Puntaje` es el porcentaje total obtenido, de 0 a 100.
* Resultados menores a 60% son notas de reprobación (<4.0).
* La nota máxima es 7.0 para 100%.

---

**Resumen:**

* Para aprobar necesitas al menos 60 puntos (60%).
* El puntaje total es la suma ponderada de cada indicador evaluado.
* La nota final se calcula con la fórmula anterior y se asocia al desempeño descrito en la tabla.

