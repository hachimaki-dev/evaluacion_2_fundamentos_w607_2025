#| Promedio                          | Quintil                          | Descuento en Arancel |
#| --------------------------------- | -------------------------------- | -------------------- |
#| Mayor a 6.0                       | Quintil 1 o 2                    | 20%                  |
#| Mayor a 6.0                       | Quintil 3 o 4                    | 15%                  |
#| Mayor a 5.0 y menor o igual a 6.0 | Quintil 1 o 2                    | 13%                  |
#| Mayor a 5.0 y menor o igual a 6.0 | Quintil 3 o 4                    | 10%                  |
#| Cualquier promedio                | Quintil 5 o promedio 5.0 o menos | 0%                   |

base_arancel = 1800000
base_matricula = 90000
continuar = True

print("Bienvenido")

promedio_final = float(input("Ingrese Promedio:")) 

if promedio_final > 7.0 or promedio_final < 1.0:
    print("Valor Ingresado Incorrecto")

quintil = int (input("Ingrese Quintil (1, 2, 3, 4, 5.)"))

if quintil > 5 or quintil < 1:
    print("Valor ingresado incorrecto")


if (quintil == 1 or quintil == 2) and (promedio_final > 6.0): #mayor a 6.0 y quintil 1 o 2
    base_arancel -= base_arancel * 0.2
    base_matricula -= base_matricula * 0.15
    print ("El valor del arancel es: $", base_arancel)  
    print ("El valor de la matrícula es: $", base_matricula)
elif (quintil == 3 or quintil == 4) and (promedio_final > 6.0): #mayor a 6.0 y quintil 3 o 4
    base_arancel -= base_arancel * 0.15
    base_matricula -= base_matricula * 0.15
    print ("El valor del arancel es: $", base_arancel)  
    print ("El valor de la matrícula es: $", base_matricula)
elif (quintil == 1 or quintil == 2) and (promedio_final <= 6.0 and promedio_final >= 5.5 ): #mayor a 5 y menor o igual a 6.0 y quintil 1 o 2 con descuento matricula
    base_arancel -= base_arancel * 0.13
    base_matricula -= base_matricula * 0.15
    print ("El valor del arancel es: $", base_arancel)  
    print ("El valor de la matrícula es: $", base_matricula)
elif (quintil == 1 or quintil == 2) and (promedio_final > 5.0 and promedio_final < 5.5 ): #mayor a 5 y menor o igual a 6.0 y quintil 1 o 2
    base_arancel -= base_arancel * 0.13
    base_matricula -= base_matricula * 0.10
    print ("El valor del arancel es: $", base_arancel)  
    print ("El valor de la matrícula es: $", base_matricula)
elif (quintil == 3 or quintil == 4) and (promedio_final <= 6.0 and promedio_final >= 5.5 ): #mayor a 5 y menor o igual a 6.0 y quintil 3 o 4 con descuento matricula
    base_arancel -= base_arancel * 0.13
    base_matricula -= base_matricula * 0.15
    print ("El valor del arancel es: $", base_arancel)  
    print ("El valor de la matrícula es: $", base_matricula)    
elif (quintil == 3 or quintil == 4) and (promedio_final > 5.0 and promedio_final < 5.5 ): #mayor a 5 y menor o igual a 6.0 y quintil 3 o 4
    base_arancel -= base_arancel * 0.13
    base_matricula -= base_matricula * 0.10
    print ("El valor del arancel es: $", base_arancel)  
    print ("El valor de la matrícula es: $", base_matricula)
elif (quintil == 5) and (promedio_final >= 5.5):
    base_matricula -= base_matricula * 0.05 
    print ("El valor del arancel es: $", base_arancel)  
    print ("El valor de la matrícula es: $", base_matricula)
elif (quintil == 5) and (promedio_final < 5.5):
    print ("El valor del arancel es: $", base_arancel)  
    print ("El valor de la matrícula es: $", base_matricula)


print("Godines")   

