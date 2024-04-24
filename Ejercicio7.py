#Definir el peso de cada payaso y muñeco en gramos
peso_payaso = 112
peso_muñecas = 75

num_payaso = int(input("Introduce el número de payasos vendidos:  "))
num_muñecas = int(input("Introduce el número de muñecas vendidas:  "))

peso_total = (num_muñecas * peso_muñecas) + (num_payaso * peso_payaso) 

print(f"El peso total del paquete que será enviado es: {peso_total} ""gramos")