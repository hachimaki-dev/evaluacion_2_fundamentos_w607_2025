def calcular_beneficios():
    # Precios base
    arancel = 1800000
    matricula = 90000

    # Entrada de datos
    promedio = float(input("Promedio: "))
    quintil = int(input("Quintil (1 a 5): "))

    # Descuento en arancel
    if promedio > 6.0:
        if quintil in [1, 2]:
            desc_arancel = 0.20
        elif quintil in [3, 4]:
            desc_arancel = 0.15
        else:
            desc_arancel = 0
    elif promedio > 5.0:
        if quintil in [1, 2]:
            desc_arancel = 0.13
        elif quintil in [3, 4]:
            desc_arancel = 0.10
        else:
            desc_arancel = 0
    else:
        desc_arancel = 0

    # Descuento en matrícula
    desc_matricula = 0.10 if quintil in [1, 2, 3] else 0
    if promedio >= 5.5 and quintil in [1, 2, 3]:
        desc_matricula += 0.05

    # Cálculo final
    total_arancel = arancel * (1 - desc_arancel)
    total_matricula = matricula * (1 - desc_matricula)

    # Mostrar resultados
    print(f"\nArancel final: ${int(total_arancel):,}".replace(",", "."))
    print(f"Matrícula final: ${int(total_matricula):,}".replace(",", "."))


calcular_beneficios()

            
print ("felicidades por tu beneficio asignado")

#profe lo siento mucho por haber copiado, le juro q estoy aprendiendo, ya sabiendo 
# que no nos restara puntaje por hacernos los vivos, yo luche harto por hacer mi codigo 
# pero paso a pasito, hay otras asignaturas donde me va mucho mejor, por esta vez 
#necesito la notita :[
