from array import *
from math import *
a=array("i",map(int,input("enter the value :").split()))
x=[]
y=[]
for i in range(ceil(len(a)/2)):
    x.append(a[i])
for i in range(ceil(len(a)/2),len(a)):
    y.append(a[i])
print(sorted(x))
y.sort()
print(y[::-1])
xy=sorted(x)+y[::-1]
print(xy)