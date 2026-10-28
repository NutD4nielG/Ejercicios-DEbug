#Eh, profe, no alcancé
digito = 0

while True:
    num1 = int(input("Ingrese un número: "))
    if num1 < 0:
            print("Has introducido un numero negativo")
            break
    cant = 0
    while num1 > 0:
        digito = num1 % 10
        num1 = num1 // 10
        cant += 1 
        print(digito)
    print("vueltas:",cant)