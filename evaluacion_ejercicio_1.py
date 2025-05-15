promedio_estudiante = float(input("cual fue su promedio final en el colegio o liceo: "))
quintil_socioeconomico = int(input("cual es su quintil socioeconomico[1 siendo nivel mayor de vulnerabilidad y 5 el menor]: "))

valor_arancel = 1800000
valor_matricula = 90000

if promedio_estudiante > 6.0 and (quintil_socioeconomico == 1 or quintil_socioeconomico == 2):
    descuento_arancel = valor_arancel * 0.20 
    arancel_final_1 = valor_arancel - descuento_arancel
    print(arancel_final_1)
elif promedio_estudiante > 6.0 and (quintil_socioeconomico == 3 or quintil_socioeconomico == 4):
        descuento_arancel = valor_arancel * 0.15 
        arancel_final_2 = valor_arancel - descuento_arancel
        print(arancel_final_2)
elif promedio_estudiante > 5.0 and promedio_estudiante <= 6.0 and (quintil_socioeconomico == 1 or quintil_socioeconomico == 2):
        descuento_arancel = valor_arancel * 0.13
        arancel_final_2 = valor_arancel - descuento_arancel
        print(arancel_final_2)  
elif promedio_estudiante > 5.0 and promedio_estudiante <= 6.0 and (quintil_socioeconomico == 3 or quintil_socioeconomico == 4):
        descuento_arancel = valor_arancel * 0.10
        arancel_final_2 = valor_arancel - descuento_arancel
        print(arancel_final_2)


else: 
    print("no se aplica ningun descuento de arancel ")
    print(valor_arancel)

if promedio_estudiante >= 5.5 and ( quintil_socioeconomico == 1 or quintil_socioeconomico == 2 or quintil_socioeconomico == 3):
      descuento_matricula = valor_matricula * 0.15 
      valor_final_matricula = valor_matricula - descuento_matricula
      print(valor_final_matricula)
else:
      print("no se aplican descuento a la matricula ")
      print(valor_matricula)