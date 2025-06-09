print("Sistema verficacion de vacunas")

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("ingrese un numero entero")
            else:
                return valor
        except ValueError:
            print("ingrese un numero entero")
            
            
cantidad = pedir_entero("Ingrese la cantidad de vacunados")
 
for i in range (1,cantidad +1):
    print(f"peronas {i}:")
dosis = pedir_entero("Ingrese la cantidad de personas registradas")  

if dosis >=3:
    print("Esquema completo")
else:
    print("Esquema incompleto")




