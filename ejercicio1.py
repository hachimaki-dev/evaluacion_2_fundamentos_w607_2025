base_arancel = 1800000
base_matricula = 90000

promedio_final = float(input("Cual es tu promedio entre 1.0 y 7.0:"))
quintil = int(input("A cual de los 5 quintiles perteneces?:"))


if quintil == 1 or 2 and promedio_final > 6.0:
    print("papá")
elif quintil == 3 or 4 and promedio_final > 6.0:
    print("weno")








if promedio_final > 5.0 or promedio_final <= 6.0 and quintil == 3 or 4:
    base_arancel = float(base_arancel - (base_arancel * 0.1))
    print(f"Matricula = {base_matricula} y arancel = {base_arancel}")
elif promedio_final > 5.0 or promedio_final <= 6.0 and quintil == 1 or 2:
    base_arancel = float(base_arancel - (base_arancel * 0.13))
    print(f"Matricula = {base_matricula} y arancel = {base_arancel}")
elif promedio_final > 6.0 and quintil == 1 or 2:
    base_arancel = float(base_arancel - (base_arancel * 0.15))
    print(f"Matricula = {base_matricula} y arancel = {base_arancel}")




