promedio = 0
quintil = 0
descuento_A = 0
descuento_M = 0
precio_arancel = 1800000
precio_matricula = 90000
precio_A_final = 0
precio_M_final = 0

def arancel (promedio, quintil):
    if promedio > 6.0 and (quintil == 1 or quintil == 2):
        descuento = 0.2
    elif promedio > 6.0 and (quintil == 3 or quintil == 4):
        descuento = 0.15
    elif 5.0 < promedio <= 6.0 and (quintil == 1 or quintil == 2):
        descuento = 0.13
    elif 5.0 < promedio <= 6.0 and (quintil == 3 or quintil == 4):
        descuento = 0.1
    else: 
        descuento = 0
    return descuento

def matricula (promedio, quintil):
    if promedio >= 5.5 and (quintil == 1 or quintil == 2 or quintil == 3):
        descuento_m = 0.15
    elif quintil == 1 or quintil == 2 or quintil == 3 :
        descuento_m = 0.1
    else:
        descuento_m = 0
    return descuento_m

print("Bienvenido a la calculadora de beneficios economicos\nse te solicitara que ingreses tu promedio y quintil recuerda que el promedio se ingresa como decimal")
promedio = float(input("favor ingresar tu promedio: "))
quintil = int(input("favor ingresar tu quintil: "))

descuento_A = arancel (promedio, quintil)
descuento_M = matricula (promedio,quintil)
precio_A_final = precio_arancel - (precio_arancel * descuento_A )
precio_M_final = precio_matricula - (precio_matricula * descuento_M)

print("el precio final de su arancel es: ", precio_A_final)
print("el precio final de su matricula es:  ", precio_M_final)
