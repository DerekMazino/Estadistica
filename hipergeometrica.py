import math as m
def factorial(num):
    return m.factorial(num)

def convinatoria(n, x):
    return factorial(n)/(factorial(x)*factorial(n-x))


def dHiperGeometrica(K,x,N,n):
    return round((convinatoria(K,x)*convinatoria(N-K,n-x))/convinatoria(N,n),7)

""" s = 0
for i in range(0,10):
    s  = dHiperGeometrica(5,2,25,10)
    print(s) """
""" final = 1 - s
print(final)     """

print("Respuesta solita")
print(dHiperGeometrica(5,2,25,10))