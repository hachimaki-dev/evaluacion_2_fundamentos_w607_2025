vehiculos = {
    'TOY8475': ['Toyota', 2019, '65000km', 'Gasolina', 'Automática', '1.8L 4cil', 'Blanco'],
    'FOR2175': ['Ford', 2017, '85000km', 'Gasolina', 'Manual', '1.6L 4cil', 'Azul'],
    'CHE9834': ['Chevrolet', 2020, '25000km', 'Gasolina', 'Automática', '2.0L 4cil', 'Negro'],
    'NIS7654': ['Nissan', 2016, '95000km', 'Gasolina', 'Manual', '1.6L 4cil', 'Rojo'],
    'HYU4521': ['Hyundai', 2021, '15000km', 'Híbrido', 'Automática', '1.6L 4cil', 'Gris'],
    'KIA3456': ['Kia', 2018, '75000km', 'Diesel', 'Manual', '2.0L 4cil', 'Blanco'],
    'MAZ8901': ['Mazda', 2019, '55000km', 'Gasolina', 'Automática', '2.5L 4cil', 'Rojo'],
    'SUB2468': ['Subaru', 2020, '30000km', 'Gasolina', 'Manual', '2.0L 4cil', 'Verde'],
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
}
print("sistema finalizado correctamente.")
print("MENU CONCESIONARIO AUTOUSADOS")
print("1. Consultar inventario por marca")
print("2. Búsqueda por rango de precios")
print("3. Modificar precio de vehículo")
print("4. Salir del sistema")
def inventario_marca(marca):
    print(f"inventario de vehiculos de la marca {marca}:")
    total_stock = 0
    for codigo, vehiculo in vehiculos.items():
        if vehiculo[0].lower() == marca.lower(): 
            if codigo in inventario and inventario[codigo][1] > 0:
                total_stock += inventario[codigo][1]

    print(f"El inventario de {marca.title()} es: {total_stock}")
    return
def busqueda_precio(precio_minimo, precio_maximo):
    return
def actualizar_precio(codigo, precio_nuevo):
    return
while True:
    opcion = input("Ingrese opción")  
    if opcion == "1":
        marca = input("Ingrese marca a consultar")
        inventario_marca(marca)
    elif opcion == "2":
        while True:
            try:
                precio_min = int(input("Ingrese precio mínimo"))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        while True:
            try:
                precio_max = int(input("Ingrese precio máximo"))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        busqueda_precio(precio_min, precio_max)
    elif opcion == "3":
        while True:
            codigo = input("Ingrese código del vehículo a actualizar")
            try:
                precio_nuevo = int(input("Ingrese precio nuevo"))
            except ValueError:
                print("Debe ingresar un valor entero")
                continue
            if actualizar_precio(codigo, precio_nuevo):
                print("Precio actualizado exitosamente")
            else:
                print("El código del vehículo no existe")
            continuar = input("¿Desea actualizar otro precio (s/n)?: ")
            if continuar.lower() != "s":
                break         
    elif opcion == "4":
        print("Sistema finalizado correctamente.")
        break      
    else:
        print("Debe seleccionar una opción válida!!")
    print()