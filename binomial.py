import math as m
def factorial(num):
    return m.factorial(num)

def convinatoria(n, x):
    return factorial(n)/(factorial(x)*factorial(n-x))


def dBinomial(n,x,p):
    return round(convinatoria(n,x)*(p**x)*(1-p)**(n-x),7)

s = 0
for i in range(0,10):
    s  = dBinomial(10,i,0.01)
    print(s)
""" final = 1 - s
print(final)     """

print("Respuesta solita")
print(dBinomial(10,3,0.4))