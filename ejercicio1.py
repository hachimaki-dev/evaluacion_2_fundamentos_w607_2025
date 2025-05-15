promedio_final= float(input("ingrese el promedio final del estudante "))
quintil= int(input("cual es su quintil socioeconomico:1, 2, 3, 4, 5 "))

if promedio_final >= 6 and quintil == 1 or quintil== 2:
    
    valor_arancel= 1800000*0.80
    print("el valor del arancel es:", valor_arancel)

elif promedio_final >= 6 and quintil == 3 or quintil== 4:
    
    valor_arancel= 1800000*0.85
    print("el valor del arancel es:", valor_arancel)

elif promedio_final >= 5 and promedio_final <=6 and quintil == 1 or quintil== 2:
    
    valor_arancel= 1800000*0.87
    print("el valor del arancel es:", valor_arancel)
