
comple = ""
incomple = ""
while True:
    try:
        perso_registrar = int(input("cuantas personas se van a registrar: "))
        break
    except:
        print("Error, intente de nuevo")

for i in range(perso_registrar):
    while True:
        try:
            dosis = int(input("ingrese la cantidad de dosis que tiene:"))
            break
        except:
            print("debe ingresar un numero entero:")

if dosis >= 3:
    print("completo")
    comple += 1
else:
    print("incompleto")
    incomple += 1

print(f"esta completo {comple}")
print(f"esta incompleto {incomple}")