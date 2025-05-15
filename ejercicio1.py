promedio = float(input("Ingresa el promedio:"))
decil = int(input("Ingresa el decil (1-10):"))

if promedio>=6:
    if decil in [1,2,3]:
        arancel=100000
        matricula=900000
        porcentajedescuento=20
    else:
        arancel=2000000
        matricula=900000
        porcentajedescuento=20

    descuento_arancel=arancel * (porcentajedescuento /100)
    descuento_matricula=matricula * (porcentajedescuento /100)

    valor_arancel_final=arancel - descuento_arancel
    valor_matricula_final=matricula - descuento_matricula

    print(f"El valor de tu arancel con descuento es: ${valor_arancel_final}")
    print(f"El valor de tu matrícula con descuento es: ${valor_matricula_final}")
else:
    print("No cumples con el requisito del promedio para obtener el descuento.")



