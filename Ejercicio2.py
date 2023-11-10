x = input("nombre")
y = input("edad")
z = input("direccion")
a = input("telefono")


b = {'nombre': x,'edad': y, 'direccion': z,'telefono': a}


print([b["nombre"]], "tiene", [b["edad"]], "vive en", [b["direccion"]], "y su numero es", [b["telefono"]] )