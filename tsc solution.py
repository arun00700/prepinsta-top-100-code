#multiply the digits
from array import *
a=int(input())
b=[]
if a<10:
    print("Not possible")

if a>=10:
  for x in range(9,1,-1):
     while a%x==0:
          b.append(x)
          a=a/x

if len(b)==0:
    print("Not Possible")

for x in range(0,len(b)):
    print(b[-1-x],end="")
