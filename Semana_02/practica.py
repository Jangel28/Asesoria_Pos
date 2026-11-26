inventario = {
    "manzana": "$15.00",
    "leche": "$26.50",
    "pan": "$32.00",
    "huevo": "$45.00"
}

print("Consulta de precios (Escribe 'salir' para finalizar)")

while True:
    producto = input("\n¿Qué producto deseas consultar?: ").strip().lower()
    
    if producto == "salir":
        print("Programa finalizado.")
        break
        
    # Buscamos el producto en el diccionario
    if producto in inventario:
        print(f"El precio de '{producto}' es: {inventario[producto]}")
    else:
        print(f"Lo siento, '{producto}' no se encuentra en el inventario.")
