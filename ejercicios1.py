#Ejercicio 1, calcular descuentos de arancel y matricula
arancel = 1800000
matricula = 90000
print("-Bienvenid@ al portal de beneficios estudiantiles")
print("-Este sistema trabaja en base a filtros como al quintil al cual")
print("pertenece y a su promedio con el cual egresó de su liceo/colegio")
print("#######################-Ingreso de datos-#######################")
print("Debe ingresar el promedio con el que egresó de su liceo/colegio")
print("#Nota mínima 1.0 y nota máxima 7.0")
print("Ej: 5.2, 6.5. 7.0, 4.6")
promedio = float(input("Ingrese su promedio: "))
print("Debe ingresar el quintil al que pertenece")
print("Los quintiles son del 1 al 5")
print("Ej: 1, 2, 3, 4 y 5")
quintil = int(input("Ingrese el quintil al que pertenece: "))

#Descuento del arancel
if promedio > 6.0 and (quintil == 1 or quintil == 2):
    descuento = 0.2
    valor_final_arancel = (arancel)-(arancel*descuento)
elif promedio > 6.0 and (quintil == 2 or quintil == 4):
    descuento = 0.15
    valor_final_arancel = (arancel)-(arancel*descuento)
elif (promedio > 5.0 and promedio <= 6.0) and (quintil == 1 or quintil == 2):
    descuento = 0.13
    valor_final_arancel = (arancel)-(arancel*descuento)
elif (promedio > 5.0 and promedio <= 6.0) and (quintil == 3 or quintil == 4):
    descuento = 0.1
    valor_final_arancel = (arancel)-(arancel*descuento)
else:
    descuento = 0
    valor_final_arancel = (arancel)-(arancel*descuento)

#Descuento de matrícula
if (quintil == 1 or quintil == 2 or quintil ==3) and (promedio >= 5.5):
    descuento_m = 0.15
    valor_final_matricula = (matricula)-(matricula*descuento_m)
elif (quintil == 1 or quintil == 2 or quintil ==3):
    descuento_m = 0.1
    valor_final_matricula = (matricula)-(matricula*descuento_m)
elif (promedio >= 5.5):
    descuento_m = 0.05
    valor_final_matricula = (matricula)-(matricula*descuento_m)
else:
    descuento_m = 0
    valor_final_matricula = (matricula)-(matricula*descuento_m)

print(f"Su costo base de arancel es de {arancel}")
print(f"Su costo base de matrícula es de {matricula}")
print("Depués de evaluar sus beneficios:")
print(f"Su arancel quedó con un costo de {valor_final_arancel}")
print(f"Su matrícula quedo con un valor final de {valor_final_matricula}")