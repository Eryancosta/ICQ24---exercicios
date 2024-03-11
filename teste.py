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

# Exemplo de uso
matriz1 = np.array([[0+1j, 1],
                    [1, 0+1j]])

matriz2 = np.array([[1+0j, 0],
                    [0, 1-1j]])

print("A matriz 1 é unitária?", eh_unitaria(matriz1))
print("A matriz 2 é unitária?", eh_unitaria(matriz2))
