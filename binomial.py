import math as m
def factorial(num):
    return m.factorial(num)

def convinatoria(n, x):
    return factorial(n)/(factorial(x)*factorial(n-x))


def dBinomial(n,x,p):
    return round(convinatoria(n,x)*(p**x)*(1-p)**(n-x),5)

s = 0
for i in range(0,5):
    s  += dBinomial(20,i,0.2)
final = 1 - s
print(final)    

#print(dBinomial(20,i,0.2))