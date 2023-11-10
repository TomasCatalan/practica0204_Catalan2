x = {'Pan': 1.40, 'Huevos': 2.30, 'Cebolla': 0.85, 'Aceite': 4.35}
y = input("Ingrese el nombre del artículo")
z = int(input("Ingrese el número de unidades"))

if y in x:
    a = x[y] * z
    print("El precio de", z, "unidades es de", a, "€")
else:
    print("Lo siento, el artículo no está en la lista")