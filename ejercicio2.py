numero = []
print("---Menu Principal---")
print("1.ingresar un numero")
print("2.numero mayor ")
print("3.numero menor ")
print("4.salir")


def ingresar():
    while True:
        try:    
            numero = int(input("ingrese un numero en el rango de 0 a 100: "))
            if numero >= 0 and numero <= 100:
                print("numero ingresado esta dentro del rango solicitado")
                break
            else:
                print("numero ingresado esta fuera del rango solicitado")
            break
        except:
            print("numero ingresado es incorrecto")
            print("porfavor ingrese un numero valido (numero entero)")
            print("numero ingresado esta fuera del rango solicitado")

def mayor():
    while True:
        try:
            print("el numero mas grande ingresado es:",numero) 
        except:
            print("no se ah ingresado ningun numero")

def salir():
    print("cofirmar que quieres salir")
    print("escribe yes/no ")

    adios = str(input("escriba aqui: "))
    if adios == "yes":
        print("muchas gracias por confirmar")
        print("adios y muchas gracias por ingresar al menu")
    else:
        print("volviendo al menu")
        

opcion = int(input("seleccione una opcion "))
if opcion == 1:
    ingresar()
elif opcion == 2:
     mayor()
        
elif opcion == 4:
    salir()
    break
