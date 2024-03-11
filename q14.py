import numpy as np
import matplotlib.pyplot as plt

def t_moebius(a,b,c,d,x):
    if ((a*d)-(c*b))!=0:
        return (a*x+b)/(c*x+d)
    else:
        print("ad-bc = 0, deve ser diferente de zero")

a=d=0
b=c=1

for x in range(1,11):
    print(t_moebius(a,b,c,d,x))
