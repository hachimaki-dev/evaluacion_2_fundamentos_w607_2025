promedio = float(input("Ingrese el promedio final del estudiante: \n"))
quintil = int(input("Ingrese en que quintil esta (1, 2, 3, 4, 5): \n"))
arancel = 1800000
matricula = 90000

descuento_arancel = 0

descuento_matricula = 0

if promedio > 6 and quintil in [1, 2]:
    descuento_arancel = 0.20
elif promedio > 6 and quintil in [3, 4]:
    descuento_arancel = 0.15
elif 5. > promedio >= 6 and quintil in [1, 2]:
    descuento_arancel = 0.13
elif 5. > promedio <= 6 and quintil in [3, 4]:
    descuento_arancel = 0.10

arancel -= arancel * descuento_arancel

if quintil in [1, 2, 3]:
    descuento_matricula = 0.10
    if promedio >= 5.5:
        descuento_matricula += 0.05

matricula -= matricula * descuento_matricula

print(f"El valor total del arancel es {arancel}")
print(f"El valor total de la matricula es {matricula}")