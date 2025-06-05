print ("MENU PRINCIPAL")
print ("1. ingresar un numero")
print ("2.mostrar numero mayor")
print ("3.mostrar promedio")
numero_rango=0 
numero_rango=100
seleccion=input(" Seleccione una opción")

if seleccion == '1':
        print("ingresa el rango del 0 al 100")
        while True:
            try:
                numero = float(input("ingresa el rango"))
            except ValueError:
                print("Ingreso no concluido")
            except ValueError:
                break





        