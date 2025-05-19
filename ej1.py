promedio = (input("Ingrese su promedio: "))
quintil = int(input("Ingrese el quintil 1, 2, 3, 4 o 5: "))

arancel_base = 1800000
matricula_base = 90000

if quintil == 1:
    descuento_arancel = 0.20
    descuento_matricula = 0.15
elif quintil == 2:
    descuento_arancel = 0.15
    descuento_matricula = 0.10
elif quintil == 3:
    descuento_arancel = 0.10
    descuento_matricula = 0.05
elif quintil == 4:
    descuento_arancel = 0.10
    descuento_matricula = 0.05
else:
    descuento_arancel = 0.0
    descuento_matricula = 0.0

valor_arancel = arancel_base * (1 - descuento_arancel)
valor_matricula = matricula_base * (1 - descuento_matricula)

print(f"El valor del arancel es: {valor_arancel :,}")
print("El valor de la matrícula es:", valor_matricula)
