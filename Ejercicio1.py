promedio_final = float(input("Ingrese su promedio final de enseñanza media: "))
quintil = int(input("Ingrese el quintil socioeconómico al que pertenece (1, 2, 3, 4 y 5): "))

valor_arancel = 1800000
valor_matricula = 90000
descuento_total = 0
descuento_total_M = 0

if promedio_final > 6.0 and (quintil == 1 or quintil == 2):
    descuento_total = valor_arancel - (valor_arancel * 0.2)
elif promedio_final > 6.0 and (quintil == 3 or quintil == 4):
    descuento_total = valor_arancel - (valor_arancel * 0.15)
elif (promedio_final > 5.0 and promedio_final <= 6.0) and (quintil == 1 or quintil == 2):
    descuento_total = valor_arancel - (valor_arancel * 0.13)
elif (promedio_final > 5.0 and promedio_final <= 6.0) and (quintil == 3 or quintil == 4):
    descuento_total = valor_arancel - (valor_arancel * 0.1)
elif promedio_final <= 5.0 or (quintil == 5):
    descuento_total = valor_arancel  

if (quintil == 1 or quintil == 2 or quintil == 3) and promedio_final >= 5.5:
    descuento_total_M = valor_matricula - (valor_matricula * 0.15)
elif quintil == 1 or quintil == 2 or quintil == 3:
    descuento_total_M = valor_matricula - (valor_matricula * 0.1)
else:
    descuento_total_M = valor_matricula  

print(f"Su descuento de arancel es: {descuento_total}")
print(f"Su descuento total de la matrícula es: {descuento_total_M}")


    
    
    
    
    
    

