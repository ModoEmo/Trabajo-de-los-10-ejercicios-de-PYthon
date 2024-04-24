# Pedir al usuario que introduzca la cantidad de dinero depositada en la cuenta de ahorros
cantidad_depositada = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))

ahorros_1 = cantidad_depositada * 0.04
ahorros_2 = ahorros_1 * 0.04
ahorros_3 = ahorros_2 * 0.04

ahorros_1 = round(ahorros_1, 2)
ahorros_2 = round(ahorros_2, 2)
ahorros_3 = round(ahorros_3, 2)

print("")
print("Cantidad de ahorros tras el primer año:", ahorros_1)
print("Cantidad de ahorros tras el segundo año:", ahorros_2)
print("Cantidad de ahorros tras el tercer año:", ahorros_3)