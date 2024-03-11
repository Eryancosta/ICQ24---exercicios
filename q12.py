import numpy as np
import matplotlib.pyplot as plt

# Criando uma lista de valores de n de 1 a 10
valores_n = np.arange(1, 11)

# Definindo uma lista de pontos no círculo unitário
theta = np.linspace(0, 2*np.pi, 100)
raio = 1
x = raio * np.cos(theta)
y = raio * np.sin(theta)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
for n in valores_n:
    plt.plot(x**n, y**n, label=f'n = {n}')

plt.title('Operação $z = z^n$ para diferentes valores de n')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Garante proporções iguais nos eixos x e y
plt.show()

'''
A operação c**n, onde c é um complexo en é um número inteiro positivo, tem um significado geométrico interessante no 
plano complexo. Quando n=1 a operação c** simplesmente retorna o próprio número complexo  Assim, não há mudança geométrica 
significativa.

Entretanto, quando n>1 a operação  resulta em uma amplificação da distância do ponto até a origem no plano complexo, 
além de uma rotação do ponto ao redor da origem. Isso acontece porque elevar um número complexo a uma potência maior 
que 1 resulta em uma amplificação da magnitude do número complexo e em uma rotação do ângulo no plano complexo.

A rotação ocorre porque a operação de potenciação em números complexos gera múltiplos ângulos quando n>1. Cada ponto 
é elevado a um múltiplo do ângulo original. Isso resulta em uma rotação do ponto ao redor da origem.

'''