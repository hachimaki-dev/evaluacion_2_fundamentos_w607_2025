personas_registradas = []

print("===Menu principal de vacunaciones===")

# Limite de registrados
while True:  
    cantidad_registrados = int(input("Cuantas personas se van a registrar solo hay un limite de 10: "))
    if 1 <= cantidad_registrados <= 10:
        print("cantidad de personas registradas exitosamente")
        break
    else:
        print("numero no valido porfavor ingrese otro numero")
        continue

# Contadores
esquema_completo = 0
esquema_incompleto = 0

# Registracion de dosis
for i in range(cantidad_registrados):
      try:
        dosis = int(input(f"\nCuantas dosis recibio la persona {i + 1}?"))
      except:
        print("debe ingresar un numero entero")
        continue

      if dosis >=3:
         esquema_completo += 1  
      else:    
         esquema_incompleto += 1
 
 # Mostrar resultados
print(f"\nLa cantidad de personas con el esquema de vacunacion completo es: {esquema_completo}")
print(f"\nLa cantidad de personas con el esquema de vacunacion incompleto es: {esquema_incompleto}")

