a = int(input("digite a parte real de z1 "))
b = int(input("digite a parte imaginária de z1 "))
c = int(input("digite a parte real de z2 "))
d = int(input("digite a parte imaginária de z1 "))
e = int(input("digite a parte real de z3 "))
f = int(input("digite a parte imaginária de z3 "))

z1 = complex(a, b)
z2 = complex(c, d)
z3 = complex(e, f)
# alternativa a)
print(f"Veja que z1 + z2 = {z1+z2} e z2 + z1 = {z2+z1}")
print(f"\nVeja que z1*z2 = {z1*z2} e z2*z1 = {z2*z1}")
print(
    f"Veja que (c1 + c2) + c3 = {((z1+z2)+z3)} é igual a c1 +(c2 + c3) = {z1+(z2+z3)}")
print(
    f"Note a distribuitivade pois z1*(z2+z3)={z1*(z2+z3)} e z1*z2 + z1*z3 = {z1*z2 + z1*z3}")
