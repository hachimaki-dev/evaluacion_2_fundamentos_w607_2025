esquemacompleto = 0
esquemaIncompleto = 0

print("----Bienvenido al sistema de vacunas----")
while True:
    try:
        cantidadDepersonas = int(input("Ingrese la cantidad de personas que desea registrar:"))
        break
    except ValueError:
      print ("Error debe escribir un numero entero")

for i in range (cantidadDepersonas):
        print (f"Favor indique cuantas dosis tiene Usuario N" [i+1])
        while True:
            try:
                numeroDeDosis =int(input("Por favor indica la cantidad de dosis recibidas que tiene el usuario : "))
                break
            except ValueError:
             print ("Ha ocurrido un error en captar la informacion")

if numeroDeDosis <= 3:
     esquemacompleto = esquemacompleto + 1
     print ("Numero de dosis completo")
else:  
     esquemaIncompleto = esquemaIncompleto - 1
     print("Numero de dosis incompleto")
 
print("la cantidad de personas con el esque completo de vacunacion es :" (esquemacompleto))
print("la cantidad de personas con esquema incompleto es :" (esquemaIncompleto))
 




