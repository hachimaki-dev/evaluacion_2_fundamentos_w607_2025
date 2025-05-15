valor_arancel = 1800000
valor_matricula = 90000
descuento_arancel = 0
descuento_matricula = 0
valor_final_arancel = 0
valor_final_matricula = 0


promedio_final = float(input("Ingresa el promedio final: (1/7) "))
quintil_socioeconomico = int(input("Ingresa el quintil al que perteneces: (1/5) "))

if (promedio_final > 6) and (quintil_socioeconomico == 1 or quintil_socioeconomico == 2):

    print("recibiste un descuento del 20%")
    valor_final_arancel = valor_arancel * 0.2
    valor_final_arancel = valor_arancel - valor_final_arancel
    print("el valor del arancel es:" , valor_final_arancel )

    valor_final_matricula = valor_matricula * 0.2
    valor_final_matricula = valor_matricula - valor_final_matricula
    print("el valor de la matricula es:" , valor_final_matricula)

