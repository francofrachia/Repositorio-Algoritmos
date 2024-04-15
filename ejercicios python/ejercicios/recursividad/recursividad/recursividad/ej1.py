#Suma Fibonacci#
def sumaRec (numero):
    
    if numero == 0 or numero == 1:
        return numero
    else:
        return sumaRec(numero - 1) + sumaRec(numero - 2)

print(sumaRec(11))