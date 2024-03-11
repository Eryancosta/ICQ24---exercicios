import numpy as np
import matplotlib.pyplot as plt

# Criando uma lista de valores de i de 0 a 10
valores_i = np.arange(0, 11)

# Definindo uma lista de pontos no círculo unitário
c = 1
vetor_complexo = []

for i in valores_i:
    vetor_complexo.append(c + complex(0, i))

# Plotando o gráfico
plt.figure(figsize=(10, 6))
for i in range(0, 10):
    raio = np.abs(vetor_complexo[i])
    theta = np.linspace(0, np.angle(vetor_complexo[i]), 100)
    x = raio * np.cos(theta)
    y = raio * np.sin(theta)    
    plt.plot(x, y, label=f'i = {i}')

plt.title('Operação $c = c + i$ para diferentes valores de i')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
