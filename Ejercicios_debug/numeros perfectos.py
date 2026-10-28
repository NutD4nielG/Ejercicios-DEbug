perfecto = 0

while True:
    num1 = int(input("Ingrese un número: "))
    perfecto = 0
    if num1 < 0:
        print("Has introducido un numero negativo")
        break
    for vuelta in range(1, num1):
        if num1 % vuelta == 0:
            perfecto = perfecto + vuelta
    if perfecto == num1:
        print("Es un numero perfecto")
    else:
        print("No es un numero perfecto")
