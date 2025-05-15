
#Desarrollar un programa en **Python** que calcule los **beneficios económicos** otorgados a estudiantes de primer año según sus condiciones **académicas** y **socioeconómicas**.
#* Valor **base del arancel**: `$1.800.000`
#* Valor **base de la matrícula**: `$90.000`


#definimos las variables necesarias
promedio = 0
quintil = 0
descuentoArancel = 0.0
descuentoMatricula = 0.0
arancel = 1800000
matricula = 90000
valorFinalMatricula = 0
valorFinalArancel = 0
print("Bienvenido a la calculadora de beneficios socioeconomicos")

print("*************************************************************")

#hacemos que el usuario ingrese su nota
promedio = float(input("Ingrese su nota final: "))

print("*************************************************************")


#creamos un menú para que el usuario ingrese el quintil 
print("*************************************************************")
print("1. Quintil 1")
print("2. Quintil 2")
print("3. Quintil 3")
print("4. Quintil 4")
print("5. Quintil 5")

#hacemos que el usuario ingrese el quintil al que pertenece
quintil = int(input("Ingrese el quintil al que pertenece: "))



if promedio > 6.0 and (quintil == 1 or quintil == 2):
    descuentoArancel = 0.2
    print(f"Tienes un 20% de descuento")
elif promedio > 6.0 and (quintil == 3 or quintil == 4 ):
    descuentoArancel = 0.15
    print(f"Tienes un 15% de descuento")
elif (promedio > 5.0 and promedio <= 6.0) and (quintil == 1 or quintil == 2):
    descuentoArancel = 0.13
    print(f"Tienes un 13% de descuento")
elif (promedio > 5.0 and promedio <= 6.0) and (quintil == 3 or quintil == 4):
    descuentoArancel = 0.1
    promedio(f"Tienes un 10% de descuento ")
else:
    print("No existe ese quintil")
    print("No tienes ningun descuento")


if (quintil == 1 or quintil == 2 or quintil == 3):
    descuentoMatricula += 0.1
    matricula 
    print(f"Felicidades, tienes un 10% de descuento adicional")

print("*************************************************************")

if promedio >= 5.5:
    descuentoMatricula += 0.05
    print(f"Felicidades, por tu desempeño tambien tienes un 5% de descuento adicional")

print("*************************************************************")

valorFinalMatricula = matricula - (matricula * descuentoMatricula)
valorFinalArancel = arancel - (arancel * descuentoArancel)
print("Segun mis calculos, tu descuento final del arancel y la matricula es: ")
print("Descuento de arancel: ", valorFinalArancel)
print("Descuento de matricula: ", valorFinalMatricula)








