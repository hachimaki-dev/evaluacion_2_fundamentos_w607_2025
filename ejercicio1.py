#variables globales
persn_esq_incompleto = 0
persn_esq_completo = 0
dosis_esq_completo = 3
cont_dosis = 0

#While para ingresar cantidad de personas 
while True:
    try:
        num_personas = int(input("Ingrese el numero de personas que desea registrar: "))
        break        
    except ValueError:
        print("Debe ingresar un número entero")

#Bucle para preguntar por cada persona que se ingreso la cantidad de dosis que ha recibido en el vacunatorio
for i in range(num_personas):
    while True:
        try:
            dosis = int(input(f"Ingrese cantidad de dosis recibidas: "))
            if dosis >= dosis_esq_completo:
                print("Esquema completo.")
                person_esq_completo += 1
            #Profe al final me enrede y copie lo que tenia antes y le agregue el break en el else y tambien funcionó
            else:    
                print("Esquema incompleto.")
                person_esq_incompleto += 1
            break
        except ValueError:
            print("Debe ingresar un numero entero.")

print(f"Se ingresaron {num_personas} personas")
print(f"Se registraron {person_esq_completo} personas con esquema completo.")
print(f"Se registraron {person_esq_incompleto} persona con esquema incompleto.")