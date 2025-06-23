lista_juego = []


def guardar_juego(juego_guardar):
    lista_juego.append(guardar)
    print("el juego guardado es", lista_juego)
    

def buscar_juego(juego_buscar):
    for buscar in lista_juego:
        if buscar == lista_juego:
            print("el juego existe")
            break
        else:
            print("el juego no existe")
            break



while True:
    print("--MENU--")
    print("1-guardar juego")
    print("buscar videojuego")
    eleccion = int(input(print("cual opcion eliges:")))

    if eleccion == 1:
        guardar = input(print("cual juego agregaras:"))

    if eleccion == 2:
        buscar = input(print("cual juego buscara:"))


              

