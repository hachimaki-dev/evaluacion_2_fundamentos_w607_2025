ingresar_numero = "1-ingresar un numero"
mostrar_mayor = "2-mostrar mayor"
mostrar_promedio = "3-mostrar promedio"
salir = "4-salir"

eleccion = ""
print("1-ingresar un numero")
print("2-mostrar mayor")
print("3-mostrar promedio")
print("4-salir")

while True:
    try:
        eleccion = int(input("elija:"))
        print("1-ingresar un numero")
        print("2-mostrar mayor")
        print("3-mostrar promedio")
        print("4-salir")
        break
    except:
        print("debe ingresar un numero entero")



while True:
    try:
        numero = int(input("ingrese un numero entero:"))
        if 0<= numero>= 100:
            break
        else:
            print("debe ingresar un numero del 0 al 100")
    except:
        print("debe ingresar un numero entero:")
