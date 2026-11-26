precio= 25.0
cantidad= 2
existencias= 5
activo= True
if activo and precio > 0 and 0 < cantidad <= existencias:
    print ("Se puede continuar")
else:
    print ("Revisar los datos")
print (not activo)

