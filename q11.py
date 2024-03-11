import numpy as np
import matplotlib.pyplot as plt



def produto_r(complexo, real):
    return complexo * real

def produto_c(complexo, imag):
    return complexo * imag

def c_polar(complexo):
    return np.array([np.sqrt((complexo.real**2 + complexo.imag**2)), np.arctan2(complexo.imag,complexo.real)])

c1 = 1+2j
c2 = 3+2j

resultado_r = produto_r(c1,c2.real)
resultado_i = produto_c(c1, c2.imag)

resultado_polar = c_polar(resultado_r)
resultado_polar2 = c_polar(resultado_i)

plt.figure(figsize=(8, 8))
plt.polar(resultado_polar[1], resultado_polar[0])
plt.ylim(0, resultado_polar[0]+2)

plt.quiver(0, 0, resultado_polar[1], resultado_polar[0], angles='xy', scale_units='xy', scale=1, color='g', width=0.005, label = "produto_r")
plt.quiver(0, 0, resultado_polar2[1], resultado_polar2[0], angles='xy', scale_units='xy', scale=1, color='r', width=0.005, label = "produto_r")



plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()

plt.show()
