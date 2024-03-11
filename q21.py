import numpy as np

def imprimir_matriz(matriz):
    np.set_printoptions(precision=3, suppress=True)
    print(matriz)

def prod_tensorial(m1,m2):
    return np.kron(m1,m2)


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

print("Produto tensorial de C1 e C2")

prod_tens = np.array(prod_tensorial(c1,c2)).reshape(m1*m2,1)

imprimir_matriz(prod_tens)
