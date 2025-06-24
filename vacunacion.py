esquema_completo=0
esquema_incompleto=0
while True:
    try:
        cantidad_personas= int(input("ingrese la cantidad de gente a registrar: "))
        break 
    except ValueError: 
        print("debe poner un n enterro")
        
for i in range (cantidad_personas):
    while True:
        try:
            dosis= int(input("ingrese cantidad de dosis q recibio: "))
            if dosis >=3:
                 print("toas las vakunas")
                 esquema_completo+=1 
            else: 
                 print("no todas las vacunas")
                 esquema_incompleto+=1 
            break 
        except ValueError:
                 print("debe ingresar un n entero") 
  
print(f"se registraron {esquema_completo} personas con esquema completo")
print(f"se registraron {esquema_incompleto} persona con esquema incompleto")