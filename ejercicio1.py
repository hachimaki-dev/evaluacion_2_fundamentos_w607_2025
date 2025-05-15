print("-----BIENVENIDO-----\nINGRESA LOS DATOS REQUERIDOS")
print





matricula= 90000
arancel= 18000000
descuento_arancel= 0
descuento_matricula= 0




promedio_usuario= int(input("\nIngrese su promedio (sin puntos): "))
while True:
    if promedio_usuario > 70:
     promedio_usuario=int(input("Ingrese promedio valido: "))
    else: break


quintil_usuario= int(input("Ingrese el numero de su quintil (1, 2, 3, 4 o 5):"))
while True:
    if quintil_usuario > 5:
       quintil_usuario = int(input("Ingrese un numero valido"))
    else: break



if promedio_usuario > 60 and quintil_usuario == 1 or 2:
   descuento_arancel = (arancel) * 20/100
   descuento= print(f"Su descuento es de arancel es 20%\nSu arancel queda en {descuento_arancel + arancel}$")
elif promedio_usuario > 60 and quintil_usuario == 3 or 4: 
   descuento_arancel = descuento_arancel = (arancel) * 15/100
   descuento= print(f"Su descuento es de arancel es 15%\nSu arancel queda en {descuento_arancel}$")
elif promedio_usuario <= 60 or promedio_usuario == 50 and quintil_usuario == 1 or 2:
   descuento_arancel = (arancel) *  13/100
   descuento= print(f"Su descuento es de arancel es 13%\nSu arancel queda en {descuento_arancel}$")
elif promedio_usuario <= 60 or promedio_usuario == 50 and quintil_usuario == 3 or 4:
   descuento_arancel = (arancel) *  10/100
   descuento= print(f"Su descuento es de arancel es 10%\nSu arancel queda en {descuento_arancel}$")
elif promedio_usuario < 50 or quintil_usuario == 5:
   print("No cuenta con descuentos")

   
   



