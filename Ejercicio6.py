x = {}

while True:
    print("\nMenú:")
    print("(1) Añadir alumno")
    print("(2) Eliminar alumno")
    print("(3) Mostrar alumno")
    print("(4) Listar todo el alumnado")
    print("(5) Listar alumnado aprobado")
    print("(6) Terminar")

    y = input("Ingrese el número de la opción deseada: ")

    if y == '1':
        z = input("Ingrese el NIF del alumno")
        a = input("Ingrese el nombre del alumno")
        b = input("Ingrese los apellidos del alumno")
        c = input("Ingrese el teléfono del alumno")
        d = input("Ingrese el correo del alumno")
        e = input("¿El alumno ha aprobado el módulo? (SI/NO)").lower() == 'SI'
    
        x[z] = {
            'Nombre': a,
            'Apellidos': b,
            'Teléfono': c,
            'Correo': d,
            'Aprobado': e
        }
        print("Alumno añadido a la base de datos")
    
    elif y == '2':
        z = input("Ingrese el NIF del alumno a eliminar")
        if z in x:
            del x[z]
            print("Alumno eliminado de la base de datos")
        else:
            print("No se encontró al alumno en la base de datos")

    elif y == '3':
        z = input("Ingrese el NIF del alumno")
        if z in x:
            print("\nDatos del alumno")
            for f, g in x[z].items():
                print(f,":",g)
        else:
            print("No se encontró al alumno en la base de datos.")
    
    elif y == '4':
        print("\nLista de todo el alumnado")
        for z, h in x.items():
            print(f"NIF: {z}, Nombre: {h['Nombre']}")
    
    elif y == '5':
        print("\nLista de alumnado aprobado")
        for z, h in x.items():
            if h['Aprobado']:
                print(f"NIF: {z}, Nombre: {h['Nombre']}")
    
    elif y == '6':
        print("Programa terminado.")
        break