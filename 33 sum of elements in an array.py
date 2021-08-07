from array import *
from math import *
a=array("i",[])
b=int(input("enter size :"))
sum=0
for x in range(b):
    c=int(input())
    a.append(c)
    sum=sum+c
print(sum)

print(a.reverse())
#or
print(a[::-1])