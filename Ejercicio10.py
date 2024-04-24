#Pedir al usuarios que ingrese el nombre de su producto

nombre_producto = input("Ingrese el nombre del producto:  ")
precio_unitario = float(input("Ingrese el precio unitario del producto:  "))
unidades = int(input("Ingrese el número de unidades:  "))

costo_total = precio_unitario * unidades 

print("")
print(f"{nombre_producto.upper()}: Precio unitario - ${precio_unitario:6.2f}, unidades - {unidades:03d}, Costo total - ${costo_total:8.2f}")