import sympy as sp


x = sp.symbols('x')

equacao = x**4 + 2*x**2 + 1


solucoes = sp.solve(equacao, x)



print("Sendo I o número imaginário, As soluções da equação são:")
for solucao in solucoes:
    print(solucao)