comple = ""
incomple = ""
while True:
    try:
        perso_registrar = int(input("cuantas personas se van a registrar: "))
        break
    except:
        print("debe ingresar un numero entero")

for i in range(perso_registrar):
    while True:
        try:
            dosis = int(input("ingrese la cantidad de dosis que tiene:"))
            if dosis >= 3:
                print("completo")
                comple += 1
            else:
                print("incompleto")
            incomple += 1
            perso_registrar
            break
        except:
            print("numero entero")

if dosis >= 3:
    print("completo")
    comple += 1
else:
    print("incompleto")
    incomple += 1

print(f"esta completo {comple}")
print(f"esta incompleto {incomple}")