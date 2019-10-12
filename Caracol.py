import numpy as np

def cargarTexto():
    return [a.split() for a in open("matriz.txt").readlines()]

def imprimirPrimeraPosicion(matriz):
    print (matriz[0])

def mostrar(matriz):
    imprimirPrimeraPosicion(matriz)

    if len(matriz[1:,:]) is not 0:
        mostrar(np.rot90(matriz[1:,:]))

if __name__ == '__main__':


    print ("Matriz del archivo de texto:")
    print (np.array(cargarTexto()))
    print("")

    print ("Matriz del archivo de texto en caracol:")
    mostrar(np.array(cargarTexto()))
