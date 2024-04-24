n=int(input("Introduce un número entero positivo:  "))

if n <= 0:
    print("")
    print("Por favor, introduce un número entero positivo")
else:
    suma = n * (n+1) // 2
    print("")
    print(f"La suma de todos los enteros desde 1 hasta {n} es: {suma}")    
