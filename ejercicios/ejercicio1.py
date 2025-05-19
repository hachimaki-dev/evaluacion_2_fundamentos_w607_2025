# Calcular los beneficios económicos otorgados a estudiantes de primer año según sus condiciones académicas y socioeconómicas.
def calculadora_beneficios():
    valorbase_matricula = 850000
    valorbase_arancel = 1500000
    try:
        while True:
            try:
                print("-Bienvenido Usuario-")
                promedio_estudiante = float(input("Ingresa tu promedio final: "))
                nivel_estudiante = int(input("Ingresa el nivel al que perteneces (1-5): "))
                if 0 <= promedio_estudiante <= 7.0 and 1 <= nivel_estudiante <= 5:
                    break
                else:
                    print("Datos incorrectos, intentalo nuevamente")
            except ValueError:
                print("Ingresa un dato valido")
                
        # Aranceles
        descuento_arancel = 0
        if promedio_estudiante > 6.0:
            if nivel_estudiante in[1,2]:
                descuento_arancel = 0.25
            elif nivel_estudiante in[3,4]:
                descuento_arancel = 0.20
            else:
                descuento_arancel = 0.10
        elif promedio_estudiante > 5.0:
            if nivel_estudiante in[1,2]:
                descuento_arancel = 0.15
            elif nivel_estudiante in[3,4]:
                descuento_arancel = 0.10
            else:
                descuento_arancel = 0.05

        # Matricula
        descuento_matricula = 0
        if promedio_estudiante > 5.5:
            descuento_matricula += 0.05
        if nivel_estudiante in[1,2]:
            descuento_matricula += 0.05
        
        # Resultados Finales
        valorfinal_arancel = valorbase_arancel*(1-descuento_arancel)
        valorfinal_matricula = valorbase_matricula*(1-descuento_matricula)
        print("Valor Final del arancel:", valorfinal_arancel)
        print("Valor Final de la matricula:", valorfinal_matricula)
    except ValueError:
        print("Ingresa un dato valido")

calculadora_beneficios()
