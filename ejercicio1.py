valor_final_arancel = 1800000
arancel_final = 0
valor_final_matricula = 90000

Promedio_final = float(input("Cual es tu promedio final?:"))
quintil_socioeconomico = (input("A que quintil perteneces?:"))
if Promedio_final == (1.0 , 7.0) and quintil_socioeconomico == 5:
 print(f"El valor de la matricula es de {valor_final_matricula} y el de arancel es {valor_final_arancel}")
elif Promedio_final > 5.0 or Promedio_final <=6.0 and quintil_socioeconomico == 3 or quintil_socioeconomico == 4:
 valor_final_arancel *= 0.1
 arancel_final = valor_final_arancel - valor_final_arancel
 print(f"El valor del arancel es {valor_final_arancel} y la matricula es de {valor_final_matricula}")
elif Promedio_final > 5.0 or Promedio_final <= 6.0 and quintil_socioeconomico == 1 or 2:
 valor_final_arancel *= 0.13

 
 
