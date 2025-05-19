## Constantes ##
arancel_base=1800000.0
matricula_base=90000.0


print("### Calcule el valor del arancel y de la matricula ###")

## Entrada de datos y filtro ##
promedio=0.0
quintil=0

while promedio>7.0 or promedio<=0 or quintil>5 or quintil<1:
    promedio=float(input("Ingrese el promedio del estudiante: \n"))
    quintil=int(input("Ingrese el quintil socioeconomico(1,2,3,4 o 5): \n"))

## Descuento arancel ##

if promedio>6.0 and quintil<=2:
    arancel_final= arancel_base-(arancel_base*0.2)
elif promedio>6.0 and 3<=quintil<=4:
    arancel_final= arancel_base-(arancel_base*0.15)
elif 5.0<promedio<=6.0 and quintil<=2:
    arancel_final= arancel_base-(arancel_base*0.13)
elif 5.0<promedio<=6.0 and 3<=quintil<=4:
    arancel_final= arancel_base-(arancel_base*0.1)
else:
    arancel_final=arancel_base

## Descuanto Matricula ##

if quintil <= 3:
    matricula_final= matricula_base-(matricula_base*0.1)
    if promedio>=5.5:
        matricula_final-=(matricula_base*0.05)
else:
    matricula_final = matricula_base

## Salida de Datos ##

print(f"Valor final de la matricula es: {matricula_final}")
print(f"Valor final del arancel es: {arancel_final}")
