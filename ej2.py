
num_may = None
num_prom = []

while True:
    print("Menú principal.")
    print("1.- Ingresar número.")
    print("2.- Mostrar mayor.")
    print("3.- Mostrar promedio.")
    print("4.- Salir.")
    opcion = int(input("Ingrese la opción del menú a la que desea acceder: "))
    break



if opcion == 1:
    while True:
        try:
            num = int(input("Ingrese número: "))
            if 0 <= num <= 100:
                print("Perfecto, número añadido.")
                num_may == num
                break
            else:
                print("Debe ingresar un número entre 0 y 100!")
        except:
            print("Error: Debe ingresar un número entero.")
elif opcion == 2:
    if num_may == None:
        print("No se han ingresado números.")
    else:
        print(f"El número mayor es {num_may}.")