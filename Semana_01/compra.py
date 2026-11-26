producto= input("Ingresa un producto:")
print(producto)
precio= input("dame el precio:")
print(precio)
cantidad= input("Cuantas unidades:")
print(cantidad)
total=(float (precio) * int (cantidad))
print("{:.2f}".format(total))

