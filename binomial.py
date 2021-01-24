import math as m
def factorial(num):
    return m.factorial(num)

def convinatoria(n, x):
    return factorial(n)/(factorial(x)*factorial(n-x))

def dBinomial(n,x,p):
    return round(convinatoria(n,x)*(p**x)*(1-p)**(n-x),2)

def rango(c, f, p):
    final = 0
    for i in range(c, 4):
        s = dBinomial(f,i,p)
        final+=s
        print(s, final)
    return final

print(dBinomial(18,4,0.1))
print(round(1-rango(0,18,0.1),2))