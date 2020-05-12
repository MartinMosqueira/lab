import os
import argparse
from multiprocessing import Process

analizador = argparse.ArgumentParser()
analizador.add_argument("-f", help="archivo en formato ppm")
analizador.add_argument("-n", help="Blocke de bytes que se van a leer")
argumento = analizador.parse_args()


archivo = os.open(argumento.f, os.O_RDWR)
leer=os.read(archivo,int(argumento.n))

def rojo():
    rojo = os.open('rojo.ppm', os.O_RDWR)
    cadena=bytearray(leer)
    pos=16
    pos1=17
    i=0
    while i <= 19990:
        cadena[pos]=0
        cadena[pos1]=0
        pos+=3
        pos1+=3
        i+=1

    leer_rojo=os.write(rojo,cadena)
    
def azul():
    azul = os.open('azul.ppm', os.O_RDWR)
    cadena=bytearray(leer)
    pos=15
    pos1=16
    i=0
    while i <= 19990:
        cadena[pos]=0
        cadena[pos1]=0
        pos+=3
        pos1+=3
        i+=1

    leer_azul=os.write(azul,cadena)

def verde():
    verde = os.open('verde.ppm', os.O_RDWR)
    cadena=bytearray(leer)
    pos=15
    pos1=17
    i=0
    while i <= 19990:
        cadena[pos]=0
        cadena[pos1]=0
        pos+=3
        pos1+=3
        i+=1

    leer_verde=os.write(verde,cadena)

v = Process(target=verde(), args=())
a = Process(target=azul(), args=())
r = Process(target=rojo(), args=())

v . start()
a . start()
r . start()












# tamaño=os.path.getsize(imagen)
# with open('Paisaje.ppm', 'r') as f:
#data = f.readlines()
