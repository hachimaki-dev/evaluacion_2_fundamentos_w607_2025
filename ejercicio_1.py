print("====Bienvenido al sistema de vacunaciones====")


def solicitar_entero(mensaje):
  
  while True:
   
   entrada = input(mensaje)

   if entrada.strip() =="":
      
      print("no se ingresaron numeros. intente de nuevo")

      continue
   
   try:
       
       numero = int(entrada)

       if 1 <= numero <= 10:
          
          return numero
       else:

        print("el numero debe estar enetre 1 y 10")

   except ValueError:
      
        print("debe ingresar un numero entero")
        
   
    
# Solicitar el numero de personas registradas

registrados = solicitar_entero("Cantidad de personas registradas: ")

# Contadores

esquema_completo = 0

esquema_incompleto = 0

# Registrar dosis de cada uno

for i in range(registrados):

 dosis = solicitar_entero(f"\nCuantas dosis tiene la persona {i + 1}?: ")


if dosis >=3:

   esquema_completo += 1

else:

   esquema_incompleto += 1

# Resultados finales


print(f"\nPersonas con el esquema completo: {esquema_completo}")

print(f"Personas con el esquema incompleto: {esquema_incompleto}")


