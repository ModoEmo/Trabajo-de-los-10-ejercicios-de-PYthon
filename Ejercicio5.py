#Pedir al usuario su peso y estatura
peso = float(input("Introduce su peso en kg:  "))
estatura = float(input("Introduce tu estatura en metros:  "))

indice = peso / (estatura ** 2)
indice_redondeado = round(indice, 2)

print("")
print(f"Tu indice de masa corporal es: {indice_redondeado}")