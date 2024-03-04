import sympy as sp


# Defina a variável simbólica
x = sp.symbols('x')
equacao = x**2 + 2*x + 2
z1 = -1 + 1j
# Defina a equação com solução complexa


# Resolva a equação
solucoes_complexas = sp.solve(equacao, x)

# Exiba as soluções
if not solucoes_complexas:
    print("A equação não possui soluções no conjunto dos números complexos.")
else:
    print("Soluções complexas da equação:")
    for solucao in solucoes_complexas:
        print(solucao)