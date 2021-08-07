from array import *
a=array("i",[])
b=int(input("enter size :"))
for x in range(b):
    c=int(input())
    a.append(c)
a1=sorted(a)
print(min(a))
print(a1[1])
