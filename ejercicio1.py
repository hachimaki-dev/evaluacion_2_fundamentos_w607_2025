print("Bienvenid@")

prom_final = float(input("Ingrese su promedio de egreso del liceo: "))
quintil = int(input("Ingrese el quintil al que pertenece su grupo familiar (1, 2, 3, 4 o 5: "))

aran = 1800000
matric = 90000
desc_aran = ""
desc_matric = ""

if prom_final >= 6.0:
    if quintil == 1 or 2:
        desc_aran = 0.8
        desc_matric = 0.85
        aran_final = aran * desc_aran
        matric_final = matric * desc_matric
       
    
        print(f"El valor final de su arancel será ${aran_final}")
        print(f"El valor final de su matrícula será ${matric_final}")
    elif quintil == 3:
        desc_aran = 0.85
        desc_matric = 0.85
        aran_final = aran * desc_aran
        matric_final = matric * desc_matric
        
        print(f"El valor final de su arancel será ${aran_final}")
        print(f"El valor final de su matrícula será ${matric_final}")
elif prom_final >= 6.0 and quintil == 4:
    desc_aran = 0.85
    aran_final = aran * desc_aran
    
    print(f"El valor final de su arancel será ${aran_final}")
    print(f"El valor de su matricula es ${matric}")

elif  5.0 >= prom_final <= 6.0:
    if quintil == 1 or 2:
        desc_aran = 0.87
        desc_matric = 0.85
        aran_final = aran * desc_aran
        matric_final = matric * desc_matric
       
    
        print(f"El valor final de su arancel será ${aran_final}")
        print(f"El valor final de su matrícula será ${matric_final}")
    elif quintil == 3:
        desc_aran = 0.9
        desc_matric = 0.85
        aran_final = aran * desc_aran
        matric_final = matric * desc_matric
        
        print(f"El valor final de su arancel será ${aran_final}")
        print(f"El valor final de su matrícula será ${matric_final}")
else:
    print(f"El valor de su arancel es ${aran}")
    print(f"El valor de su matrícula es ${matric}")