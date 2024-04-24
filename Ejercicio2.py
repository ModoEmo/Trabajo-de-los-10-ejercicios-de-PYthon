
# Pedir al usuario el número de horas trabajadas y el coste por hora

horas_trabajadas = float(input("Por favor, introduce el número de horas trabajadas: ")) 
coste_por_hora = float(input("Por favor, introduce el coste por hora: "))

paga = horas_trabajadas * coste_por_hora

print("")
print(f"La paga correspondiente es: ${paga}")