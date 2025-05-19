# Desarrolle un programa en python que permita calcular los nemeficios a los estudiantes de primer año segun sus condiciones academicas y socioeconomicas. 
# Las condiciones academicas estan basadas en el promedio final con el que salieron del colegio o liceo. Las condiciones socioeconomicas
# estan basadas segun el quintil al que pertenece su grupo familiar (5 quintiles en total). La tabla siguiente muestra el beneficio según 
# las condiciones recien mencionadas.

# Condicion Academica    Condicion Socioeconomica	           Beneficio
# Promedio mayor a 6.0        Quintil 1 o 2		               20% descuento en arancel
# Promedio mayor a 6.0        Quintil 3 o 4		               15% descuento en arancel
# 5.0 < Promedio <= 6.0       Quintil 1 o 2		               13% descuento en arancel
# 5.0 < Promedio <= 6.0       Quintil 3 o 4		               10% descuento en arancel
# Cualquier promedio          Quintil 5 o promedio 5.0 o menos   0% descuento en arancel                |

# Ademas por el hecho de pertenecer al Quintil 1, 2 o 3 tiene un descuento de 10% en la matricula y si perteneciendo a esos Quintiles

# su promedio es mayor o igual a 5.5 se obtiene un 5% adicional.

# Suponga que el valor del arancel es de $1.800.000 y el valor de la matricula es de $90.000.

# Ejemplo 1:
# Ingerese promedio: 6.5
# Ingerese quintil: 1
# El valor del arancel es: $1.440.000
# El valor de la matricula es: $76.500

# Ejemplo 2:
# Ingerese promedio: 4
# Ingerese quintil: 5
# El valor del arancel es: $1.800.000
# El valor de la matricula es: $90.000


arancel = 1800000
matricula = 90000

print("--------------------------------------------------------------")
print("----- Bienvenido al sistema de beneficios --------------------")
print("----- Ingrese su promedio final y quintil socioeconómico -----")
print("--------------------------------------------------------------")
print(". ")
promedio = float(input("----- Ingrese su promedio final :D -----: "))
print(". ")
quintil = int(input("----- Ingrese su quintil socioeconómico (1 al 5) -----: "))
print(". ")

descuento_arancel = 0
descuento_matricula = 0

if promedio > 6.0:
    if quintil == 1 or quintil == 2:
        descuento_arancel = 0.20
    elif quintil == 3 or quintil == 4:
        descuento_arancel = 0.15
elif promedio > 5.0:
    if quintil == 1 or quintil == 2:
        descuento_arancel = 0.13
    elif quintil == 3 or quintil == 4:
        descuento_arancel = 0.10

if quintil in [1, 2, 3]:
    descuento_matricula = 0.10
    if promedio >= 5.5:
        descuento_matricula += 0.05
elif quintil == 5 or promedio <= 5.0:
    descuento_matricula = 0.0

arancel_final = arancel - (arancel * descuento_arancel)
matricula_final = matricula - (matricula * descuento_matricula)

print("Resumen de descuentos:")
print("-----------------------------------------------------")
print(f"--- Arancel con descuento:   ----- [ ${int(arancel_final)} ] -----")
print(f"--- Matrícula con descuento: ----- [ ${int(matricula_final)}   ] -----")
print("-----------------------------------------------------")