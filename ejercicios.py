def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 13
if es_par(numero):
    print(numero, "es un número par.")
else:
    print(numero, "es un número impar.")