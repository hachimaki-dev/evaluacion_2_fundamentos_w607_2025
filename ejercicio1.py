pacientes = 0

def dosis():
    for i in range(personas_registradas):
        print(f"Cuantas dosis ha recibido el paciente {pacientes + 1}")
        break





while True:
    try:
        print("Cuantas personas seran ingresadas")
        personas_registradas = int(input("Ingrese:"))
        dosis()
    except ValueError:
        print("No decimales ni letras, solo enteros!!")
        continue



