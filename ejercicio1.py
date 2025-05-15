aracel = 0
total_aracel = 1800000
matricula = 90000

print("---menu---")
print("1- primer quintil")
print("2- segundo quintil")
print("3- tercer quintil")
print("4- cuarto quintil")
print("5- quinto quintil")
quintil = 0

while quintil < 1 or  quintil > 5:
    try:
        quintil = int(input("ingrese al quintil que pertenece: "))
    except ValueError:
        print("error 1: porfavor ingrese solo numero enteros")



prom = float(input("ingrese su promedio con el que egresaste de el colegio: "))
while prom < 1 or prom > 7:
    prom = float(input("ingrese un promedio valido: "))

if prom > 6 and (quintil == 1 or quintil == 2):
    aracel = 20
    calcular_aracel = total_aracel * 0.20
    aracel_f = total_aracel - calcular_aracel

    print("tiene un aracel del:", aracel,"%")
    print("el valor del arancel con descuento es", aracel_f) 

elif prom > 6 and (quintil == 3 or quintil == 4):
    aracel = 15
    print("tiene un aracel del:", aracel,"%")

elif prom > 5  and prom <= 6 and (quintil == 1 or quintil == 2):
    aracel = 13
    print("tiene un aracel del:", aracel,"%") 

elif prom > 5  and prom <= 6  and (quintil == 3 or quintil == 4):
    aracel = 10
    print("tiene un aracel del:", aracel,"%")

elif prom >= 1  and prom <= 5  and (quintil == 5):
    aracel = 0
    print("tiene un aracel del:", aracel,"%")
else:
    print("tu promedio es muy bajo para optar al arancel")


if quintil == 1 or quintil == 2 or quintil == 3:
    descuento = 10
    print("-tienes un descuento en la matricula por pertenecer a uno de los quitiles 1 2 o 3 del ",descuento,"%")
    if prom >= 5.5:
        descuento = 10 + 5
        print("ademas por tu desenpeño mayor a 5.5 tienes un 5% mas de descuento en la matricula")
        print("-tienes un descuento total del: ",descuento,"%")


    




