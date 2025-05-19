
prom = float(input("Ingrese su promedio (con el cual egresó de Enseñanza Media): "))

quintil = int(input("Ingrese su quintil (1, 2, 3, 4 o 5): "))

arancelbase = 1800000 #(1.8M)

matrbase = 90000 #(90K)

matrdesc = 0

arancelfin = 0

#Promedios 6 o superior

if prom > 6 and quintil == 1:
    matrdesc = matrbase * 0.85
    arancelfin = arancelbase * 0.80
    print(f"El valor final de su matrícula es de ${matrdesc}, y el de su arancel es de ${arancelfin}.")

elif prom > 6 and quintil == 2:
    matrdesc = matrbase * 0.85
    arancelfin = arancelbase * 0.85
    print(f"El valor final de su matrícula es de ${matrdesc}, y el de su arancel es de ${arancelfin}.")

elif prom > 6 and quintil == 3:
    matrdesc = matrbase * 0.85
    arancelfin = arancelbase * 0.85
    print(f"El valor final de su matrícula es de ${matrdesc}, y el de su arancel es de ${arancelfin}.")


elif prom > 6 and quintil == 4:
    matrdesc = matrbase * 0.95
    print(f"El valor final de su matrícula es de ${matrdesc}, y el de su arancel es de ${arancelbase}. No aplica descuento para el arancel.")

#Promedios mayores a 5.0 y menores o iguales a 6.0

elif (prom >= 5.0 and prom <= 6.0) and (quintil == 1):
    if prom >= 5.5:
        arancelfin = arancelbase * 0.87
        matrdesc = matrbase * 0.90
        print(f"El valor final de su matrícula es de ${matrdesc}, y el de su arancel es de ${arancelfin}.")
    else:
        arancelfin = arancelbase * 0.87
        print(f"El valor final de su matrícula es de ${matrbase}, y el de su arancel es de ${arancelfin}.")


elif (prom >= 5.0 and prom <= 6.0) and (quintil == 2):
    if prom >= 5.5:
        arancelfin = arancelbase * 0.87
        matrdesc = matrbase * 0.90
        print(f"El valor final de su matrícula es de ${matrdesc}, y el de su arancel es de ${arancelfin}.")
    else:
        arancelfin = arancelbase * 0.87
        print(f"El valor final de su matrícula es de ${matrbase}, y el de su arancel es de ${arancelfin}.")

elif (prom >= 5.0 and prom <= 6.0) and (quintil == 3):
    if prom >= 5.5:
        arancelfin = arancelbase * 0.90
        matrdesc = matrbase * 0.90
        print(f"El valor final de su matrícula es de ${matrdesc}, y el de su arancel es de ${arancelfin}.")
    else:
        arancelfin = arancelbase * 0.90
        print(f"El valor final de su matrícula es de ${matrbase}, y el de su arancel es de ${arancelfin}.")

elif (prom >= 5.0 and prom <= 6.0) and (quintil == 4):
    if prom >= 5.5:
        arancelfin = arancelbase * 0.90
        matrdesc = matrbase * 0.95
        print(f"El valor final de su matrícula es de ${matrdesc}, y el de su arancel es de ${arancelfin}.")
    else:
        arancelfin = arancelbase * 0.90
        print(f"El valor final de su matrícula es de ${matrbase}, y el de su arancel es de ${arancelfin}.")



# Quintil 5 o promedio 5.0 o menos

elif (prom <= 5.0 and prom >= 4.0) and (quintil == 5):
    if prom >= 5.5:
        matrdesc = matrbase * 0.95
        print(f"El valor final de su matrícula es de ${matrdesc}, y el de su arancel es de ${arancelbase}. No aplica descuento para el arancel.")
    else:
        print(f"El valor final de su matrícula es de ${matrbase}, y el de su arancel es de ${arancelbase}. No aplica descuento para el arancel ni para la matrícula.")

else:
    print("Error del programa: Datos no válidos o no hay descuentos aplicables.")