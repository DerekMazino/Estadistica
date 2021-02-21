import math as m
def dPoisson(lamda,x):
    return ((m.exp(-lamda)*lamda**x/m.factorial(x)),7)
print(dPoisson(2.3,2))