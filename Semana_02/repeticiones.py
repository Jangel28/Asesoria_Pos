cantidad = 0
while cantidad <= 0:
    cantidad = int(input("Cantidad positiva:  "))
print("Cantidad aceptada: ", cantidad)

inventario = {
"tornillo": "$2.50",
"martillo": "$30.00",
"tubo": "$25.00"
}
print("consulta el precio, para finalizar escribe salir")

while True :
    producto = input("\n¿Que producto deseas consultar?").strip().lower()
    if producto == "salir":
        print("consulta terminada")
        break
    elif producto in inventario:
        print(f"El precio de '{producto}'es: {inventario[producto]}")
    else:
        print(f"Lo siento, '{producto}' no se encuentra en disponible")