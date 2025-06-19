# Lista global para almacenar las reservas
lista_reservas = []

def mostrar_menu():

    print("\n=== SISTEMA DE RESERVAS BLOCKBUSTER ===")
    print("1. Ingresar reserva")
    print("2. Buscar reserva")
    print("3. Eliminar reserva")
    print("4. Mostrar todas las reservas")
    print("5. Salir")

def ingresar_reserva(nombre_cliente):
    print(f"Reserva registrada exitosamente para {nombre_cliente}")
    lista_reservas.append(nombre_cliente)

def buscar_reserva(nombre_cliente):
    for i in lista_reservas:
        if i == nombre_cliente:
            print(f"El cliente {nombre_cliente} tiene una reserva registrada") 
            break
        else:
            print("Este cliente no tiene ninguna reserva a su nombre")


def eliminar_reserva(nombre_cliente):
    if nombre_cliente in lista_reservas:
        lista_reservas.remove(nombre_cliente)
        print(f"Reserva eliminada exitosamente para {nombre_cliente}")
    else:
        print(f"No se encontró reserva para {nombre_cliente}")


def mostrar_reservas():
    print(lista_reservas)
    print("Total reservas:",len(lista_reservas))


def main():

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            
            if opcion == 1:
                nombre = input("Ingrese el nombre del cliente: ").strip().title()
                ingresar_reserva(nombre)
            elif opcion == 2:
                nombre = input("Ingrese el nombre a buscar: ").strip().title()
                buscar_reserva(nombre)
            elif opcion == 3:
                nombre = input("Ingrese el nombre a eliminar: ").strip().title()
                eliminar_reserva(nombre)
            elif opcion == 4:
                mostrar_reservas()
            elif opcion == 5:
                print("Programa terminado. Gracias por usar el sistema de Blockbuster")
                break
            else:
                print("Opción inválida. Ingrese un número entre 1 y 5")
        except ValueError:
            print("Error: Debe ingresar un número válido")

if __name__ == "__main__":
    main()