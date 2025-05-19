promedio = float(input("Ingrese el promedio con el egresó: "))
quintil = int(input("Ingrese el quintil al que pertenece (1, 2, 3 , 4 o 5): "))

# Valores Base
arancel = 1800000
matricula = 90000

# Inicializar variables
descuento_a = 0
descuento_m = 0

#Descuentos Arancel
if (promedio > 6.0) and (quintil == 1 or quintil == 2):
    descuento_a = arancel * 0.2
    arancel = arancel - descuento_a
elif (promedio > 6.0) and (quintil == 3 or quintil == 4):
    descuento_a = arancel * 0.15
    arancel = arancel - descuento_a
elif (6.0 >= promedio > 5.0) and (quintil == 1 or quintil == 2):
    descuento_a = arancel * 0.13
    arancel = arancel - descuento_a
elif (6.0 >= promedio > 5.0) and (quintil == 3 or quintil == 4):
    descuento_a = arancel * 0.1
    arancel = arancel - descuento_a
else:
    print("No obtienes ningún descuento en el arancel.")


#Descuentos Matrícula
if quintil == 1 or quintil == 2 or quintil == 3:
    descuento_m = matricula * 0.1
    if promedio >= 5.5:
        descuento_m = matricula * 0.15
    matricula = matricula - descuento_m
else:
    print("No obtienes ningún descuento en la matrícula.")


print(f"El valor final de tu arancel es: {arancel:0.0f}")
print(f"El valor final de tu matrícula es: {matricula:0.0f}")