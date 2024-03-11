a = int(input("digite a parte real de z1 "))
b = int(input("digite a parte imaginária de z1 "))
c = int(input("digite a parte real de z2 "))
d = int(input("digite a parte imaginária de z1 "))

z1 = complex(a, b)
z2 = complex(c, d)
print(f"|z1|*|z2| = {abs(z1)*abs(z2)} e |z1*z2| = {abs(z1*z2)}\n")
print(
    f"|z1 + z2| = {abs(z1 + z2)} e |z1|+|z2| = {abs(z1) + abs(z2)} tal que |z1+z2| <= |z1| + |z2| ")
