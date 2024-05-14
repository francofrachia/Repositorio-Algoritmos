def romano_a_decimal(romano, valores):
    if len(romano) == 0:
        return 0
    
    valor_actual = valores[romano[0]]
    
    if len(romano) == 1:
        return valor_actual
    
    if valores[romano[0]] < valores[romano[1]]:
        return -valor_actual + romano_a_decimal(romano[1:], valores)
    else:
        return valor_actual + romano_a_decimal(romano[1:], valores)

valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Ejemplo
numero_romano = "MMXIV"
print("Número romano:", numero_romano)
print("Número decimal:", romano_a_decimal(numero_romano, valores_romanos))
