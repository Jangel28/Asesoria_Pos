while True:
    while True:
        producto = input("Ingresa el nombre del producto: ").strip()
        if producto:
            break
        print("El nombre del producto no puede estar vacio.")
    while True:
        try:
            precio = float(input("Ingresa el precio: "))
            if precio > 0:
                break
            print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Ingresa un precio valido.")
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad: "))
            if cantidad > 0:
                break
            print("La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Ingresa una cantidad entera valida.")
    importe = precio * cantidad
    print("\n--- Resumen de compra ---")
    print(f"Producto: {producto}")
    print(f"Precio: ${precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Importe: ${importe:.2f}")
    while True:
        respuesta = input("¿Deseas realizar otra compra? (s/n): ").strip().lower()
        if respuesta == "s":
            break
        if respuesta == "n":
            print("Gracias por tu compra. ¡Hasta luego!")
            break
        print("Respuesta no valida. Escribe s o n.")
    if respuesta == "n":
        break