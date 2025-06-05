print ("MENU PRINCIPAL")
print ("1. ingresar el rango")
print ("2.mostrar numero mayor")
print ("3.mostrar promedio")
numero_rango = 0
numero_rango = 100
seleccion = input("seleccione una opcion:")
if seleccion=="1":
    while True:
        numero=int(input("Ingrese número"))
        if 0 <=numero <= 100:
            numero_rango = numero
            print(f"numero ingresado {numero_rango}")
            break
        else:
            print("numero fuera de rango")
elif seleccion=="2":
    if numero_rango == 0:
        print("muestra el numero mayor")
    else: 
        print(f"el numero mayor es {numero_rango}")
elif seleccion=="3":
    if numero_rango == 0:
        print("muestra el promedio")
    else: 
        promedio=numero_rango/2
        print(f"tu promedio es {promedio}")
else:
        print("opcion no valida gracias por usar el programa")



            




        
    





        