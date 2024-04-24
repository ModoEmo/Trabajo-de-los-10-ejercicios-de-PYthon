def proceso_edad():
    edad = int(input("Introduzca la edad:  "))
    
    if edad >= 1 and edad <= 90:
        if edad >= 18:
            print("")
            print("Eres mayor de edad")
        else:
            print("")
            print("Eres menor de edad")
    else:
        print("Error: Edad fuera de rango")

proceso_edad()