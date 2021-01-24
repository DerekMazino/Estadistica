import math as m
def factorial(num):
    return m.factorial(num)

def convinatoria(n, x):
    return factorial(n)/(factorial(x)*factorial(n-x))

def dBinomial(n,x,p):
    return convinatoria(n,x)*(p**x)*(1-p)**(n-x)

print(dBinomial(18,2,0.1))