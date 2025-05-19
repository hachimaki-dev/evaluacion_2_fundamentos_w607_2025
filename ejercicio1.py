#incializar variables
promediofinal = 0
quintil = 0
valor_arancel = 1800000
valor_matricula = 90000
descuento_arancel = 0
descuento_matricula = 0


#entradas
promediofinal = float(input("ingrese su promedio final : "))
quintil = int(input("Ingrese el numero de quintil socio econmico que pertenece (1,2,3,4,5) : "))

#Descuento en arancel 

if promediofinal > 6.0 and (quintil == 1 or quintil == 2):
     descuento_arancel =  0.20
     print ("Tienes un descuento del 20 % en arancel")
elif promediofinal > 6.0 and (quintil == 3 or quintil == 4):
    descuento_arancel =  0.15
    print ("Tienes un descuento del 15 % en arancel")
elif promediofinal > 5.0  and promediofinal <= 6.0 and (quintil == 3 or  quintil == 5 ):
     descuento_arancel = 0.10
     print ( "Tienes un descuento del 10% en arancel")
else :
     print ( "No tienes descuento")

#Descuento en matricula

if (quintil == 1 or quintil == 2 or quintil == 3) :
    descuento_matricula = 0.10
    print("Tienes un descuento de 10% en matricula gracias a tu quintil ")
    if promediofinal >= 5.5:
     descuento_matricula = 0.15
     print("Tienes un descuento adicional del 5% por tu buen promedio")

#Calculo final

valor_arancel = valor_arancel - (valor_arancel * descuento_arancel)
valor_matricula = valor_matricula - (valor_matricula * descuento_matricula)

#Se entrega el resultado
print("El valor de tu arancel es :" ,round(valor_arancel))
print("El valor de la matricula es:",round(valor_matricula))