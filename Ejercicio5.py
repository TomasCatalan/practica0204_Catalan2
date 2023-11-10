x = {}
y = input("ingresa palabras en español y sus traducciones (español:inglés), para terminar, escribe 'terminar'.")

for z in y.split(","):
    if z != "terminar":
        a, b =  z.split(":")
        x[a] = b

c = input("escriba una frase en español")

d = c.split()
e = [x.get(f,f) for f in d]

print(" ".join(e))
    