promedio_final = float(input("Ingresa el promedio final con el que saliste del colegio o el liceo: "))
print("Ingresa tu nivel socioeconomico, donde 1 representa mayor vulnerabilidad y 5 menor vulnerabilidad: ")
quintil_socioeconomico = int(input("1-5: "))

arancel_final = 1800000
valor_matricula = 90000
descuento_arancel = 0.0
descuento_matricula = 0.0

if promedio_final == 6.0 and (quintil_socioeconomico == 1 or quintil_socioeconomico == 2):
    descuento_arancel = 0.2

elif promedio_final == 6.0 and (quintil_socioeconomico == 3 or quintil_socioeconomico == 4):
    descuento_arancel = 0.15

elif 5.0 < promedio_final <= 6.0 and (quintil_socioeconomico == 1 or quintil_socioeconomico == 2):
    descuento_arancel = 0.13

elif 5.0 < promedio_final <= 6.0 and (quintil_socioeconomico == 3 or quintil_socioeconomico == 4):
    descuento_arancel = 0.1

else:
    descuento_arancel = 0

if promedio_final >= 5.5 and (quintil_socioeconomico == 1 or  quintil_socioeconomico == 2 or quintil_socioeconomico == 3):
    descuento_matricula = 0.1
elif promedio_final > 5.5 and (quintil_socioeconomico == 1 or quintil_socioeconomico == 2 or quintil_socioeconomico == 3):
    descuento_matricula = 0.15
else:
    descuento_matricula = 0

valor_a = arancel_final - (arancel_final * descuento_arancel)

valor_m = valor_matricula - (valor_matricula * descuento_matricula)

print("El valor final del arancel es: ", valor_a)
print("El valor final de la Matricula es: ", valor_m)