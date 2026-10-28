
def menu():
    print("""
    MENÚ
    1. Ingresar temperaturas
    2. Salir""")

while True:
    menu()
    opcion = input("Ingrese una opción:")
    match opcion:
        case "1":
            while True:
                dato = input("Ingrese temperatura (o 'fin' para volver al menú): ")
                if dato == "fin":
                    break
                temp = float(dato)
                if temp > 34:
                    print("T. Alta")
                elif temp < 26:
                    print("T. Baja")
                else:
                    print("T. Normal")
        case "2":
            print("Has salido")
            break
    

