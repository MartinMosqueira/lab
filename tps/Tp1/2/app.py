def suma_de_numeros_repetidos(numero,repeticion):
    listaNumero = []
    sumaNumero = 0
    elemento = numero
    for posicion_listaNumero in range(repeticion+1):
        elemento = str(numero)*posicion_listaNumero
        listaNumero.append(elemento)
    listaNumero.pop(0)
    listaNumeroEntera = [int(x) for x in listaNumero]
    for elemento_listaNumero in listaNumeroEntera:
        sumaNumero += elemento_listaNumero
    return sumaNumero
