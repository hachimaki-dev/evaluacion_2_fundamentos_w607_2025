def quintiles():
# Valor de las variables de arancel, matricula y descuentos
    valor_de_arancel= 1800000
    valor_de_matricula = 90000

    descuento_arancel = 0
    descuento_matricula = 0


 # Recibir los datos de entrada
    promedio = float(input("Ingrese el promedio de notas de su enseñanza media: "))
    quintil = int(input("Ingrese el quintil al que pertence (1, 2, 3, 4 o 5): "))

# Calcular los quintiles del 1 al 5 
    if quintil < 1 or quintil > 5:
        print("Ingresa un número entre el 1 y el 5")
        
        if promedio > 6.0:
            if quintil in [1, 2]:
                descuento_arancel = 0.20
        elif promedio > 6.0:
            if quintil in [3, 4]:
                descuento_arancel = 0.15
        elif promedio >= 5.0 <= 6.0:
            if quintil in [1, 2]:
                descuento_arancel = 0.13
        elif promedio >= 5.0 <= 6.0:
            if quintil in [3, 4]:
                descuento_arancel = 0.10
    else:
        print("Los valores de tu arancel y matricula son:") 

# Aplicar el descuento al arancel para sacar el resultado final
    valor_arancel_final = int(valor_de_arancel - (valor_de_arancel * descuento_arancel))

# Calcular el descuento de matrícula

    if quintil in [1, 2, 3]:
        descuento_matricula += 0.10
        if promedio >= 5.5:
            descuento_matricula += 0.05

# Aplicar el descuento a la matricula para sacar el resultado final

    valor_matricula_final = int(valor_de_matricula - (valor_de_matricula * descuento_matricula))

    print(f"El valor del arancel es: ${valor_arancel_final}")
    print(f"El valor de la matrícula es: ${valor_matricula_final}")

quintiles()