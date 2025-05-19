print("Bienvenid@")

prom_final = float(input("Ingrese su promedio de egreso del liceo: "))
quintil = int(input("Ingrese el quintil al que pertenece su grupo familiar (1, 2, 3, 4 o 5) : "))

aran = 1_800_000
matric = 90_000
desc_aran = ""
desc_matric = ""

if prom_final >= 6.0 and (quintil == 1 or quintil == 2):
    desc_aran = 0.8
    aran_final = aran*desc_aran
    print(f"El valor del arancel es ${aran_final : ,}")
    
elif prom_final >= 6.0 and (quintil == 3 or quintil == 4):
    desc_aran = 0.85
    aran_final = aran*desc_aran
    print(f"El valor del arancel es ${aran_final : ,}")
    
elif 5.0 >= prom_final <= 6.0 and (quintil == 1 or quintil == 2):
    desc_aran = 0.87
    aran_final = aran*desc_aran
    print(f"El valor del arancel es ${aran_final : ,}")
    
elif 5.0 >= prom_final <= 6.0 and (quintil == 3 or quintil == 4):
    desc_aran = 0.9
    aran_final = aran*desc_aran
    print(f"El valor del arancel es ${aran_final : ,}")
    
else:
    print(f"El valor del arancel mantiene el valor original: ${aran : ,}")
    
    
if quintil == 1 or quintil == 2 or quintil == 3:
    desc_matric = 0.1
    if prom_final >= 5.5:
        desc_matric += 0.05
    matric_final = matric*(1 - desc_matric)
    print(f"El valor de su matricula es ${matric_final : ,}")
else:
    print(f"Su matricula mantiene su precio original: ${matric : ,}")