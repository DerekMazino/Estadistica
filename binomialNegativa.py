import math as m
def factorial(num):
    return m.factorial(num)

def convinatoria(n, x):
    return factorial(n)/(factorial(x)*factorial(abs(n-x)))


def dBinomialNegativa(r,x,p):
    return round(convinatoria(x-1,r-1)*(1-p)**(x-r)*p**r,7)

s = 0
for i in range(1,4):
    pp = dBinomialNegativa(3,i,0.6)
    print(pp)
    s  += pp
print(s)

""" final = 1 - s
print(final)    """ 

print("Respuesta solita")
print(dBinomialNegativa(3,1,0.6))