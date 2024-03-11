import numpy as np

def eh_unitaria(matriz):
    # Verifica se a matriz é quadrada
    linhas, colunas = matriz.shape
    if linhas != colunas:
        return False

    # Calcula o produto entre a matriz e sua adjunta
    produto = np.dot(matriz, np.conjugate(matriz).T)

    # Verifica se o resultado é próxima da matriz identidade
    identidade = np.eye(linhas)
    return np.allclose(produto, identidade)

def imprimir_matriz(matriz):
    np.set_printoptions(precision=3, suppress=True)
    print(matriz)

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

c2 = np.array([[1/np.sqrt(2), 1/np.sqrt(2)],
              [-1/np.sqrt(2), 1/np.sqrt(2)]])

m2,n2 = c2.shape
c1 = np.array(c1).reshape(m1, n1)

print("A matriz 1 é unitária?", eh_unitaria(c1))

print('\nexemplo de matriz unitara:\n')
imprimir_matriz(np.array(c2).reshape(m2, n2))
print("\nA matriz 2 é unitária?", eh_unitaria(c2))
