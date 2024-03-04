import numpy as np

# Note que i^0 = 1, i^1 = i, i^2 = -1, i^3 = -i, i^4 = 1, i^5 = i * i^4 = i, 
# de tal forma que o padrão se repete dependendo do resto deixado pela divisão
# do expoente por 4!

potencia = input("Digite o valor do expoente: ")

def calExp(a):
    if(a%4 == 0): print(f"o valor de i elevado a {a} eh 1")
    elif(a%4 == 1): print(f"o valor de i elevado a {a} eh i")
    elif(a%4 == 2): print(f"o valor de i elevado a {a} eh -1")
    elif(a%4 == 3): print(f"o valor de i elevado a {a} eh -i")
    return 0

calExp(potencia)