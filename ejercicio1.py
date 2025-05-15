arancel = 1800000
matricula = 90000

print("¡Hola, estudiante de primer año!\nVamos a calcular tus beneficios económicos según tus condiciones académicas y socioeconómicas ")

promedio = float(input("Ingresa tu promedio final con el que egresaste de tu colegio o liceo\n"))
quintil = int(input("Ingresa el quintil socioeconómico al que pertenece tu grupo familiar ('1' mayor vulnerabilidad - '5' menor vulnerabilidad)\n"))

#desc arancel
if promedio > 6.0 and quintil == 1 or quintil == 2:
    descarancel = 0.2
    resta = arancel * descarancel
    arancelfinal = arancel - resta
    print(f"El valor del arancel es: ${arancelfinal}")
elif promedio > 6.0 and quintil == 3 or quintil == 4:
    descarancel = 0.15
    resta = arancel * descarancel
    arancelfinal = arancel - resta
    print(f"El valor del arancel es: ${arancelfinal}")
elif promedio > 5.0 and promedio <= 6.0 and quintil == 1 or quintil == 2:
    descarancel = 0.13
    resta = arancel * descarancel
    arancelfinal = arancel - resta
    print(f"El valor del arancel es: ${arancelfinal}")
elif promedio > 5.0 and promedio <= 6.0 and quintil == 3 or quintil == 4:
    descarancel = 0.1
    resta = arancel * descarancel
    arancelfinal = arancel - resta
    print(f"El valor del arancel es: ${arancelfinal}")
elif promedio < 5.0 or quintil == 5:
    descarancel = 0
    resta = arancel * descarancel
    arancelfinal = arancel - resta
    print(f"El valor del arancel es: ${arancelfinal}")

#desc matricula
if quintil == 1 or quintil == 2 or quintil == 3 and promedio >= 5.5:
    descmatri = 0.15
    resta2 = matricula * descmatri
    matrifinal = matricula - resta2
    print(f"El valor de la matrícula es: ${matrifinal}")
elif quintil == 1 or quintil == 2 or quintil == 3:
    descmatri = 0.1
    resta2 = matricula * descmatri
    matrifinal = matricula - resta2
    print(f"El valor de la matrícula es: ${matrifinal}")
else:
    descmatri = 0
    resta2 = matricula * descmatri
    matrifinal = matricula - resta2
    print(f"El valor de la matrícula es: ${matrifinal}")