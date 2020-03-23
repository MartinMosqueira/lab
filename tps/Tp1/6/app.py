# 1-genera una lista a partir de una string de numeros con coma


def generar_lista_numeros_con_coma(numeros):
    listaNumeros = numeros.split(',')
    return listaNumeros

# 2-genera una lista de enteros a partir de una lista de strings


def generar_lista_entera(lista_str):
    listaEntera = [int(x) for x in lista_str]
    return listaEntera

# 3-ordena los elementos de manera descendente a partir de una lista entera


def ordenamiento_lista_descendente(lista_entera):
    for recorrido in range(1, len(lista_entera)):
        for posicion in range(len(lista_entera) - recorrido):
            if lista_entera[posicion] < lista_entera[posicion + 1]:
                temp = lista_entera[posicion]
                lista_entera[posicion] = lista_entera[posicion + 1]
                lista_entera[posicion + 1] = temp
    return lista_entera
