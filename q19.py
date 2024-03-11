import numpy as np


def imprimir_matriz(matriz):
    np.set_printoptions(precision=3, suppress=True)
    print(matriz)

def eh_hermitiana(matriz):
    # Verifica se a matriz é quadrada
    linhas, colunas = matriz.shape
    if linhas != colunas:
        print('A matriz não é quadrada')
        return False

    # Verifica se a matriz é igual à sua própria dagger
    if np.allclose(matriz, np.conj(matriz).T):
        return True
    else:
        return False

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


c1 = np.array(c1).reshape(m1, n1)

print("A matriz 1 é hermitiana?", eh_hermitiana(c1))










