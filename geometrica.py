def dGeometrica(x,p):
    return round((1-p)**(x-1)*p,7)
print(dGeometrica(3, 0.2083))

""" s=0
for i in range(1,4):
    s+=dGeometrica(i, 0.6)
print(s) """
""" total = 1 - s
print(total) """
