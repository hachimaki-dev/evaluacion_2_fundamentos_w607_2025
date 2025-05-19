promedio = float(input("Ingrese su promedio"))
quintil = int(input("Ingrese su quintil del (1/5):"))

arancel_base = 1800000
matricula_base = 90000

descuento_arancel = 0.0
descuento_matricula = 0.0

if promedio > 6.0:
    if quintil == 1 or quintil ==2:
        descuento_arancel = 0.20
    elif quintil == 3 or quintil ==4:
        descuento_arancel == 0.15
    else:
        descuento_arancel == 0.0


elif promedio > 5.0:
    if quintil == 1 or quintil ==2:
        descuento_arancel == 0.13
    elif quintil == 3 or quintil ==4:
        descuento_arancel ==0.10
    else:
        descuento_arancel == 0.0


    #calcular promedio
if quintil == 1 or quintil ==2 or quintil ==3:
    descuento_matricula == 0.10
    if promedio > 5.5:
        descuento_matricula += 0.05
else:
    descuento_matricula == 0.0
    
    


    

arancel_final = arancel_base * (1- descuento_arancel)
descuento_matricula = matricula_base * (1- descuento_matricula)

#Resultado
print("El arancel final es:", arancel_final)
print("La matricula final es:",matricula_base)
 


