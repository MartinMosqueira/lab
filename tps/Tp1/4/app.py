def histograma_de_enteros(lista, caracter):
    archivo = open('ejercicio3.txt', 'a')
    archivo.write('--------------------')
    archivo.write('\n')
    for elementos_lista in lista:
        archivo.write(caracter*elementos_lista)
        archivo.write('\n')    
    archivo.close()
