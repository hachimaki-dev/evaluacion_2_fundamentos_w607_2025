juegos = []

while True:
        print("----MENU---")
        print("1.- Ingresar videojuego.")
        print("2.- Buscar videojuego.")
        print("3.- Eliminar videojuego.")
        print("4.- Salir")
        eleccion = int(input(print("cual numero eliges?")))

        if eleccion is 1:
            def agregar_juegos(guardar_juegos):
                guarda = input(print("cual juego guardara"))
                juegos.append(guarda)
                print("nuevo juego guardado",juegos)

        agregar_juegos(juegos)

        if eleccion is 2:
            def buscar_juego(juego_buscar):
                buscar = input(print("cual juego busca?:"))
                if buscar in juegos:
                    print("el juego si esta")
                else:
                    print("el juego no esta")

        buscar_juego(juegos)

        if eleccion is 3:
            def eliminar_juego(juego_eliminar):
                elimi = input(print("cual juego eliminara?:"))
                juegos.remove(elimi)
                print("el juego eliminado", juegos)

        eliminar_juego(juegos)

        if eleccion is 4:
            break


