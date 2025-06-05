esquema_completo = 0
esquema_incompleto = 0
def vacunas():

    while True:
        global esquema_completo,esquema_incompleto
        try:
            vacunas_recibidas = int(input("cantidad de vacunas recibidas: "))
            break
        except:
            print("ingrese un numero valido(numero entero)")
    if vacunas_recibidas >= 3:
        print("esquema de vacunas completo")
        esquema_completo = esquema_completo + 1
    else:  
        print("esquema de vacunas incompleto")
        esquema_incompleto = esquema_incompleto + 1

while True:
    try:
        numero_de_personas_a_ingresar = int(input("cuantas personas se van a registrar: "))
        break
    except:
        print("ingrese un numero valido(numero entero)")

for i in range(numero_de_personas_a_ingresar):
    vacunas()
print("----resumen final de las personas ingresadas----")
print("se ingresaron",numero_de_personas_a_ingresar,"personas")
print("de las cuales")
print("se ingresaron",esquema_completo,"esquemas completos de vacunas")
print("se ingresaron",esquema_incompleto,"esquemas incompletos de vacunas")

