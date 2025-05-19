import random





print("-----BIENVENIDO-----\n")
print("\nINGRESE UN RANGO ENTRE DOS NUMEROS ")




while True:
    num1= int(input("INGRESE EL PRIMER NUMERO (debe ser menor al segundo): "))
    num2= int(input("INGRESE NUNMERO DOS: "))
    if num1 > num2:
        print("-----DATOS INVALIDOS VUELVA A INGRESAR-----")
        num1= int(input("INGRESE EL PRIMER NUMERO (debe ser menor al segundo): "))
        num2= int(input("INGRESE NUNMERO DOS: "))
    else:
        break




num_random= random.randint(num1,num2)
intentos= 3
while intentos == 3:
    intento1= int(input("INTENTE ADIVINAR EL NUMERO SECRETO\nINGRESE SU NUMERO: "))
    if intento1 == num_random:
        print("FELICIDADES, ADIVINASTE A LA PRIMERA!!!")
        break
    elif intento1 < num_random:
        print("EL NUMERO INGRESADO ES MENOR AL NUMERO SECRETO")
    else:
        if intento1 > num_random:
            intentos= intentos - 1
            print("EL NUMERO INGRESADO ES MAYOR AL NUMERO SECRETO")


    intento2= int(input("SEGUNDO INTENTO: "))
    if intento2 == num_random:
        print("FELICIDADES ADIVINASTE")
        break
    elif intento2 < num_random:
        intentos= intentos - 1
        if num1 < num2:
            print(" EL NUMERO INGRESADO ESTA MAS CERCA QUE EL NUMERO ANTERIOR")
            print("EL NUMERO INGRESADO ES MENOR AL NUMERO SECRETO")
    else:
        if intento1 > num_random:
            intentos= intentos - 1
            if num1 > num2:
                print("EL NUMERO INGRESADO ES MAS CERCANO QUE EL ANTERIOR")
                print("EL NUMERO INGRESADO ES MAYOR AL NUMERO SECRETO")


    intento3= int(input("ULTIMO INTENTO: "))
    if intento3 == num_random:
        print("GANASTE!!")
        break
    else:
        print("PERDISTE:c")
        print("El numero secreto era" ,num_random)
        intentos == 0
