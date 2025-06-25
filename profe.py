lista_de_juegos = []

def ingresar_juego(juego_recibido):
    print(juego_recibido)
    lista_de_juegos.append(juego)
    return

def buscar_juego(juego_a_buscar):
     for juegos in lista_de_juegos:
         if juego_a_buscar == juegos:
             print("El juego existe")
             break
         else:
            print("Juego no existe")
            break

def eliminar_juego(juego_eliminar):
    print(juego_eliminar)
    lista_de_juegos.remove(juego_eliminar)
    return



while True:
    print("---MENU---")
    print("1- ingresar videojuego")
    print("2-buscar videojuego")
    print("3-eliminar videojuego")
    print("4-salir")
    opcion = int(input("Ingrese opcion"))
    if opcion == 1:
        juego = input("Cual es el juego?")
        ingresar_juego(juego)
    
    if opcion == 2:
        juego_a_buscar = input("Cual es el juego a buscar?")
        buscar_juego(juego_a_buscar)

    if opcion == 3:
        juego_eliminar=input(print("cual juego eliminara"))
        eliminar_juego(juego_eliminar)
