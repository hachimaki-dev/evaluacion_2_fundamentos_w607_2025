dosis_completa=0
dosis_incompleta=0

def filtro():
        while True:
            try:
                entero=int(input())
                return entero
                break
            except ValueError:
                print("Debe ingresar un número entero")    

print("*** Sistema de Verificación de Vacunación ***")

print("Ingrese la cantidad de personas que deseas verificar:")
cantidad_personas=filtro()

for i in range(cantidad_personas):
    print(f"Ingrese la cantidad de dosis de la persona {i+1}")
    dosis=filtro()
    if dosis<3:
        print("Esquema incompleto")
        dosis_incompleta+=1
    elif dosis>=3:
        print("Esquema completo")  
        dosis_completa+=1

print(f"La cantidad de personas con Esquema completo es: {dosis_completa}")
print(f"La cantidad de personas con Esquema incompleto es: {dosis_incompleta}")
