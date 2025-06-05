import time
def menu():
    global opcion_usuario
    print("---Bienvenido---")
    print("1.INGRESAR NUMEROS")
    print("2.MOSTRAR NUMERO MAYOR")
    print("3.MOSTRAR PROMEDIO")
    print("4.SALIR")
    opcion_usuario= int(input("INGRSE OPCION: "))

num1= None
num2= None
def opcion1():
    global num1, num2
    while True:
        try:
            num1 = int(input("INGRESE EL PRIEMER NUMERO (DEL 0 AL 100): "))
            if 0 <= num1 <= 100:
                print("NUMERO VALIDO")
                break
            elif 0 < num1 > 100:
                print("ingrese numero valido")
            else:
                num1 == num2
                print("Los numeros son iguales ")
        except ValueError:
            print("INGRESE UN NUMERO EMTERO VALIDO")
    while True:
        try:
            num2 = int(input("INGRESE EL SEGUNDO NUMERO (DEL 0 AL 100): "))
            if 0 <= num2 <= 100:
                print("NUMERO VALIDO")
                opcion_menu()
                break
            elif 0 < num2> 100:
                print("ingrese numero valido")
            else:
                num1 == num2
                print("Los numeros son iguales ")
        except ValueError:
            print("INGRESE UN NUMERO EMTERO VALIDO")

def opcion2():
    global num1, num2
    if num1 is None or num2 is None:
        print("NO HAY DATOS SUFICIENTES PARA ANALIZAR")
    elif num1 > num2:
        print("EL NUMERO MAS GRANDE ES: ", num1)
    elif num1 < num2:
        print("EL NUMERO MAS GRANDE ES: ", num2)


promedio = None
def opcion3():
    global promedio
    promedio= (num1 + num2 ) / 2 
    print("EL PROMEDIO ES: ", promedio)



def opcion_menu():
    global opcion_usuario
    menu() == opcion_usuario
    while True:
        try:
            if opcion_usuario == 1:
                opcion1()
                break
            elif opcion_usuario == 2:
                opcion2()
                break
            elif opcion_usuario == 3:
                opcion3()
                break
            elif opcion_usuario == 4:
                time.sleep(2)
                break
            elif opcion_usuario > 4:
                print("INGRSE OPCION VALIDA")
                opcion_menu()
        except ValueError:
            print("INGRESE UN NUMERO ENTERO VALIDA")

opcion_menu()
        
    
