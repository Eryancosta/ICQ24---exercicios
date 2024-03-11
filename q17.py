import numpy as np
import matplotlib.pyplot as plt


def produto_interno(m1, m2):
    return np.dot(dagger(m1), m2)

def dagger(matriz):
    return np.conjugate(transposta(matriz))

def transposta(matriz):
    return np.transpose(matriz)


def imprimir_matriz(matriz):
    np.set_printoptions(precision=3, suppress=True)
    print(matriz)


m1 = (int(input("Para a primeira matriz mxn introduza o valor de m: ")))
n1 = (int(input("Para a primeira matriz mxn introduza o valor de n: ")))
m2 = (int(input("Para a segunda matriz mxn introduza o valor de m: ")))
n2 = (int(input("Para a segunda matriz mxn introduza o valor de n: ")))

c1 = []
c2 = []

print('\n\nEntradas da primeira matriz: \n')
for i in range(0, m1):
    for j in range(0, n1):
        a = float(input("insira parte real de a{}{}: ".format(i+1,j+1)))
        b = float(input("insira parte imaginaria de a{}{}: ".format(i+1,j+1)))
        c1.append(complex(a,b))

print('\n\nMatriz c1:')
imprimir_matriz(np.array(c1).reshape(m1, n1))

print('\n\nEntradas da segunda matriz: \n')
for i in range(0, m2):
    for j in range(0, n2):
        a = float(input("insira parte real de a{}{}: ".format(i+1,j+1)))
        b = float(input("insira parte imaginaria de a{}{}: ".format(i+1,j+1)))
        c2.append(complex(a,b))

print('\n\nMatriz c2:')
imprimir_matriz(np.array(c2).reshape(m2, n2))

print("Produto interno de <C1, C2>")
dot = produto_interno(c1,c2)
imprimir_matriz(np.array(dot))







