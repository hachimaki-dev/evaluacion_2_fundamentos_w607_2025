# Calcular los beneficios económicos otorgados a estudiantes de primer año según sus condiciones académicas y socioeconómicas.
valorbase_arancel = 1800000
valorbase_matricula = 90000
promedio_final = float(input("Ingresa el promedio final con el que egresaste del colegio o liceo: "))
quintil_estudiante = int(input("Ingresa el quintil socioeconómico al que pertenece tu grupo familiar: "))

if promedio_final > 6.0:
    if quintil_estudiante in[1,2]:
            print("El valor del arancel es: ", valorbase_arancel*0.8)
            print("El valor de la matricula es: ", valorbase_matricula*0.85)
    elif quintil_estudiante == 3:
            print("El valor del arancel es: ", valorbase_arancel*0.85)
            print("El valor de la matricula es: ", valorbase_matricula*0.85)
    else:
            print("El valor del arancel es: ", valorbase_arancel*0.8)
            print("El valor de la matricula es: ", valorbase_matricula)
elif 5.0 < promedio_final <= 6.0:
    if promedio_final >= 5.5:
        if quintil_estudiante in[1,2]:
                print("El valor del arancel es: ", valorbase_arancel*0.87)
                print("El valor de la matricula es: ", valorbase_matricula*0.85)
        elif quintil_estudiante == 3:
                print("El valor del arancel es: ", valorbase_arancel*0.9)
                print("El valor de la matricula es: ", valorbase_matricula*0.85)
        else:
                print("El valor del arancel es: ", valorbase_arancel*0.9)
                print("El valor de la matricula es: ", valorbase_matricula)
    else:
        if quintil_estudiante in[1,2]:
                print("El valor del arancel es: ", valorbase_arancel*0.87)
                print("El valor de la matricula es: ", valorbase_matricula*0.9)
        elif quintil_estudiante == 3:
                print("El valor del arancel es: ", valorbase_arancel*0.9)
                print("El valor de la matricula es: ", valorbase_matricula*0.9)
        else:
                print("El valor del arancel es: ", valorbase_arancel*0.9)
                print("El valor de la matricula es: ", valorbase_matricula)
else:
    print("El valor del arancel es: ", valorbase_arancel)
    print("El valor de la matricula es: ", valorbase_matricula)