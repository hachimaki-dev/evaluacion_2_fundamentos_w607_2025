uno = "1-ingresar un numero"
dos= "2-mostrar mayor"
tres= "3-mostrar promedio"
cuatro = "4-salir"

eleccion = ""
print("1-ingresar un numero")
print("2-mostrar mayor")
print("3-mostrar promedio")
print("4-salir")

while True:
    try:
        eleccion = int(input("elija:"))
        break
    except:
        print("debe ingresar un numero entero")

if eleccion == uno:
    print("hola")