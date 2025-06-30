import time


vehiculos = {
    'TOY8475': ['Toyota', 2019, '65000km', 'Gasolina', 'Automática', '1.8L 4cil', 'Blanco'],
    "TOY1111": ['Toyota', 2019, '65200km', 'Gasolina', 'Automática', '1.7L 4cil', 'Blanco'],
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
    "TOY1111" :[8400000, 4],
    'FOR2175': [6200000, 1], 
    'CHE9834': [12750000, 1],
    'NIS7654': [5400000, 2], 
    'HYU4521': [15200000, 1], 
    'KIA3456': [7800000, 1],
    'MAZ8901': [9200000, 1], 
    'SUB2468': [11500000, 0], 
    'HON1357': [6800000, 0],
}





def inventario_marca(marca):
    total_stock = 0
    
    for codigo, datos_vehiculo in vehiculos.items():
        if datos_vehiculo[0] == marca:
            if codigo in inventario:
                total_stock += inventario[codigo][1]
    
    return total_stock


print("=== CONSULTA DE INVENTARIO POR MARCA ===")
marca_usuario = input("Ingrese la marca que desea consultar: ")


cantidad = inventario_marca(marca_usuario)


if cantidad > 0:
    print(f"Inventario disponible de {marca_usuario}: {cantidad}")
else:
    print(f"No hay inventario disponible de la marca '{marca_usuario}'")

def busqueda_precio(precio_min, precio_max):
    return

def actualizar_precio(codigo, precio_nuevo):
    return

inventario_marca("Toyota")