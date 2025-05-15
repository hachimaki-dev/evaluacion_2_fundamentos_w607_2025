promedio = float(input("Ingrese el promedio final del estudiante: \n"))
quintil = int(input("Ingrese en que quintil esta (1, 2, 3, 4, 5): \n"))
arancel = 1800000
matricula = 90000

if promedio >= 6 and quintil == 1 or 2:
    arancel = arancel - arancel * 0.20
    print(f"El valor del arancel es: {arancel}$")

    if quintil == 1 or 2 or 3:
        matricula = matricula - matricula * 0.10
        print(f"El valor de la matricula es: {matricula} ")
    elif quintil == 1 or 2 or 3 and promedio > 5.5:
        matricula = matricula - matricula * 0.15
        print(f"El valor de la matricula es {matricula}")
    else:
        print(f"El valor de la matricula es {matricula}")

if promedio >= 6 and quintil == 3 or 4:
    arancel = arancel - arancel * 0.15
    print(f"El valor del arancel es: {arancel}$")

    if quintil == 1 or 2 or 3:
        matricula = matricula - matricula * 0.10
        print(f"El valor de la matricula es: {matricula} ")
    elif quintil == 1 or 2 or 3 and promedio > 5.5:
        matricula = matricula - matricula * 0.15
        print(f"El valor de la matricula es {matricula}")
    else:
        print(f"El valor de la matricula es {matricula}")

if promedio > 5 and promedio >= 6 and quintil == 1 or 2:
    arancel = arancel - arancel * 0.13
    print(f"El valor del arancel es: {arancel}$")

    if quintil == 1 or 2 or 3:
        matricula = matricula - matricula * 0.10
        print(f"El valor de la matricula es: {matricula} ")
    elif quintil == 1 or 2 or 3 and promedio > 5.5:
        matricula = matricula - matricula * 0.15
        print(f"El valor de la matricula es {matricula}")
    else:
        print(f"El valor de la matricula es {matricula}")

if promedio > 5 and promedio >= 6 and quintil == 3 or 4:
    arancel = arancel - arancel * 0.10
    print(f"El valor del arancel es: {arancel}$")

    if quintil == 1 or 2 or 3:
        matricula = matricula - matricula * 0.10
        print(f"El valor de la matricula es: {matricula} ")
    elif quintil == 1 or 2 or 3 and promedio > 5.5:
        matricula = matricula - matricula * 0.15
        print(f"El valor de la matricula es {matricula}")
    else:
        print(f"El valor de la matricula es {matricula}")

if promedio < 5 and quintil == 5:
    print(f"El valor de la matricula es {matricula}")
    print(f"El valor del arancel es {arancel}")
else:
    print(f"El valor de la matricula es {matricula}")
    print(f"El valor del arancel es {arancel}")
