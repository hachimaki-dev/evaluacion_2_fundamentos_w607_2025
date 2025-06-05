 

while True:
    try:
        personas_registradas = int(input("Ingrese cantidad de personas que se desean registrar: "))
        break 
    except:
        print("Error la cantidad de personas debe ser en numero entero positivo")