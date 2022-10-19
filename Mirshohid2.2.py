import math
x=float(input('0<x<1  x='))
n=int(input('n='))
s=0
if(0<x and x<1):
    for i in range(1,n):
        s=s+(math.pow(-1,i)*math.pow(x,(2*i+1)))/(2*i+1)
print(s)

