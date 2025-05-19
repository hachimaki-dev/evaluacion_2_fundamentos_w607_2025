while True:
    promedio_final= float(input("ingrese el promedio final del estudiante\n "))
    quintil= int(input("cual es su quintil socioeconomico:1, 2, 3, 4, 5\n"))
    if promedio_final <= 7 and quintil <= 5:
        break
    else:
        print("escriba un promedio o quintil valido\n")

valor_arancel = 1800000
valor_matricula = 90000

if promedio_final > 6 and quintil == 1 or quintil== 2:
    
    valor_arancel= valor_arancel*0.80

elif promedio_final > 6 and quintil == 3 or quintil== 4:
    
    valor_arancel= valor_arancel*0.85

elif promedio_final > 5 and promedio_final <=6 and quintil == 1 or quintil== 2:
    
    valor_arancel= valor_arancel*0.87

elif promedio_final > 5 and promedio_final <=6 and quintil == 1 or quintil== 2:
    
    valor_arancel= valor_arancel*0.90

else: 
    print("no se han aplicado descuentos al arancel")

if quintil== 1 or quintil== 2 or quintil== 3 and promedio_final>= 5.5:    
    valor_matricula= valor_matricula*0.85

elif quintil== 1 or quintil== 2 or quintil== 3:
    valor_matricula= valor_matricula*0.90


else: print("no recibio descuento de matricula")

print("el valor del aracel es:" , valor_arancel)
print("el valor de la matricula es:" , valor_matricula)