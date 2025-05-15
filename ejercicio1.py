promedioFinal = float(input("Ingrese el promedio final con el que salió del colegio/Liceo: "))
quintilSocioeconomico = int(input("Ingrese el Quintil al que pertenece (1-5): "))

valorFinalArancel = 1800000
valorFinalMatricula = 90000

# mayor  a 6 quintil 1 o 2  20% desc
# mayor a 6 quintil 3 o 4 15%
#  5 > <= 6 Quntil 1 o 2  13%
#  ""    3 o 4 10%
# cualquier promedio  quintil 5 o promedio 5 o menos  0% descuento

if promedioFinal > 6 and (quintilSocioeconomico == 1 or quintilSocioeconomico == 2) :
    print("¡usted obtiene un descuento del 20%!")
    valorFinalArancel = valorFinalArancel * 0.8    

elif promedioFinal > 6 and (quintilSocioeconomico == 3 or quintilSocioeconomico == 4):
    print("¡usted obtiene un descuento del 15%!")
    valorFinalArancel = valorFinalArancel * 0.85

elif 5 < promedioFinal >= 6 and (quintilSocioeconomico == 1 or quintilSocioeconomico == 2):
    print("¡Usted obtiene un descuento del 13%") 
    valorFinalArancel = valorFinalArancel * 0.87

elif 5 < promedioFinal >= 6 and (quintilSocioeconomico == 3 or quintilSocioeconomico == 4):
    print("¡Usted obtiene un descuento del 10%")
    valorFinalArancel = valorFinalArancel * 0.9

elif 1 < promedioFinal <= 7 and (quintilSocioeconomico == 5 or promedioFinal <= 5 ):
    print("usted no obtiene descuento")



if (quintilSocioeconomico == 1 or quintilSocioeconomico == 2 or quintilSocioeconomico == 3) and (promedioFinal >= 5.5):
    print("Usted por pertenecer a los 3 primeros quintiles recibirá un descuento en la matricula del 10%")
    print("Además, usted recibirá un 5% de descuento adicional por tener un promedio mayor o igual a 5.5")
    valorFinalMatricula = valorFinalMatricula * 0.85

print("EL precio final del arancel es de: $", valorFinalArancel)
print("El precio final de la matricula es de: $", valorFinalMatricula)
