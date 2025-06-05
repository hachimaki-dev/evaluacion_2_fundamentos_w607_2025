personas = 0
while personas < 1:
    try:
        personas = int(input("Ingrese una cantidad de personas valida: "))
    except ValueError:
        print("Error 202: Solo puedes ingresar numeros.")

completo = 0
incompleto = 0
i= 0
for i in range (personas):
    
    dosis = 0
    while dosis < 1:
        try:
            dosis = int(input("Ingrse una cantidad de dosis valida: "))
        except ValueError:
            print("Error 202: solo puede ingresar numeros.")

    if dosis >= 3:
        print("esquema completo")
        completo += 1
    elif dosis < 3:
        print("esquema incompleto")
        incompleto += 1
    else:
        print("Erro 203: Lo lamentamos, Hubo un error inesperado.")

print("personas con esquema completo", completo)
print("personas con esquema incompleto", incompleto)
