def usar_la_fuerza(mochila, index=0):
    if index >= len(mochila):
        return (False, index)
    
    objeto = mochila[index]

    if objeto == "sable de luz":
        return (True, index + 1)
    else:
        return usar_la_fuerza(mochila, index + 1)
        
mochila = ["libro", "botella de agua", "sable de luz", "ropa"]
    
resultado = usar_la_fuerza(mochila)

print(f"¿Se encontró el sable de luz? {'Sí' if resultado[0] else 'No'}")
print(f"Objetos sacados de la mochila hasta encontrarlo: {resultado[1]}")