import numpy as np
import matplotlib.pyplot as plt

#matrizes complexas para teste 2x2
c1 = np.array([[1+1j, 2],
      [0, 2+1j]
     ])

c2 = np.array([[0, 2j],
      [1j, 2+1j]
     ])

#função soma
def soma(m1, m2):
    return np.array((m1+m2))

#função multiplicação por escalar
def m_esc(n, m1):
    return np.array([[n * elem for elem in row] for row in m1])

#função inversa
def inversa(m1):
    return np.linalg.inv(m1)

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

c1 = np.array(c1).reshape(m1,n1)
c2 = np.array(c2).reshape(m2,n2)
soma = soma(c1,c2)

print("soma c1+c2")
imprimir_matriz(soma)

n = float(input('Introduza um escalar para multiplicar a primeira matriz: '))
print('n*c1')

multi = m_esc(n,c1)
print("multiplicação por escalar")
imprimir_matriz(multi)

print('Inversa de c1')
inv = np.array(inversa(c1)).reshape(m1,n1)
imprimir_matriz(inv)