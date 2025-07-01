
vehiculos = {
    'TOY8475': ['Toyota', 2019, '65000km', 'Gasolina', 'Automática', '1.8L 4cil', 'Blanco'],
    'FOR2175': ['Ford', 2017, '85000km', 'Gasolina', 'Manual', '1.6L 4cil', 'Azul'],
    'CHE9834': ['Chevrolet', 2020, '25000km', 'Gasolina', 'Automática', '2.0L 4cil', 'Negro'],
    'NIS7654': ['Nissan', 2016, '95000km', 'Gasolina', 'Manual', '1.6L 4cil', 'Rojo'],
    'HYU4521': ['Hyundai', 2021, '15000km', 'Híbrido', 'Automática', '1.6L 4cil', 'Gris'],
    'KIA3456': ['Kia', 2018, '75000km', 'Diesel', 'Manual', '2.0L 4cil', 'Blanco'],
    'MAZ8901': ['Mazda', 2019, '55000km', 'Gasolina', 'Automática', '2.5L 4cil', 'Rojo'],
    'SUB2468': ['Subaru', 2020, '30000km', 'Gasolina', 'Manual', '2.0L 4cil', 'Verde'],
    # ... más vehículos
}

inventario = {
    'TOY8475': [8500000, 1], 
    'FOR2175': [6200000, 1], 
    'CHE9834': [12750000, 1],
    'NIS7654': [5400000, 2], 
    'HYU4521': [15200000, 1], 
    'KIA3456': [7800000, 1],
    'MAZ8901': [9200000, 1], 
    'SUB2468': [11500000, 0], 
    'HON1357': [6800000, 0],
    # ... más vehículos
}

def buscr(vehiculos,buscar):
    return print(vehiculos[buscar])

def rango():
    busqueda_precio=(precio_min, precio_max)
    return

def modificar():
    return

def sal():
    return

while True:
    print("*** MENU CONCESIONARIO AUTOUSADOS ***")
    print("1. Consultar inventario por marca.")
    print(" 2. Búsqueda por rango de precios.")
    print("3. Modificar precio de vehículo.")
    print("4. Salir del sistema.")
    opcion = int(input("elige una opcion"))

    if opcion == 1:
        buscar = input("ingrese la marca a consultar:")
    buscr(vehiculos,buscar)


    if opcion == 2:
        precio_min = int(input("precio minimo del rango"))
        precio_max = int(input("precio maximo del rango"))
        busqueda_precio=(precio_min, precio_max)
        print
        

    if opcion == 3:
        print("h")

    if opcion == 4:
        exit