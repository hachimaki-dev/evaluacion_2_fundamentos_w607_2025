valor_arancel = 1800000
valor_matricula = 90000
descuento_total = 0
descuento_matricula = 0

promedio = float(input("Cual es su promedio: ")) 

Quintil = int(input("Cual es el Quintil al que pertenece: ")) 

if promedio > 6.0 and (Quintil == 1 or Quintil ==2):
  descuento_total = valor_arancel - (valor_arancel * 0.2)
elif promedio > 6.0 and (Quintil == 3 or Quintil ==4):
  descuento_total = valor_arancel - (valor_arancel * 0.15)
elif promedio > 5.0 and promedio <= 6.0 and (Quintil == 1 or Quintil ==2):
  descuento_total = valor_arancel - (valor_arancel * 0.13)
elif promedio > 5.0 and promedio <= 6.0 and (Quintil == 3 or Quintil ==4):
  descuento_total = valor_arancel - (valor_arancel * 0.1)
elif promedio <= 5.0 or (Quintil == 5):
  descuento_total = valor_arancel 

if Quintil == 1 or Quintil == 2 or Quintil == 3 and promedio >= 5.5:
  descuento_matricula = valor_matricula - (valor_matricula * 0.15)
elif Quintil == 1 or Quintil == 2 or Quintil == 3:
  descuento_matricula = valor_matricula - (valor_matricula * 0.1)
else:
  descuento_matricula = valor_matricula

print(f"el valor del arancel es {descuento_total}")
print(f"el valor de la matricula es {descuento_matricula}")