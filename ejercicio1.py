valor_arancel = 1800000
valor_matricula = 90000

promedio = float(input("Ingresa el promedio correspondiente (1/7) "))
quintil = int(input("Ingresa al quintil que corresponde (1/5) "))

descuento_arancel = 0
descuento_matricula = 0

if promedio > 6.0 and quintil == 1 or quintil == 2:
   descuento_arancel = 0.20
   print("Recibiste un descuento del 20%, en el arancel")
elif promedio > 6.0 and quintil == 3 or quintil == 4:
    descuento_arancel = 0.15
    print("Recibiste un descuento del 15%, en el arancel")
elif promedio > 5.0 or promedio <= 6.5 and quintil == 1 or quintil == 2:
    descuento_arancel = 0.13
    print("Recibiste un descuento del 13%, en el arancel")
elif promedio > 5.0 or promedio <= 6.5 and quintil == 3 or quintil == 4:
    descuento_arancel = 0.1
    print("Recibiste un descuento del 10%, en el arancel")
elif promedio < 5.0 and quintil == 5:
    descuento_arancel = 0
    print("No recibiste ningun beneficio")
if quintil == 1 or quintil == 2 or quintil == 3:
    descuento_matricula = 0.1
    print("Recibiste un descuento del 10%, en la matricula")
    if promedio >= 5.5:
        descuento_matricula += 0.05
        print("Recibiste una suma de 5% mas en el descuento de la matricula")

descuento_final_arancel = valor_arancel * descuento_arancel
descuento_final_matricula = valor_matricula * descuento_matricula

valor_final_arancel = valor_arancel - descuento_final_arancel
valor_final_matricula = valor_matricula - descuento_final_matricula

print(f"El valor del arancel es: ${valor_final_arancel}")
print(f"El valor del arancel es: ${valor_final_matricula}")