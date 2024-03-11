import numpy as np
import matplotlib.pyplot as plt



def cart_polar(vet):
    return np.array([np.sqrt((vet[0]**2 + vet[1]**2)), np.arctan(vet[1]/vet[0])])




v1 = np.array([2,-1])
v2 = np.array([1,1])



v1_polar = cart_polar(v1)
v2_polar = cart_polar(v2)

soma = v1+v2
soma_polar = cart_polar(soma)



plt.figure(figsize=(10, 10))
plt.polar(v1_polar[1], v1_polar[0])
plt.ylim(0, 4)
plt.quiver(0, 0, v1_polar[1], v1_polar[0], angles='xy', scale_units='xy', scale=1, color='g', width=0.005,label='Vetor 1')
plt.quiver(0, 0, v2_polar[1], v2_polar[0], angles='xy', scale_units='xy', scale=1, color='y', width=0.005, label='Vetor 2')
plt.quiver(0, 0, soma_polar[1], soma_polar[0], angles='xy', scale_units='xy', scale=1, color='r', width=0.005, label='soma')


#diferença
dif = v1-v2
dif_polar = cart_polar(dif)

plt.quiver(0, 0, v1_polar[1], v1_polar[0], angles='xy', scale_units='xy', scale=1, color='g', width=0.005,label='Vetor 1')
plt.quiver(0, 0, v2_polar[1]+(np.pi),v2_polar[0], angles='xy', scale_units='xy', scale=1, color='m', width=0.005, label='Vetor 2')
plt.quiver(0, 0, dif_polar[1], dif_polar[0], angles='xy', scale_units='xy', scale=1, color='b', width=0.005, label='soma')



plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()

plt.show()
