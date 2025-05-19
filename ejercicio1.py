total_aracel = 1800000
matricula = 90000

print("-------menu-------")
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
    calcular_aracel = total_aracel * 0.80
    print("tiene un descuento en el aracel del 20%")
    print("el valor del arancel original es de: ",total_aracel)
    print("el valor del arancel con descuento es: ", calcular_aracel) 

elif prom > 6 and (quintil == 3 or quintil == 4):
    calcular_aracel = total_aracel * 0.85
    print("tiene un descuento en el aracel del 15%")
    print("el valor del arancel original es de: ",total_aracel)
    print("el valor del arancel con descuento es", calcular_aracel) 

elif prom > 5  and prom <= 6 and (quintil == 1 or quintil == 2):
    calcular_aracel = total_aracel * 0.87
    print("tiene un descuento en el aracel del 13%")
    print("el valor del arancel original es de: ",total_aracel)
    print("el valor del arancel con descuento es", calcular_aracel) 

elif prom > 5  and prom <= 6  and (quintil == 3 or quintil == 4):
    calcular_aracel = total_aracel * 0.90
    print("tiene un descuento en el aracel del 10%")
    print("el valor del arancel original es de: ",total_aracel)
    print("el valor del arancel con descuento es", calcular_aracel) 

elif prom >= 1  and prom <= 5  and (quintil == 5):
    print("no tienes descuento en el aracel")
    print("el valor del arancel original es de: ",total_aracel)
else:
    print("tu promedio es muy bajo optar al descuento en el arancel")
    print("el valor del arancel original es de: ",total_aracel)

if (quintil == 1 or quintil == 2 or quintil == 3) and (prom >= 5.5):
    descuento = matricula * 0.85
    print("ademas por tu desempeño mayor a 5.5 tienes un 5% mas de descuento en la matricula")
    print("tienes un descuento total de 15%")
    print("el valor original de la matricula es", matricula)
    print("el valor de la matricula con descuento es", descuento)
elif (quintil == 1 or quintil == 2 or quintil == 3):
        descuento = matricula * 0.90
        print("tienes un descuento del 10% por pertenecer a uno de los quintiles 1 2 o 3")
        print("el valor original de la matricula es de:", matricula)
        print("el valor de la matricula con descuento es:", descuento)
else:
    print("no tienes descuento de matricula")
    print("el valor original de la matricula es:", matricula)
