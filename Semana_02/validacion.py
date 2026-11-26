while True:
    try:
        cantidad= int(input("Cantidad: "))
        if cantidad > 0:
            break
        print("Debe ser mayor que cero")
    except ValueError:
        print("Escribe un número entero")
print("Cantidad válida: ", cantidad)

while True:
    try:
        cantidad= float(input("Cantidad: "))
        if cantidad > 0:
            break
        print("Debe ser mayor que cero")
    except ValueError:
        print("Escribe un número decimal")
print("Cantidad válida: ", cantidad)