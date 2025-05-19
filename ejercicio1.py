print("-----BIENVENIDO-----\nINGRESA LOS DATOS REQUERIDOS")




matricula= 90000
arancel= 18000000
descuento_arancel= 0
descuento_matricula= 0


promedio_usuario= float(input("\nIngrese su promedio (con puntos ej 6.3): "))
while True:
    if promedio_usuario > 7.0:
     promedio_usuario=float(input("Ingrese promedio valido: "))
    else: break




quintil_usuario= int(input("Ingrese el numero de su quintil (1, 2, 3, 4 o 5):"))
while True:
    if quintil_usuario > 5:
       quintil_usuario = int(input("Ingrese un numero valido"))
    else: break




if promedio_usuario > 6.0 and (quintil_usuario == 1 or quintil_usuario == 2):
    descuento_arancel = arancel * 0.80
    print(f"Su descuento es de arancel es 20%\nSu arancel queda en {descuento_arancel:,.0f}$")
elif promedio_usuario > 6.0 and (quintil_usuario == 3 or quintil_usuario == 4):
    descuento_arancel = arancel * 0.85
    print(f"Su descuento es de arancel es 15%\nSu arancel queda en {descuento_arancel:,.0f}$")


if 5.0 < promedio_usuario <= 6.0 and (quintil_usuario == 1 or quintil_usuario == 2):
        descuento_arancel = (arancel) * 0.83
        print(f"Su descuento es de arancel es 13%\nSu arancel queda en {descuento_arancel:,.0f}$")
elif 5.0 < promedio_usuario <= 6.0 and (quintil_usuario == 3 or quintil_usuario == 4):
      descuento_arancel= arancel * 0.90
      print(f"Su descuento es de arancel es 10%\nSu arancel queda en {descuento_arancel:,.0f}$")
else:
   if promedio_usuario <5.0:
      print("No cuenta con descuentos de arancel")
      print(f"Su arancel es de {arancel:,.0f}$")




if promedio_usuario >= 5.5 and (quintil_usuario == 1 or quintil_usuario == 2 or quintil_usuario == 3):
    descuento_matricula = matricula * 0.85
    print(f"Su descuetno de matricula es del 15%\nSu matricula queda en {descuento_matricula: ,.0f}$")
elif quintil_usuario == 1 or quintil_usuario == 2 or quintil_usuario == 3:
    descuento_matricula = matricula * 0.90
    print(f"Su descuetno de matricula es del 10%\nSu matricula queda en {descuento_matricula: ,.0f}$")
else:
    matricula = matricula
    print(f"No cuenta con descuento de matriclula\nSu matricula es de {matricula:,.0f}$")
   
   



