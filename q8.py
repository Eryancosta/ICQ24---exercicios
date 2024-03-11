import numpy as np
import matplotlib.pyplot as plt


v1 = np.array([2,-1])
v2 = np.array([1,1])

soma = v1+v2
diferenca = v1-v2

#soma
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vetor 1')
plt.quiver(v1[0], v1[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='y', label='Vetor 2')
plt.quiver(0, 0, soma[0], soma[1], angles='xy', scale_units='xy', scale=1, color='r', label='soma')

#diferença
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='g')
plt.quiver(v1[0], v1[1], -v2[0], -v2[1], angles='xy', scale_units='xy', scale=1, color='k', label='Vetor 2 - diferença')
plt.quiver(0, 0, diferenca[0], diferenca[1], angles='xy', scale_units='xy', scale=1, color='b', label='diferença')

plt.xlim(-1, 4)
plt.ylim(-2, 2)
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()

plt.show()
