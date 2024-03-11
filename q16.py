import numpy as np
import matplotlib.pyplot as plt

def imprimir_matriz(matriz):
    np.set_printoptions(precision=3, suppress=True)
    print(matriz)

def transposta(matriz):
    return np.transpose(matriz)

def conjugado(matriz):
    return np.conjugate(matriz)

def dagger(matriz):
    return np.conjugate(transposta(matriz))


m1 = (int(input("Para a primeira matriz mxn introduza o valor de m: ")))
n1 = (int(input("Para a primeira matriz mxn introduza o valor de n: ")))


c1 = []


print('\n\nEntradas da primeira matriz: \n')
for i in range(0, m1):
    for j in range(0, n1):
        a = float(input("insira parte real de a{}{}: ".format(i+1,j+1)))
        b = float(input("insira parte imaginaria de a{}{}: ".format(i+1,j+1)))
        c1.append(complex(a,b))

print('\n\nMatriz c1:')
imprimir_matriz(np.array(c1).reshape(m1, n1))

print("\nTransposta de c1")
imprimir_matriz(np.array(transposta(c1)).reshape(n1, m1))

print('\nconjugada de c1')
imprimir_matriz(np.array(conjugado(c1)).reshape(m1, n1))

print('Dagger de c1')
imprimir_matriz(np.array(dagger(c1)).reshape(n1, m11))







